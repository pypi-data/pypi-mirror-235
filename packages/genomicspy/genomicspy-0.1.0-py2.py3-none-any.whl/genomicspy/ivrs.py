# ivrs.py

# Methods to calculate intravariant regions
#%%
# Vivian Leung
# 13 Oct 2023
from __future__ import annotations
from collections.abc import Collection
from typing import Annotated, Union

import pandas as pd
import vcfpy
from Bio.AlignIO import MultipleSeqAlignment
from Bio.Seq import Seq
from Bio.SeqIO import SeqRecord

import oddsnends as oed
from oddsnends import SeriesType


RefSeqType = Union[str, Seq, SeqRecord]
SampleErrorHandlingType = Annotated[str, "ignore", "force", "raise" ]

#%%

__all__ = [
    "calc_ivrs",
    "gen_ivr_records", 
]

VCF_DEFAULT_DICT = {"ID": [],
                    "QUAL": None,
                    "FILTER": ["PASS"],
                    "INFO": {},
                    "FORMAT": ["GT"],
                    }



def gen_ivr_records(variants: pd.DataFrame,
                    refseqs: SeriesType[str, RefSeqType],
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

    def _write_calls(record: vcfpy.Record, samples: Collection[str]):
        record.calls = [
            vcfpy.Call(sample, {"GT": 0}, record) for sample in samples]
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
        lambda ser: vcfpy.Record(
            ser["CHROM"],
            ser["POS"],
            default_dict["ID"],
            ser["REF"],             # REF
            [],                     # ALT
            default_dict["QUAL"],
            default_dict["FILTER"],
            {"END_POS": ser.END_POS},
            default_dict["FORMAT"],
            [vcfpy.Call(sample, {"GT": 0}) for sample in samples],  # CALLS
            ), axis=1)

    return ivrs



def calc_ivrs(locs: Union[pd.DataFrame, Collection[tuple[int, int]]],
              refseq: RefSeqType,
              col_start: str = "POS",
              col_end: str = "END_POS",
              chrom: str = None,
              start: int = 1,
              end: int = None,
              astype: Annotated[type, str, Seq, MultipleSeqAlignment] = str
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
        REF: str, Seq, SeqRecord or MSA
    """
    def _astype_msa(ser: pd.Series) -> MultipleSeqAlignment:
        """Core function for converting output to MSA"""

        new_record = SeqRecord(getattr(ser.REF, "seq", Seq(ser.REF)),
                               id=f"{ser.CHROM}|{ser.POS}|0")

        anns = {"CHROM": ser.CHROM, "POS": ser.POS, "END_POS": ser.END_POS}

        return MultipleSeqAlignment([new_record], annotations=anns)

    def _astype_seqrecord(ser: pd.Series) -> list[Seq]:
        if isinstance(ser.REF, SeqRecord):
            return ser.REF

        return SeqRecord(getattr(ser.REF, "seq", Seq(ser.REF)),
                         id=f"{ser.CHROM}|{ser.POS}|0")

    def _astype_seq(ser: pd.Series) -> list[Seq]:
        """Core function for converting output to Seq"""
        if isinstance(ser.REF, SeqRecord):
            return ser.REF.seq
        return Seq(ser.REF)

    def _astype_str(ser: pd.Series) -> list[str]:
        """Core function for converting output to str"""
        if isinstance(ser.REF, SeqRecord):
            return str(ser.REF.seq)
        return str(ser.REF)


    # define vars from args
    begin = start - 1

    if end is None:
        end = len(refseq)

    if chrom is None:
        try:
            chrom = refseq.id
        except AttributeError as err:
            raise ValueError(
                f"No chrom name given for refseq of type {refseq}") from err


    match astype:
        case MultipleSeqAlignment():
            astype_func = _astype_msa
        case SeqRecord():
            astype_func = _astype_seqrecord
        case Seq():
            astype_func = _astype_seq
        case _:
            astype_func = _astype_str


    # calculate the ivr positions and merge into ranges
    ivrs = oed.set_ranges(locs, [(begin, end)], col_start="POS",
                          col_end="END_POS", how="right_only")
    
    # if not isinstance(locs, pd.DataFrame):
    #     locs = pd.DataFrame(locs, columns=[col_start, col_end])
    #
    # ivrs = (locs
    #         .apply(lambda ser: range(ser[col_start] - 1, ser[col_end]), axis=1)
    #         .explode()
    #         .drop_duplicates()
    #         .dropna()
    #         .rename("pos")
    #         .pipe(pd.merge,
    #             right=pd.Series(range(begin, end), name="pos"),
    #             how="outer",
    #             indicator=True)
    #         .pipe(lambda df: df.loc[df["_merge"] == "right_only", "pos"])
    #         .pipe(lambda ser: pd.DataFrame(
    #             calc_intervals(ser), columns=["POS", "END_POS"]))
    # )

    ivrs["CHROM"] = chrom

    # get allele sequences
    ivrs["REF"] = ivrs.apply(
        lambda ser: refseq[ser[col_start] - 1:ser[col_end]], axis=1)

    # format sequences as output type
    ivrs["REF"] = ivrs.apply(astype_func, axis=1)

    return ivrs


# %%
