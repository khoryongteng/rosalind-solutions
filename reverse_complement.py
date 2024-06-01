# https://rosalind.info/problems/revc/

import argparse

def revc(dna):
    return dna[::-1].translate(str.maketrans('ATCG', 'TAGC'))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('arg', type=str, help='DNA String')
    args = parser.parse_args()
    dna_revc = revc(args.arg)
    print(dna_revc)