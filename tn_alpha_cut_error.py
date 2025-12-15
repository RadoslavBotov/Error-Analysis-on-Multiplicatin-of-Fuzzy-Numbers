import argparse
from tqdm.contrib import itertools
import numpy as np

from alg.triangular_number import TriangularNumber
from alg.utility import load_triangular_numbers, timing


def init_parser() -> "argparse.ArgumentParser":
    parser = argparse.ArgumentParser(
        prog='AlphaCutErrorTriangularNumbers',
        description='Load TriangularNumbers from file and calculate alpha cut left/right error with given precision')
    parser.add_argument('-file', '-f', type=str, help='Name of file where the TN are read from')
    parser.add_argument('-precision', '-p', nargs='?', type=int, default=10, help='Precision with which error is calculated. (default=10)')
    return parser

def parse_arguments(parser: "argparse.ArgumentParser") -> tuple[str, int]:
    namespace = parser.parse_args() # ["-file=data\\triangular_numbers_a100_l1_r100.txt"]
    file_name, precision = namespace.file, namespace.precision
    return file_name, precision

def validate_arguments(precision: int) -> int:
    if precision < 10:
        precision = 100
    return precision

def calculate_alpha_cut_diff(tn_naive: "TriangularNumber", tn_alpha_cut: "TriangularNumber", precision: float):
    alpha_points = np.linspace(0, 1, precision)
    
    tn_naive_left_points = list(map(tn_naive.alpha_cut_left, alpha_points))
    tn_naive_right_points = list(map(tn_naive.alpha_cut_right, alpha_points))
    tn_alpha_cut_left_points = list(map(tn_alpha_cut.alpha_cut_left, alpha_points))
    tn_alpha_cut_right_points = list(map(tn_alpha_cut.alpha_cut_right, alpha_points))
    
    return tn_alpha_cut_left_points, tn_alpha_cut_right_points, tn_naive_left_points, tn_naive_right_points

def number_similarity(alpha, naive):
    return np.minimum(alpha, naive) / np.maximum(alpha, naive) # = 1 - abs(alpha - naive) / alpha
    # return  abs(alpha - naive) / alpha

def calculate_left_right_error(tn_alpha_cut_left_points, tn_alpha_cut_right_points, tn_naive_left_points, tn_naive_right_points):
    error_left = number_similarity(tn_alpha_cut_left_points, tn_naive_left_points)
    error_right = number_similarity(tn_alpha_cut_right_points, tn_naive_right_points)
    return error_left, error_right

def calculate_average_error(triangular_numbers: list["TriangularNumber"], precision: int):
    err_l_all = []
    err_r_all = []

    for tn1, tn2 in itertools.product(triangular_numbers, triangular_numbers):
        tn_naive = tn1.mul_naive(tn2)
        tn_alpha = tn1.mul_alpha_cut(tn2)
        # tn_alpha = tn1.mul_standard_approx(tn2)
        # naive == standard approximation; they are the same

        tn_a_l, tn_a_r, tn_n_l, tn_n_r = calculate_alpha_cut_diff(tn_naive, tn_alpha, precision+1)
        err_l, err_r = calculate_left_right_error(tn_n_l, tn_n_r, tn_a_l, tn_a_r)

        err_l_all.extend(err_l[1:-1])
        err_r_all.extend(err_r[1:-1])
    
    return err_l_all, err_r_all

@timing
def main():
    # np.set_printoptions(linewidth=150, suppress=True)
    parser = init_parser()
    file_name, precision = parse_arguments(parser)

    triangular_numbers = load_triangular_numbers(file_name)
    err_l_all, err_r_all = calculate_average_error(triangular_numbers, precision)

    print("Precision:", precision)
    print("Left error:", np.average(err_l_all))
    print("Right error:", np.average(err_r_all))


if __name__ == "__main__":
    main()

# python .\tn_alpha_cut_error.py -file data\\triangular_numbers_100_1_100.txt
# python .\tn_alpha_cut_error.py -file data\\triangular_numbers_100_1_100.txt -precision 100
# python .\tn_alpha_cut_error.py -file data\\triangular_numbers_1000_1_100.txt
# python .\tn_alpha_cut_error.py -file data\\triangular_numbers_1000_1_100.txt -precision 100
# python .\tn_alpha_cut_error.py -file data\\triangular_numbers_100_1_1000.txt
# python .\tn_alpha_cut_error.py -file data\\triangular_numbers_100_1_1000.txt -precision 100
# python .\tn_alpha_cut_error.py -file data\\triangular_numbers_1000_1_1000.txt
# python .\tn_alpha_cut_error.py -file data\\triangular_numbers_1000_1_1000.txt -precision 100
