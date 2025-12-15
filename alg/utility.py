from functools import wraps
import math
import random
import sys
import time
from matplotlib import pyplot as plt
import numpy as np
from .membership_functions.membership_function_alpha import MembershipFunctionAlpha
from .triangular_number import TriangularNumber


def timing(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        time_start = time.time()
        result = f(*args, **kwargs)
        time_end = time.time()
        print('func:%r took: %2.10f sec' % \
        (f.__name__, time_end - time_start))
        return result
    return wrap

def make_task_list(l, parts):
    n = min(parts, max(len(l),1))
    k, m = divmod(len(l), n)
    return [l[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n)]

# @timing
def plot_tn(tn: TriangularNumber, *, label: str|None = None, precision : int = 100) -> None:
    x_points = np.linspace(tn.a1 - 1, tn.a3 + 1, precision)
    y_points = np.vectorize(lambda x : tn.membership(x))(x_points)
    plt.plot(x_points, y_points, label=(str(tn.u.__class__)[-7:-2] if label is None else label))
    plt.legend(loc="upper right")

def plot_show():
    plt.show()

def plot_tn_alpha(tn: TriangularNumber, *, label: str|None = None, precision : int = 100) -> None:
    y_points = np.linspace(0, 1, precision)
    x_1_points = np.vectorize(lambda x : tn.alpha_cut_left(x))(y_points)
    x_2_points = np.vectorize(lambda x : tn.alpha_cut_right(x))(y_points)
    plt.plot(x_1_points, y_points, label=(str(tn.u.__class__)[-7:-2] if label is None else label))
    plt.plot(x_2_points, y_points, label=(str(tn.u.__class__)[-7:-2] if label is None else label))
    plt.legend(loc="upper right")

def generate_random_tn(left: int, right: int, use_float: bool = False) -> TriangularNumber:
    if (use_float is True):
        a2 = random.uniform(left+1, right-1)
        a1 = random.uniform(left, a2-1)
        a3 = random.uniform(a2+1, right)
    else:
        a2 = random.randint(left+1, right-1)
        a1 = random.randint(left, a2-1)
        a3 = random.randint(a2+1, right)
    return TriangularNumber(a1, a2, a3)

@timing
def minkowski_distance_tn(tn1: TriangularNumber, tn2: TriangularNumber, w: int = 1, precision: float = 100) -> float:
    # Generalization of Manhattan distance (w = 1) and Euclidean distance (w = 2).
    x_range = np.linspace(tn1.a1, tn2.a3, precision)
    y_range_tn1 = [tn1.membership(x) for x in x_range]
    y_range_tn2 = [tn2.membership(x) for x in x_range]
    return minkowski_distance(y_range_tn1, y_range_tn2, w)

def minkowski_distance(y_range_tn1: list[float], y_range_tn2: list[float], w: int = 1) -> float:
    return (sum(abs(y1 - y2)**w for y1, y2 in zip(y_range_tn1, y_range_tn2)))**(1./w)

def cosine_similarity_tn(tn1: TriangularNumber, tn2: TriangularNumber, precision: float = 100) -> float:
    x_range = np.linspace(tn1.a1, tn2.a3, precision)
    y_range_tn1 = [float(tn1.membership(x)) for x in x_range]
    y_range_tn2 = [float(tn2.membership(x)) for x in x_range]
    return cosine_similarity(y_range_tn1, y_range_tn2)

def cosine_similarity(y_range_tn1: list[float], y_range_tn2: list[float]) -> float:
    d1 = abs(sum(y1 * y2 for y1, y2 in zip(y_range_tn1, y_range_tn2)))
    d2 = sum(y1**2 for y1 in y_range_tn1)
    d3 = sum(y2**2 for y2 in y_range_tn2)
    try:
        return d1 / math.sqrt(d2 * d3)
    except ZeroDivisionError:
        return 0.0

def min_max_similarity_tn(tn1: TriangularNumber, tn2: TriangularNumber, precision: float = 100) -> float:
    x_range = np.linspace(tn1.a1, tn2.a3, precision)
    y_range_tn1 = [tn1.membership(x) for x in x_range]
    y_range_tn2 = [tn2.membership(x) for x in x_range]
    return min_max_similarity(y_range_tn1, y_range_tn2, w)

def min_max_similarity(y_range_tn1: list[float], y_range_tn2: list[float]) -> float:
    d1 = abs(sum(min(y1, y2) for y1, y2 in zip(y_range_tn1, y_range_tn2)))
    d2 = abs(sum(max(y1, y2) for y1, y2 in zip(y_range_tn1, y_range_tn2)))
    try:
        return d1 / d2
    except ZeroDivisionError:
        return 0.0

def save_triangular_numbers(triangular_numbers: list[TriangularNumber], file: str) -> None:
    if file == "stdout":
        out = sys.stdout
    else:
        out = open(file, 'w')
    
    for tn in triangular_numbers:
        out.write(f"{tn}\n") # call __str__ of TriangularNumber

    out.flush()
    out.close()

def parse_string_to_triangular_number(line: str) -> TriangularNumber:
    def parse_float_number(x: str) -> float:
        try:
            return float(x)
        except ValueError:
            return None
    # remove unwanted characters    
    unwanted_characters  = ",:'\"\n"
    for character in unwanted_characters:
        line = line.replace(character, '')

    # isolate triangular number and membership function parts
    triangular_number_part = line[18:line.find('M')-3]
    membership_function_part = line[line.find('M')+24:len(line)-3]
    
    # get integers only
    triangular_number_part = [y for x in triangular_number_part.split(' ') if ((y := parse_float_number(x)) is not None)]
    membership_function_part = [y for x in membership_function_part.split(' ') if ((y := parse_float_number(x)) is not None)]
    
    # make TriangularNumber based on membership function(Naive/Alpha)
    tn = None
    if "Alpha" in line:
        a1, a2, a3 = triangular_number_part
        u1, u2, u3, u4, u5, u6 = membership_function_part[3:]
        u = MembershipFunctionAlpha(a1, a2, a3, 1, 1, 1, u1=u1, u2=u2, u3=u3, u4=u4, u5=u5, u6=u6)
        tn = TriangularNumber(a1, a2, a3, u)
    else:
        a1, a2, a3 = triangular_number_part
        tn = TriangularNumber(a1, a2, a3)

    return tn

def load_triangular_numbers(file: str) -> list[TriangularNumber]:
    triangular_numbers = []

    with open(file, "r") as f:
        lines = f.readlines()
        triangular_numbers = [parse_string_to_triangular_number(line) for line in lines]

    return triangular_numbers
