"""Generate N triangular numbers with in range [l, r]"""

import argparse
import random

from utility import generate_random_tn, save_triangular_numbers, timing


def init_parser() -> "argparse.ArgumentParser":
    parser = argparse.ArgumentParser(
        prog='GenerateTriangularNumbers',
        description='Generate N triangular numbers with values in range [l, r]. Difference between l and r must be at lest 2 units')
    parser.add_argument('-file', '-f', nargs='?', type=str, default="stdout", help='Name of file where the TN are saved to, otherwise written to stdout')
    parser.add_argument('-amount', '-a', nargs='?', type=int, default=2, help='Amount of TriangularNumbers to generate (default=2)')
    parser.add_argument('-left', '-l', nargs='?', type=int, default=1, help='Left range limit of TN values (inclusive) (default=1)')
    parser.add_argument('-right', '-r', nargs='?', type=int, default=10, help='Right range limit of TN values (inclusive) (default=10)')
    parser.add_argument('-seed', '-s', nargs='?', type=int, default=-1, help='Seed for random functions (default=random)')
    parser.add_argument('-use_float', '-uf', nargs='?', type=bool, default=False, help='Generate TN with int or float values')
    return parser

def parse_arguments(parser: "argparse.ArgumentParser") -> tuple[str, int, int, int, int, bool]:
    ns = parser.parse_args() # ["-f=stdout", "-a=3", "-l=1", "-r=3"] for testing
    file_name, amount, left, right, seed, use_float = ns.file, ns.amount, ns.left, ns.right, ns.seed, ns.use_float
    return file_name, amount, left, right, seed, use_float

def validate_arguments(left, right, seed):
    if abs(left - right) < 2:
        right += 2 - abs(left - right)
    if seed != -1:
        random.seed(seed)
    return left, right

def main():
    parser = init_parser()
    file, amount, left, right, seed, use_float = parse_arguments(parser)
    left, right = validate_arguments(left, right, seed)
    triangular_numbers = [generate_random_tn(left, right, use_float=use_float) for _ in range(amount)]
    save_triangular_numbers(triangular_numbers, file)

if __name__ == "__main__":
    main()

# python .\tn_generate.py -f .\data\triangular_numbers_a100_l1_r100.txt -a 100 -l 1 -r 100 -s 0123456789
# python .\tn_generate.py -f .\data\triangular_numbers_a1000_l1_r100.txt -a 1000 -l 1 -r 100 -s 0123456789
# python .\tn_generate.py -f .\data\triangular_numbers_a100_l1_r1000.txt -a 100 -l 1 -r 1000 -s 0123456789
# python .\tn_generate.py -f .\data\triangular_numbers_a1000_l1_r1000.txt -a 1000 -l 1 -r 1000 -s 0123456789

# python .\tn_generate.py -f .\data\triangular_numbers_f_a100_l1_r100.txt -a 100 -l 1 -r 100 -s 0123456789 -uf True
# python .\tn_generate.py -f .\data\triangular_numbers_f_a1000_l1_r100.txt -a 1000 -l 1 -r 100 -s 0123456789 -uf True
# python .\tn_generate.py -f .\data\triangular_numbers_f_a100_l1_r1000.txt -a 100 -l 1 -r 1000 -s 0123456789 -uf True
# python .\tn_generate.py -f .\data\triangular_numbers_f_a1000_l1_r1000.txt -a 1000 -l 1 -r 1000 -s 0123456789 -uf True
