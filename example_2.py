import numpy as np
from triangular_number import TriangularNumber

def calculate_alpha_cut_diff(tn_naive: "TriangularNumber", tn_alpha_cut: "TriangularNumber", precision: float = 100):
    alpha_points = np.linspace(0, 1, precision+1)
    
    tn_naive_left_points = np.vectorize(lambda x : tn_naive.alpha_cut_left(x))(alpha_points)
    tn_naive_right_points = np.vectorize(lambda x : tn_naive.alpha_cut_right(x))(alpha_points)
    tn_alpha_cut_left_points = np.vectorize(lambda x : tn_alpha_cut.alpha_cut_left(x))(alpha_points)
    tn_alpha_cut_right_points = np.vectorize(lambda x : tn_alpha_cut.alpha_cut_right(x))(alpha_points)
    
    return tn_alpha_cut_left_points, tn_alpha_cut_right_points, tn_naive_left_points, tn_naive_right_points

def number_similarity(alpha, naive):
    return np.minimum(alpha, naive) / np.maximum(alpha, naive) # = 1 - abs(alpha - naive) / alpha
    # return 1 - abs(alpha - naive) / alpha

def calculate_left_right_error(tn_alpha_cut_left_points, tn_alpha_cut_right_points, tn_naive_left_points, tn_naive_right_points):
    error_left = number_similarity(tn_alpha_cut_left_points, tn_naive_left_points)
    error_right = number_similarity(tn_alpha_cut_right_points, tn_naive_right_points)
    return error_left, error_right

tn1 = TriangularNumber(1,2,4)
tn2 = TriangularNumber(2,4,6)

res1 = tn1.mul_naive(tn2)
res2 = tn1.mul_standard_approx(tn2)

tn_a_l, tn_a_r, tn_n_l, tn_n_r = calculate_alpha_cut_diff(res1, res2, precision=1000)
err_l, err_r = calculate_left_right_error(tn_n_l, tn_n_r, tn_a_l, tn_a_r)

print(np.concatenate([tn_a_l, tn_a_r, tn_n_l, tn_n_r, err_l, err_r]).reshape((-1, 6), order='F'))
print(np.average(err_l))
print(np.average(err_r))
# Show how Naive Multiplication and Standard Approximation Multiplication have the same alpha-cut
