# alleles.py
from __future__ import annotations
import sys
from collections.abc import Collection
from typing import Annotated, Union

import pandas as pd
from Bio.AlignIO import MultipleSeqAlignment
from Bio.Seq import Seq
from Bio.SeqIO import SeqRecord
from vcfpy import Call, Reader, Record

import oddsnends as oed
from genomicspy.main import SeqType, seq_astype


__all__ = [
    "SampleErrorHandlingType",
    "VCF_DEFAULT_DICT",
    "_combine_ivrs_variants",
    "calc_circular",
    "calc_ivrs",
    "check_overlap",
    "gen_alleles_for_chrom_vcf",
    "gen_alleles_from_variants_df",
    "gen_alleles_from_vcf",
    "gen_ivr_records", 
]

SampleErrorHandlingType = Annotated[str, "ignore", "force", "raise" ]

VCF_DEFAULT_DICT = {"ID": [],
                    "QUAL": None,
                    "FILTER": ["PASS"],
                    "INFO": {},
                    "FORMAT": ["GT"],
                    }

## Helpers
def calc_circular(pos: pd.Series, length: int):
    """Calculate real positions on circle as 1-indexed"""
    return (pos % length).mask(lambda ser: ser == 0, length)


def check_overlap(variants: pd.DataFrame,
                  chrom: str,
                  chrom_col: str = "CHROM",
                  start_col: str = "POS",
                  end_col: str = "END_POS",
                  length: int = None,
                  is_circular: bool = False,
                  errout: str = ".",
                  ) -> None:
    """Check if intervals of entries overlap.

    Intervals are right-open and 1-indexed.

    Parameters
    ------------
    df: pd.DataFrame
    chrom:      str  
    chrom_col:  str     Name of chrom col. Default "CHROM
    start_col:  str     Col name of interval start index
    end_col:    str     Col name of interval end index
    length:     int     Total contig length. Required if is_circular is True

    Optional:
    is_circular: bool   Treat entries on circular contig. Default False
    errout:      str    Output directory for error files. Default "."

    Returns:  None
    """
    assert not(is_circular and length is None), \
        f"is_circular is {is_circular} but length is {length}"


    # get interval start and end columns
    entries = variants.loc[variants["CHROM"] == chrom, [start_col, end_col]]

    # group entries by each position and count
    # resulting df has index as pos, values as ids from entries index and n_ids
    positions = oed.ranges2locs(
        entries, col_start=start_col, col_end=end_col,
        ignore_index=False, drop_duplicates=False)
    

    if is_circular:

        # calculate real position on a circular chromosome
        positions = calc_circular(positions, length)

        # make same pos val as dot for easier reading
        entries[f"{end_col}_circ"] = (
            calc_circular(entries[end_col], length)
            .mask(lambda ser: entries[end_col] <= ser, ".")
        )

    
    positions = (
        positions
        .rename_axis("variants_index")
        .reset_index(name="pos")
        .pivot_table("variants_index", "pos", aggfunc=lambda x: x)
    )
    positions["n_variants"] = positions["variants_index"].apply(
        lambda x: x if isinstance(x, Collection) else [x]).apply(len)

    try:
        # check if there are overlaps
        overlaps = positions.loc[positions.n_variants > 1]
        assert len(overlaps) == 0, "Overlapping entries exist."

    except AssertionError:

        # ranges of overlap
        overlap_ranges = oed.calc_intervals(overlaps.index)

        # ids corresponding to entries index
        overlap_ids = overlaps["variants_index"].explode().drop_duplicates()

        overlap_entries = (
            entries.loc[overlap_ids, :]
            .assign(**{chrom_col: chrom})
            .pipe(variants.merge, "inner", on=[chrom_col, start_col, end_col])
            )

        suffix = oed.default(chrom, "", has_value=f".{chrom}")

        # save entries for review
        positions_check_fname = f"positions_check{suffix}.tsv"
        positions.to_csv(f"{errout}/{positions_check_fname}", sep="\t")

        overlap_entries_fname = f"overlapping_variants{suffix}.tsv"
        overlap_entries.to_csv(f"{errout}/{overlap_entries_fname}", sep="\t")

        print(
            ">> OVERLAPS",
            f">> {len(overlap_ranges)} intervals span {len(overlaps)} position:",
            "",
            *(f"{chrom}:{i}-{j}" for i, j in overlap_ranges),
            "",
            f">> {len(overlap_entries)} overlapping entries:",
            overlap_entries.to_string(),
            "",
            ">> Checks and ranges saved to:",
            f"    {positions_check_fname} and ",
            f"    {overlap_entries_fname}",
            sep="\n", file=sys.stderr, flush=True)




