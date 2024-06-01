# https://rosalind.info/problems/fib/

import argparse

fib = {0: 0, 1: 1, 2: 1}

def total_pairs(n_months, k_pairs):
    if n_months in fib:
        return fib[n_months]
    fib[n_months] = total_pairs(n_months - 1, k_pairs) + total_pairs(n_months - 2, k_pairs) * k_pairs
    return fib[n_months]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('arg1', type=int, help='n')
    parser.add_argument('arg2', type=int, help='k')
    args = parser.parse_args()
    print(total_pairs(args.arg1, args.arg2))