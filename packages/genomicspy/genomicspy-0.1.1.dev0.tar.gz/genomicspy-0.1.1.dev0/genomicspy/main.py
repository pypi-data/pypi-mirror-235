"""Main module."""
# alleles.py
from __future__ import annotations
import logging
from collections.abc import Hashable
from typing import Annotated, Union

import pandas as pd
from Bio.AlignIO import MultipleSeqAlignment
from Bio.Seq import MutableSeq, Seq
from Bio.SeqIO import SeqRecord

import oddsnends as oed

__all__ = [
    "SeqType",
    "copy_multipleseqalignment",
    "copy_seqrecord",
    "seq_astype",
]

SeqType = Union[str, Seq, MutableSeq, SeqRecord]




def copy_seqrecord(rec: SeqRecord, append: bool = True, **kws):
    """Makes a copy of SeqRecord, overriding any kwargs with **kws
    
    append: applies to dbxrefs, features, annotations, and letter_annotations
    """
    
    # defaults
    features = rec.features
    dbxrefs = rec.dbxrefs
    annotations = rec.annotations
    letter_annotations = rec.letter_annotations
    
    # set defaults
    if append:
        features += kws.pop("features", [])
        dbxrefs += kws.pop("dbxrefs", [])
        annotations |= kws.pop("annotations", {})
        letter_annotations |= kws.pop("letter_annotations", {})
    
    
    kws = {"seq": rec.seq,
           "name": rec.name,
           "id": rec.id,
           "description": rec.description,
           "dbxrefs": dbxrefs,
           "features": features,
           "annotations": annotations,
           "letter_annotations": letter_annotations,
           } | kws
    return SeqRecord(**kws)


def copy_multipleseqalignment(msa: MultipleSeqAlignment, append: bool = True,
                              **kws):
    """Makes a copy of MultipleSeqAlignment, overriding with any **kws
    
    append applies to records, annotations and column_annotations
    """
    # defaults
    
    records =  [copy_seqrecord(rec) for rec in msa]
    annotations = msa.annotations
    column_annotations = msa.column_annotations
    
    if append:
        records += kws.pop("records", [])
        annotations |= kws.pop("annotations", {})
        column_annotations |= kws.pop("column_annotations", {})
    
    # set defaultsSeqType
    kws = {"records": records,
           "annotations": annotations,
           "column_annotations": column_annotations,
          } | kws
    return MultipleSeqAlignment(**kws)
    
    

def seq_astype(ser: pd.Series,
               astype: Annotated[type, SeqType, MultipleSeqAlignment],
               seq_col: Hashable = "SEQ",
               inplace: bool = False,
               msa_kws: dict = None,
               rec_kws: dict = None,
               mutable: bool = False,
               ) -> Union[SeqType, MultipleSeqAlignment]:
    """ser with SEQ, REF, CHROM, POS
    
    **<msa,erc> kws passed to update or construct the (new) MSA or SeqRec
    """
    
    seq_obj = ser[seq_col]
    
    
    # for making brand new records (not copy)
    seqid = f"{ser.CHROM}|{ser.POS}|0"
    anns = {"CHROM": ser.CHROM, "POS": ser.POS, "END_POS": ser.END_POS}
    
    msa_kws = oed.defaults(msa_kws, {})
    rec_kws = oed.defaults(rec_kws, {})
    
    # return an MSA
    if issubclass(astype, MultipleSeqAlignment):
        
        # check input type            
        if isinstance(seq_obj, MultipleSeqAlignment):
            return copy_multipleseqalignment(seq_obj, **msa_kws) \
                if not inplace else seq_obj
                
        match seq_obj:
            case SeqRecord():
                rec = copy_seqrecord(seq_obj, **rec_kws) if not inplace else seq_obj
                
            case MutableSeq():
                rec = SeqRecord(
                    MutableSeq(seq_obj) if not inplace else seq_obj, id=seqid)
            
            case Seq():
                rec = SeqRecord(Seq(seq_obj) if not inplace else seq_obj, id=seqid)
                
            case _:
                rec = SeqRecord(Seq(f"{seq_obj}"), id=seqid)
        
        return MultipleSeqAlignment([rec], **({"annotations": anns} | msa_kws))
        
    # this comes after checking if output is MSA
    if isinstance(seq_obj, MultipleSeqAlignment) and len(seq_obj) > 1:
        logging.warning("More than one seq in MSA. Using first seq")

    # return as SeqRecord
    if issubclass(astype, SeqRecord):
        
        # check input type
        match seq_obj:
            case MultipleSeqAlignment():
                return copy_seqrecord(seq_obj[0], **rec_kws) if not inplace \
                    else seq_obj[0]
            
            case SeqRecord():
                return copy_seqrecord(seq_obj, **rec_kws) if not inplace \
                    else seq_obj
        
        # construct/get seq first, then make new record
        match seq_obj:    
            case MutableSeq():
                seq = MutableSeq(seq_obj) if not inplace else seq_obj
                
            case Seq():
                seq = Seq(seq_obj) if not inplace else seq_obj
            
            case _:
                seq = Seq(f"{seq_obj}")
                
        return SeqRecord(seq, **(dict(id=seqid, annotations=anns) | rec_kws))


    # return as Seq
    if issubclass(astype, MutableSeq):
        
        # get seq and then copy/cast as MutableSeq
        match seq_obj:
            case MultipleSeqAlignment():
                seq = seq_obj[0].seq  # str or Seq from first record
            
            case SeqRecord():
                seq = seq_obj.seq
            
            case _:  # str, MutableSeq or Seq
                seq = seq_obj
            
        if inplace and isinstance(seq, MutableSeq):
            return seq
        else:
            return MutableSeq(f"{seq}")
    
    # return as Seq
    if issubclass(astype, Seq):
        
        match seq_obj:
            case MultipleSeqAlignment():
                seq = seq_obj[0].seq  # str or Seq from first record
            
            case SeqRecord():
                seq = seq_obj.seq
            
            case _:  # str, MutableSeq or Seq
                seq = seq_obj
            
        return Seq(f"{seq}") if isinstance(seq, str) or not inplace else seq
    
    # return as str
    if issubclass(astype, str):
        
        match seq_obj:
            case MultipleSeqAlignment():
                seq = seq_obj[0].seq  # str or Seq from first record
            
            case SeqRecord():
                seq = seq_obj.seq
            
            case _:  # str or Seq
                seq = seq_obj

        return seq

    else:
        raise ValueError("Bad astype arg", astype)
