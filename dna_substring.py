# https://rosalind.info/problems/subs/

import argparse
    
def find_substring(dna_string, substring):
    return [i + 1 for i in range(len(dna_string)) if dna_string.startswith(substring, i)]
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('arg1', type=str, help='DNA String')
    parser.add_argument('arg2', type=str, help='Substring')
    args = parser.parse_args()
    print(' '.join(map(str, find_substring(args.arg1, args.arg2))))