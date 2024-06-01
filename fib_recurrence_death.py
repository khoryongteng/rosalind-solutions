# https://rosalind.info/problems/fibd/

import argparse

def fib(n_months, m_max_age=1):
    ages = [1] + [0]*(m_max_age - 1)
    for i in range(n_months - 1):
        ages = [sum(ages[1:])] + ages[:-1]
    return sum(ages)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('arg1', type=int, help='n_months')
    parser.add_argument('arg2', type=int, help='m_max_age')
    args = parser.parse_args()
    print(fib(args.arg1, args.arg2))