## IVR generation
def gen_ivr_records(variants: pd.DataFrame,
                    refseqs: oed.SeriesType[str, SeqType],
                    samples: Collection[str] = None,
                    start: dict[str, int] = None,
                    end: dict[str, int] = None,
                    default_dict: dict = None,
                    ) -> pd.DataFrame:
    """Augmented wrapper of calc_ivrs to generate records for invariant regions
    
    Parameters
    ----------
    variants:  pd.DataFrame
        Contains variants with CHROM, POS, END_POS, ALLELES[list]
    
    refseqs: pd.Series 
        With index as CHROM, values as ref seqs [str, Seq, SeqRecord]
    
    Optional
    --------
    start, end: dict[str, int]
        Dicts to specify only processing subregions, with CHROM as keys, 
        start/end positions as values. 1-indexed, right-open (GFF3 format)
        Default uses whole refseqs.
    default_dict: dict, default VCF_DEFAULT_DICT
        takes default values for ID, QUAL, FILTER, INFO and FORMAT. Defaults:
        - ID: []
        - QUAL: None
        - FILTER: ["PASS"]
        - INFO: []
        - FORMAT: ["GT"] 
        
        Note FORMAT must have "GT"
    
    Returns: pd.DataFrame of ivrs CHROM POS END_POS record
    """

    def _write_calls(record: Record, samples: Collection[str]):
        record.calls = [
            Call(sample, {"GT": 0}, record) for sample in samples]
        return record

    # Set defaults
    start = oed.default(start, {})
    end = oed.default(end, {})
    
    default_dict = VCF_DEFAULT_DICT | oed.default(default_dict, {})

    # calculate invariant region intervals and get sequences
    ivrs = (
        variants
        .groupby("CHROM", as_index=False, group_keys=False)
        .parallel_apply(lambda group: calc_ivrs(
            group,
            refseqs.loc[group.name],
            col_start="POS",
            col_end="END_POS",
            chrom=group.name,
            start=start.get(group.name, 1),
            end=end.get(group.name, None),
            astype=str, 
            ), axis=1)
        )

    # initialize records for ivrs
    ivrs["record"] = ivrs.apply(
        lambda ser: Record(
            ser["CHROM"],
            ser["POS"],
            default_dict["ID"],
            ser["REF"],             # REF
            [],                     # ALT
            default_dict["QUAL"],
            default_dict["FILTER"],
            default_dict["FORMAT"],
            [Call(sample, {"GT": 0}) for sample in samples],  # CALLS
        ), axis=1)

    return ivrs



