import argparse
import multiprocessing

import numpy as np
import tqdm

from alg.triangular_number import TriangularNumber
from alg.utility import cosine_similarity, load_triangular_numbers, min_max_similarity, minkowski_distance, timing


def init_parser() -> "argparse.ArgumentParser":
    parser = argparse.ArgumentParser(
        prog='MinkowskiDistanceTriangularNumbers',
        description='Load TriangularNumbers from file and calculate MinkowskiDistance with given w and precision')
    parser.add_argument('-file', '-f', type=str, help='Name of file where the TN are read from')
    parser.add_argument('-precision', '-p', nargs='?', type=int, default=10, help='Precision with which error is calculated. (default=10)')
    parser.add_argument('-step', '-s', nargs='?', type=float, default=0.1, help='Precision with which error is calculated. (default=10)')
    return parser

def parse_arguments(parser: "argparse.ArgumentParser") -> tuple[str, int, float]:
    namespace = parser.parse_args() # ["-file=data\\triangular_numbers_a100_l1_r100.txt"]
    file_name, precision, step = namespace.file, namespace.precision, namespace.step
    return file_name, precision, step

def validate_arguments(precision: int) -> tuple[int]:
    if (precision < 10):
        precision = 10
    return precision

def format_filename(file_name: str) -> str:
    l = ["".join(t for t in token if (t.isnumeric() is True)) for token in file_name.split('_')]
    amount = int(l[2])
    left = int(l[3])
    right = int(l[4])
    return f"{amount=}, {left=}, {right=}"

def calculate_multiplications(tn1: TriangularNumber, tn2: TriangularNumber, precision: int, step: float = 0.1):
    # calc different mul methods
    tn_n = tn1.mul_naive(tn2)
    tn_a = tn1.mul_alpha_cut(tn2)
    tn_s = tn1.mul_standard_approx(tn2)
    tn_e = tn1.mul_extension(tn2, step) # step = 1 VERY ROUGH | 0.1 ROUGH | 0.01 FINE | 0.001 VERY FINE
    # calc a x_range for all methods with precision samples; its the same each time
    x_range = np.linspace(tn_n.a1, tn_n.a3, precision)
    # calc the corresponding y_range
    y_range_tn_n = [float(tn_n.membership(x)) for x in x_range]
    y_range_tn_a = [float(tn_a.membership(x)) for x in x_range]
    y_range_tn_s = [float(tn_s.membership(x)) for x in x_range]
    y_range_tn_e = [float(tn_e.membership(x)) for x in x_range]
    return y_range_tn_n, y_range_tn_a, y_range_tn_s, y_range_tn_e

def calculate_distances(y_range_tn1: TriangularNumber, y_range_tn2: TriangularNumber) -> tuple[float, float, float, float]:
    err_md = minkowski_distance(y_range_tn1, y_range_tn2, w=1)
    err_ed = minkowski_distance(y_range_tn1, y_range_tn2, w=2)
    err_cs = cosine_similarity(y_range_tn1, y_range_tn2)
    err_mm = min_max_similarity(y_range_tn1, y_range_tn2)
    return err_md, err_ed, err_cs, err_mm

def calculate_distance_errors(triangular_numbers: list[tuple[TriangularNumber, TriangularNumber]], precision: int, step: float):
    pool = multiprocessing.Pool()
    
    # calculate all different multiplication methods for each pair of TN
    # list[([naive, ...], [alpha_cut, ...], [standard_approximation, ...], [extension_principle, ...]), ...]
    multiplication_results = [
        pool.apply_async(func=calculate_multiplications, args=(tn1, tn2, precision, step))
        for tn1, tn2 in triangular_numbers
    ]
    multiplication_results = [mr.get() for mr in tqdm.tqdm(multiplication_results)]
    
    # Alpha-cut and Naive
    distance_results = [
        pool.apply_async(func=calculate_distances, args=(y_a, y_n))
        for y_n, y_a, _, _ in multiplication_results
    ]
    distance_results = [dr.get() for dr in tqdm.tqdm(distance_results)]
    err1, err2, err3, err4 = zip(*distance_results)

    # Alpha-cut and Standard Approximation
    distance_results = [
        pool.apply_async(func=calculate_distances, args=(y_a, y_s))
        for _, y_a, y_s, _ in multiplication_results
    ]
    distance_results = [dr.get() for dr in tqdm.tqdm(distance_results)]
    err5, err6, err7, err8 = zip(*distance_results)

    # Alpha-cut and Extension Principle
    distance_results = [
        pool.apply_async(func=calculate_distances, args=(y_a, y_e))
        for _, y_a, _, y_e in multiplication_results
    ]
    distance_results = [dr.get() for dr in tqdm.tqdm(distance_results)]
    err9, err10, err11, err12 = zip(*distance_results)
    
    pool.close()
    pool.join()
    
    return [
        [np.average(err1), np.average(err2), np.average(err3), np.average(err4)],
        [np.average(err5), np.average(err6), np.average(err7), np.average(err8)],
        [np.average(err9), np.average(err10), np.average(err11), np.average(err12)]
    ]

@timing
def main():
    # np.set_printoptions(linewidth=150, suppress=True)
    parser = init_parser()
    file_name, precision, step = parse_arguments(parser)
    precision = validate_arguments(precision)

    triangular_numbers = load_triangular_numbers(file_name)
    # triangular_numbers = list(itertools.product(triangular_numbers, triangular_numbers))
    triangular_numbers = [
        (triangular_numbers[i], triangular_numbers[j])
        for i in range(len(triangular_numbers))
        for j in range(len(triangular_numbers))
        if i != j
    ]
    res = calculate_distance_errors(triangular_numbers, precision, step)
    
    print(f"{format_filename(file_name)}, {precision=}, {step=}")
    print( "                       | Manhattan distance | Euclidean distance | Cosine similarity | Min-Max similarity")
    print( "-----------------------+--------------------+--------------------+-------------------+-------------------")
    print(f"Naive                  | {res[0][0]:18.10f} | {res[0][1]:18.10f} | {res[0][2]:17.6%} | {res[0][3]:18.6%}")
    print(f"Standard approximation | {res[1][0]:18.10f} | {res[1][1]:18.10f} | {res[1][2]:17.6%} | {res[1][3]:18.6%}")
    print(f"Extension principle    | {res[2][0]:18.10f} | {res[2][1]:18.10f} | {res[2][2]:17.6%} | {res[2][3]:18.6%}")

if __name__ == "__main__":
    main()
    print()

# python .\tn_distance.py -file data\\triangular_numbers_100_1_100.txt -s 1
# python .\tn_distance.py -file data\\triangular_numbers_100_1_100.txt -precision 100 -s 1
# python .\tn_distance.py -file data\\triangular_numbers_1000_1_100.txt -s 1
# python .\tn_distance.py -file data\\triangular_numbers_1000_1_100.txt -precision 100 -s 1
# python .\tn_distance.py -file data\\triangular_numbers_100_1_1000.txt -s 1
# python .\tn_distance.py -file data\\triangular_numbers_100_1_1000.txt -precision 100 -s 1
# python .\tn_distance.py -file data\\triangular_numbers_1000_1_1000.txt -s 1
# python .\tn_distance.py -file data\\triangular_numbers_1000_1_1000.txt -precision 100 -s 1
