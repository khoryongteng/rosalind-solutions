# https://rosalind.info/problems/cons/

import argparse
import sys
import re
from Bio import motifs
from Bio.Seq import Seq

def get_seq_array(filepath):
    try:
        with open(filepath, 'r') as file:
            content = file.read()
            matches = re.findall(r'^>(\S+)\n([^>]+)', content, re.MULTILINE)
            seq_array = []
            for match in matches:
                _, dna_string = match
                seq_array.append(Seq(dna_string.replace('\n', '')))
            return seq_array
    except FileNotFoundError:
        print("File not found!")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('arg', type=str, help='File Path')
    args = parser.parse_args()
    seq_array = get_seq_array(args.arg)
    seq_motifs = motifs.create(seq_array)
    # Consensus
    print(seq_motifs.consensus)
    # Profile
    for base, counts in seq_motifs.counts.items():
        counts = [int(count) for count in counts]
        print(f"{base}: {' '.join(map(str, counts))}")
        
    # print(seq_motifs.counts)
