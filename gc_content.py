# https://rosalind.info/problems/gc/

import argparse
import sys
import re

# Too lazy to make efficient :)

def calculate_gc_content(dna_string):
    gc_count = dna_string.count('G') + dna_string.count('C')
    total_length = len(dna_string)
    return gc_count / total_length * 100

def get_highest_gc(filepath):
    try:
        result_dict = {}
        with open(filepath, 'r') as file:
            content = file.read()
            matches = re.findall(r'^>(\S+)\n([^>]+)', content, re.MULTILINE)
            for match in matches:
                sequence_id, dna_string = match
                dna_string = re.sub(r'\s+', '', dna_string)
                result_dict[sequence_id] = calculate_gc_content(dna_string)
        max_id = max(result_dict, key=lambda k: result_dict[k])
        return(max_id, result_dict[max_id])
    except FileNotFoundError:
        print("File not found!")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('arg', type=str, help='File Path')
    args = parser.parse_args()
    sequence_id, gc_content = get_highest_gc(args.arg)
    print(sequence_id)
    print(gc_content)
    