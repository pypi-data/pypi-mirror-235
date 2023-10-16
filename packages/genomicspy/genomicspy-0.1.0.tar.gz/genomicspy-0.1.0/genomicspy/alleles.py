# alleles.py
from __future__ import annotations
import os
import sys
from collections.abc import Mapping
from typing import Union

import pandas as pd

import oddsnends as oed


__all__ = [
    "check_overlap",
]

def check_overlap(group: pd.DataFrame,
                  start_col: str,
                  end_col: str,
                  lengths_lookup: Union[Mapping[str, int],
                                        oed.SeriesType[str, int]] = None,
                  length: int = None,
                  is_circular: bool = False,
                  errout: str = ".",
                  chrom: str = None,
                  ) -> None:
    #TODO need to make more efficient
    """Check if intervals of entries overlap.

    Intervals are right-open and 1-indexed.

    Parameters
    ------------
        df: pd.DataFrame
        start_col:  str   Col name of interval start index
        end_col:    str   Col name of interval end index
        lengths_lookup: Mapping or pd.Series
            With index or keys as CHROM, and values as int

    Optional:
        length:      int  Total contig length. Required if is_circular is True
        is_circular: bool Treat entries on circular contig. Default False
        errout:      str  Output directory for error files. Default "."
        chrom:        str  Name for error files. Default name of df (if group)
                          or None

    Returns:  None
    """

    def _circ_pos(_pos: pd.Series, _length: int):
        """Calculate real positions on circle as 1-indexed"""
        return (_pos % _length).mask(lambda ser: ser == 0, _length)


    chrom = oed.default(chrom, group.name[0])

    if is_circular:

        length = oed.default(length, lengths_lookup[chrom])
        assert length is not None, "length is None"


    # get interval start and end columns
    entries = group[[start_col, end_col]]

    # group entries for each position and count
    # resulting df has index as pos, values as ids from entries index and n_ids
    # TODO: Speed this up!!
    positions = (
        entries
        .parallel_apply(
            lambda ser: list(range(ser[start_col], ser[end_col])), axis=1)
        .explode(ignore_index=False)
    )

    if is_circular:

        # calculate real position on a circular chromosome
        positions = _circ_pos(positions, length)

        # make same pos val as dot for easier reading
        entries[f"{end_col}_circ"] = _circ_pos(entries[end_col], length).mask(
            lambda ser: entries[end_col] <= ser, ".")

    positions = (positions.to_frame("pos")
                 .groupby("pos")
                 .parallel_apply(lambda g: g.index)
                 .to_frame("ids")
                 .assign(n_ids=lambda df: df["ids"].parallel_apply(len))
                 )

    try:
        # check if there are overlaps
        overlaps = positions.loc[positions.n_ids > 1]
        assert len(overlaps) == 0, "Overlapping entries exist."

    except AssertionError:

        # ranges of overlap
        overlap_ranges = oed.calc_intervals(overlaps.index)

        # ids corresponding to entries index
        overlap_ids = overlaps["ids"].explode().drop_duplicates()

        overlap_entries = entries.loc[overlap_ids, :]

        suffix = oed.default(chrom, "", has_value=f".{chrom}")

        # save entries for review
        positions_check_fname = f"positions_check{suffix}.tsv"
        positions.to_csv(f"{errout}/{positions_check_fname}", sep="\t")

        overlap_entries_fname = f"overlapping_variants{suffix}.tsv"
        overlap_entries.to_csv(f"{errout}/{overlap_entries_fname}", sep="\t")

        print(
            ">> OVERLAPS",
            f">> {len(overlap_ranges)} intervals span ""{len(overlaps)} pos:",
            *(f"{chrom}:{i}-{j}" for i, j in overlap_ranges),
            f">> {len(overlap_entries)} overlapping entries:",
            overlap_entries.to_string(),
            ">> Checks and ranges saved to:",
            f"- {positions_check_fname} and ",
            f"- {overlap_entries_fname}",
            sep="\n", file=sys.stderr, flush=True)