def calc_ivrs(locs: Union[pd.DataFrame, Collection[tuple[int, int]]],
              refseq: SeqType,
              col_start: str = "POS",
              col_end: str = "END_POS",
              chrom: str = None,
              start: int = 1,
              end: int = None,
              ) -> pd.DataFrame:
    """Calculate intervariant region POS and END_POS

    Loc interval that is 1-indexed, right-open
    
    Parameters
    ------------
    locs:   pd.DataFrame or Collection of 2-tuples
        Variant start and end positions (1-indexed, right-open)
    refseq:  str, Seq, or SeqRecord
        Reference sequence
    col_start: str
        Col name for allele start positions
    col_end: str,
        Col name for allele end positions

    Optional
    --------
    chrom:  name of chromosome, if refseq does not have an id (i.e. is not a Seqrecord)
    astype:  type. Choices: str, Seq, SeqRecord or MultipleSeqAlignment,
        default None is str.
        Cast allele seq as this type. If MultipleSeqAlignment, allele data
        are assigned to column MSA instead of ALLELES

    To calculate for a subregion of refseq, specify:
    -------
    start:   int, default 1
    end:     int, default None (to end of refseq)

    Returns: pd.DataFrame with cols CHROM, POS, END_POS,
        SEQ: str, Seq, SeqRecord or MSA
    """
    
        
    # define vars from args
    if end is None:
        end = len(refseq)
    
    if len(locs) == 0:
        ivrs = pd.DataFrame([(start, end)], columns=[col_start, col_end])

    else:
        # calculate the ivr positions and merge into ranges
        ivrs = oed.setops_ranges(locs, [(start, end)], col_start=col_start,
                                 col_end=col_end, how="right_only")
        
    
    # get allele sequences    
    # shift interval down (both start and end values minus 1) for 0-index
    ivrs = ivrs.assign(
        CHROM=chrom,
        SEQ=ivrs.apply(lambda ser: refseq[ser[col_start] - 1:ser[col_end] - 1],
                       axis=1))
        
    return ivrs





## Allele generation - helpers

# Note: this is not made available
def _combine_ivrs_variants(ivrs: pd.DataFrame,
                           variants: Collection[pd.DataFrame],
                           astype: Annotated[
                               type, SeqType, MultipleSeqAlignment] = str
                           ) -> pd.DataFrame:
    """Post-calc_ivrs() commands common between gen_alleles_from_variants_df
    or from vcf
    
    Includes generation of ALLELES field, drop SEQ and concat
    """
    # assert start is not None, "start required"
    # assert end is not None, "end required"
    
    index_cols = ["CHROM", "POS", "END_POS"]
        
    ivrs = ivrs.assign(ALLELES=(ivrs
                                .assign(REF=ivrs["SEQ"].copy())
                                .apply(seq_astype, axis=1, astype=astype)
                                )).drop("SEQ", axis=1)

    
    for var_df in variants:
        var_df = var_df.assign(
            ALLELES=var_df.apply(
                seq_astype, astype=astype, seq_col="ALLELES", axis=1))
    
    
    alleles = pd.concat([*variants, ivrs]).sort_values(index_cols)
    
    # make as an iterable list
    if not issubclass(astype, MultipleSeqAlignment): 
        alleles["ALLELES"].update(alleles["ALLELES"].apply(lambda seq: [seq]))
        
    return alleles

  
## Allele generationSeqType
#todo: deal with circular alleles
def gen_alleles_from_variants_df(variants: pd.DataFrame,
                                 refseqs: oed.SeriesType[str, SeqType],
                                 start: dict[str, int] = 1,
                                 end: dict[str, int] = None,
                                 strand: Annotated[str, '+', '-'] = None,
                                 astype: Annotated[
                                     type, SeqType, MultipleSeqAlignment
                                     ] = None
                                 ) -> pd.DataFrame:
    """Generate list of all alleles (variant and invariant positions)

    Parameters
    ----------
    variants: pd.DataFrame
        Contains columns for chrom, start pos and end pos
    refseqs: pd.Series 
        With index as CHROM, values as ref seqs [str, Seq, SeqRecord]
    start, end: dict[str, int]
        dict of start and end positions for chromosomes, 1-indexed, right-open
        (GFF3 format). Default processes the entire ref seq
    stranded: str
        + or - strand. Default '+'
    astype:  type.
        Choices: MultipleSeqAlignment, SeqRecord, Seq, str
    """
    if astype is None:
        astype = type(variants["ALLELES"].iloc[0])

    if not issubclass(astype, MultipleSeqAlignment):
        astype = type(variants["ALLELES"].iloc[0][0])

    chrom_groups = variants.groupby("CHROM", as_index=False, group_keys=False)
    
    # apply same start to all chroms
    if isinstance(start, int):
        start = dict((chrom, start) for chrom in chrom_groups.groups.keys())
        
        # apply same end to all chroms
    if isinstance(end, (int, oed.NoneType)):
        end = dict((chrom, end) for chrom in chrom_groups.groups.keys())
        
        
    ivrs = {}
    subset_variants = []
    
    # iter groups to avoid double-run of first entry
    for chrom, group in chrom_groups:
        ivrs[chrom] = calc_ivrs(group,
                                refseqs[chrom],
                                col_start="POS",
                                col_end="END_POS",
                                start=start.get(chrom, 1),
                                end=end.get(chrom, None),
                                chrom=chrom,
                                )
        # todo: change <=/=> end start pos for strandedness
        
        # this includes variants that span across start or across end pos
        subset_variants.append(group.loc[
            (group["END_POS"] > start[chrom]) &  # END_POS is open
            (group["POS"] < end[chrom])
        ])
    
    
    ivrs = pd.concat(ivrs, ignore_index=True)
    
    alleles = _combine_ivrs_variants(ivrs, subset_variants, astype=astype)
    
    return alleles

    
