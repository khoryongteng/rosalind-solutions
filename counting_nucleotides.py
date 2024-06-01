# https://rosalind.info/problems/dna/

import argparse

def count_nucleotides(dna_string):
    nucleotide_counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for char in dna_string:
        if char in nucleotide_counts:
            nucleotide_counts[char] += 1
    return nucleotide_counts

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('arg', type=str, help='DNA String')
    args = parser.parse_args()
    count = count_nucleotides(args.arg)
    print(*count.values())