 #!/usr/bin/env python3
 
 """
 translate_orf.py
 
 This script finds the first open reading frame (ORF) in a nucleotide sequence
 and translates it into the corresponding amino acid sequence.

 Usage:
     python3 translate_orf.py -i <input_file>

 Dependencies:
     - find_orf.py: must contain find_first_orf and parse_sequence_from_path functions
 """

import argparse
from find_orf import find_first_orf, parse_sequence_from_path

def translate_first_orf(sequence,
    start_codons=['AUG'],
    stop_codons=['UAA', 'UAG', 'UGA'],
    genetic_code={
'GUC':'Val','ACC':'Thr','GUA':'Val','GUG':'Val','ACU':'Thr',
'AAC':'Asn','CCU':'Pro','UGG':'Trp','AGC':'Ser','AUC':'Ile',
'CAU':'His','AAU':'Asn','AGU':'Ser','GUU':'Val','CAC':'His',
'ACG':'Thr','CCG':'Pro','CCA':'Pro','ACA':'Thr','CCC':'Pro',
'UGU':'Cys','GGU':'Gly','UCU':'Ser','GCG':'Ala','UGC':'Cys',
'CAG':'Gln','GAU':'Asp','UAU':'Tyr','CGG':'Arg','UCG':'Ser',
'AGG':'Arg','GGG':'Gly','UCC':'Ser','UCA':'Ser','UAA':'Stop',
'GGA':'Gly','UAC':'Tyr','GAC':'Asp','UAG':'Stop','AUA':'Ile',
'GCA':'Ala','CUU':'Leu','GGC':'Gly','AUG':'Met','CUG':'Leu',
'GAG':'Glu','CUC':'Leu','AGA':'Arg','CUA':'Leu','GCC':'Ala',
'AAA':'Lys','AAG':'Lys','CAA':'Gln','UUU':'Phe','CGU':'Arg',
'CGC':'Arg','CGA':'Arg','GCU':'Ala','GAA':'Glu','AUU':'Ile',
'UUG':'Leu','UUA':'Leu','UGA':'Stop','UUC':'Phe'
},
):

"""
Find the first ORF and translate it into an amino acid sequence.
"""

orf = find_first_orf(sequence, start_codons, stop_codons)

if not orf:
    return None

amino_acids = []

for i in range(0, len(orf), 3):
    codon = orf[i:i+3]

    if len(codon) < 3:
        break

    aa = genetic_code.get(codon, "Unknown")

    if aa == "Stop":
        break

    amino_acids.append(aa)

return amino_acids