def gen_alleles_for_chrom_vcf(chrom: str,
                              reader: Reader,
                              refseq: SeqType,
                              start: SeqType = None,
                              end: int = None,
                              astype: Annotated[
                                  SeqType, MultipleSeqAlignment] = None
                              ) -> pd.DataFrame:
    """Core function"""
    
    if astype is None:
        astype = type(refseq)

    # set oed.defaults and vars
    index_cols = ["CHROM", "POS", "END_POS"]
    
    chrom = oed.default(chrom, refseq.id)
    
    # to int (or None)
    start = start.get(chrom, 1) if isinstance(start, dict) else start
    end = end.get(chrom, None) if isinstance(end, dict) else end
    
    begin = start - 1
    end = oed.default(end, len(refseq))
    
    variants_vcf = pd.DataFrame.from_records(
        ((
            rec.CHROM,
            rec.POS,
            rec.affected_end + 1,
            [rec.REF, *[alt.value for alt in rec.ALT]]
         ) for rec in reader.fetch(chrom, start, end)
        ), columns=["CHROM", "POS", "END_POS", "ALLELES"]
        ).sort_values(index_cols)

    ivrs = calc_ivrs(variants_vcf, refseq, chrom=chrom, start=start, end=end)
    
    alleles = _combine_ivrs_variants(ivrs, [variants_vcf], astype=astype)

    return alleles




def gen_alleles_from_vcf(vcf: str,
                         refseqs: oed.SeriesType[str, SeqType], 
                         start: dict[str, SeqType],
                         end: dict[str, int] = None,
                         astype: Annotated[
                                     type, SeqType, MultipleSeqAlignment
                                     ] = None) -> pd.DataFrame:
    """Read in variants and get intervariant regions for the relevant region

    Parameters
    ----------
    vcf:    str
    refseqs: pd.Series 
        With index as CHROM, values as ref seqs [str, Seq, SeqRecord]

    Optional:
    start, end: dict[str, int]
        dict of start and end positions for chromosomes, 1-indexed, right-open
        (GFF3 format). Default processes the entire ref seq

    Returns: pd.DataFrame of CHROM: str, POS: int, END_POS: int,
        ALLELES: list[str]
    """

    alleles = []
    
    with Reader.from_path(vcf) as reader:
        chroms = [ctg.id for ctg in reader.header.get_lines("contig")]

        # apply same start to all chroms
        if isinstance(start, int):
            start = dict((chrom, start) for chrom in chroms)       
        
        # apply same end to all chroms
        if isinstance(end, (int, oed.NoneType)):
            end = dict((chrom, end) for chrom in chroms)
        
        for chrom in chroms:
            chrom_alleles = gen_alleles_for_chrom_vcf(
                chrom,
                reader,
                refseqs[chrom],
                start=start.get(chrom, 1),
                end=end.get(chrom, None)
            )
            alleles.append(chrom_alleles)
    
    alleles = pd.concat(alleles, axis=0)
    
    return alleles
    
    

