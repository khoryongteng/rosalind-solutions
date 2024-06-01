# https://rosalind.info/problems/iprb/

import argparse

def dominant_factor_probability(k, m, n):
    # Less combinations result in only recessive genes. doing 1 - p(recessive genes) to get results
    num_pop = k + m + n
    p_mm_recessive = (m / num_pop) * ((m - 1) / (num_pop - 1)) * 1/4
    p_mn_recessive = (m / num_pop) * (n / (num_pop - 1)) * 1/2
    p_nm_recessive = (n / num_pop) * (m / (num_pop - 1)) * 1/2
    p_nn_recessive = (n / num_pop) * ((n - 1) / (num_pop - 1))
    return 1 - (p_mm_recessive + p_mn_recessive + p_nm_recessive + p_nn_recessive)
    # simplified solution: 
    # N = float(k+m+n)
    # return(1 - 1/N/(N-1)*(n*(n-1) + n*m + m*(m-1)/4.))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('arg1', type=int, help='k')
    parser.add_argument('arg2', type=int, help='m')
    parser.add_argument('arg3', type=int, help='n')
    args = parser.parse_args()
    print(dominant_factor_probability(args.arg1, args.arg2, args.arg3))