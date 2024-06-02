# https://rosalind.info/problems/lcsm/

import argparse
from Bio import SeqIO

def fasta_to_sequences(fasta_file):
    sequences = []
    with open(fasta_file, 'r') as handle:
        for record in SeqIO.parse(handle, 'fasta'):
            sequences.append(str(record.seq))
    return sequences            

# Naive Method
def lcsm(seqs):
    # Starting from shortest string
    shortest = min(seqs, key=len)
    # Iterate Through substrings of shortest sequence
    for length in range(len(shortest), 0, -1):
        for start in range(len(shortest) - length + 1):
            sub = shortest[start:start+length]
            # Look for longest substring possible that is in all sequences
            if all(seq.find(sub) >= 0 for seq in seqs):
                return sub
    return ""

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('arg', type=str, help='FASTA File')
    args = parser.parse_args()
    seqs = fasta_to_sequences(args.arg)
    print(lcsm(seqs))