#%%
# def gen_allele_records_from_var_df(variants: DataFrameType[str, int, int],
#                                    refseqs: oed.SeriesType[genomicspy.SeqType],
#                                    ivrs_kws: dict = None,
#                                    ) -> pd.DataFrame:
#     """Generate alleles as vcfpy Record objects
# region
#     ----------
#     variants: pd.DataFrame
#         Contains columns for chrom, start pos and end pos
#     refseqs: pd.Series with index CHROM and values str or Seq or SeqRecord
#     **kws passed to genomicspy.calc_ivrs
#     """


#     ivr_records  = (
#         variants
#         .groupby("CHROM", as_index=False, group_keys=False)
#         .apply(lambda g: genomicspy.calc_ivrs(g, refseqs.loc[g.name], chrom=g.name,
#                                    astype=Seq, **ivrs_kws), axis=1)
#         )

#     variants

#     # update variant records with QUAL

#     EXCLUDE_ANN_FIELDS = [*VCF_COLUMNS, "start", "begin", "end"]
#     def _write_variant_record(variant: pd.Series, _oed.default_dict: dict):
#         """Core function to write variant record"""
#         alleles = variant["ALLELES"]


#         # # if MSA object, try to get annotations and save to INFO
#         if isinstance(alleles, MultipleSeqAlignment):
#             info = dict((k, v) for k, v in alleles.annotations.items()
#                         if k not in EXCLUDE_ANN_FIELDS)
#         else:
#             info = {}

#         info = VCF_DEFAULT_DICT["INFO"] | info

#         # get REF
#         try:
#             ref = str(alleles[0].seq)
#         except AttributeError:
#             ref = alleles[0]


#         # get ALTs into calls
#         for alt in alleles[1:]:


#         Record(
#             variant["CHROM"],
#             variant["POS"],
#             _oed.default_dict["ID"],
#             ref
#             _oed.default_dict["QUAL"],
#             _oed.default_dict["FILTER"],
#             _oed.default_dict["INFO"],
#             # oed.default_dict["FORMAT"],

#         )
#         variant["ALLELES"]


#     variants.apply()


#     # 1-length lists of sequences
#     ivrs["ALLELES"].update(ivrs["ALLELES"].apply(lambda seq: [seq]))

#     # put together variant and invariant entries
#     alleles = pd.concat([variants, ivrs], keys=[True, False], names=["IS_VAR"]
#         ).set_index(["CHROM", "POS", "END_POS"]).sort_index()

#     return alleles



# def construct_alleles_records(variants: pd.DataFrame,
#                               refseqs: pd.Series,
#                               colname: str = "CHROM",
#                               begin: int = 0,
#                               end: int = None,
#                               chrom: str = None,
#                               samples: Iterable[str] = None
#                               ) -> pd.DataFrame:
#     """Construct IVR records with sample calls using variants and refseq"""

#     if chrom is None:
#         chrom = getattr(variants, "name", variants[colname].iloc[0])

#     chrom_range = pd.Series(range(begin, end), name="POS")

#     # todo: calculate ivr (intervals)
#     ivr_intervals = calc_ivr_intervals(variants,
#                                        refseq=refseqs.loc[chrom],
#                                        )
#     ivr_records = ivr_intervals.apply(
#         lambda ser: Record(chrom, ser.POS, [], refseq))

#     record = Record(chrom, pos,
#                     ser.CHROM, ser.POS, [], seq, [], None, ["PASS"], {}, ["GT"])
#     for sample in samples:
#         call = vcfpy.Call(sample, {}, )

#     def _astype_vcf_record(ser: pd.Series):
#         seq = _astype_seq(ser)[0]
#         Record(ser.CHROM, ser.POS, [], seq, [], None, ["PASS"], {}, ["GT"])

# endregion
