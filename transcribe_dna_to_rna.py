# https://rosalind.info/problems/rna/

import argparse

def transcribe(dna):
    return dna.replace('T', 'U')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('arg', type=str, help='DNA String')
    args = parser.parse_args()
    rna = transcribe(args.arg)
    print(rna)