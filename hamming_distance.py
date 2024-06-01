# https://rosalind.info/problems/hamm/

import argparse


def hamming_distance(seq_a, seq_b):
    distance = 0
    for a_nucleotide, b_nucleotide in zip(seq_a, seq_b):
        if a_nucleotide != b_nucleotide:
            distance += 1
    return distance

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('arg1', type=str, help='Sequence A')
    parser.add_argument('arg2', type=str, help='Sequence B')
    args = parser.parse_args()
    print(hamming_distance(args.arg1, args.arg2))