"""Plots all triangular numbers given from text file on a common graph."""

import argparse
from matplotlib import pyplot as plt

from triangular_number import TriangularNumber
from utility import load_triangular_numbers, plot_tn


def init_parser() -> "argparse.ArgumentParser":
    parser = argparse.ArgumentParser(
        prog='PlotTriangularNumbers',
        description='Plots all triangular numbers from given file. Uses a given membership function if present, otherwise asumes naive MF.')
    parser.add_argument('-file', '-f', type=str, help='Name of file where the TN are saved.')
    parser.add_argument('-precision', '-p', nargs='?', type=int, default=100, help='Precision with which TN are plotted. (default=100)')
    return parser

def parse_arguments(parser: "argparse.ArgumentParser") -> tuple[str, int]:
    namespace = parser.parse_args() # ["-file=data\\triangular_numbers_a100_l1_r100.txt"]
    file_name, precision = namespace.file, namespace.precision
    return file_name, precision

def validate_arguments(precision: int) -> int:
    if precision < 10:
        precision = 100
    return precision

def plot_tns(triangular_numbers: list["TriangularNumber"], precision: int) -> None:
    for tn in triangular_numbers:
        plot_tn(tn, precision)

def main():
    parser = init_parser()
    file_name, precision = parse_arguments(parser)
    precision = validate_arguments(precision)
    triangular_numbers = load_triangular_numbers(file_name)
    plot_tns(triangular_numbers, precision)
    plt.show()

if __name__ == "__main__":
    main()
