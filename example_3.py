# Naive Left Value, Naive Right Value, Alpha Left Value, Alpha Right Value, Left Error, Right Error
# print(np.concatenate([tn_a_l, tn_a_r, tn_n_l, tn_n_r, err_l, err_r]).reshape((-1, 6), order='F'))

from alg.triangular_number import TriangularNumber
from alg.utility import timing


@timing
def timed_mul(x, tn):
    return tn.membership(x)

iters = 5
x_value = 1

print("====================== ALPHA-CUT ==============================")
# x = x_value
# for i in range(iters):
#     p = 10**i
#     tn1 = TriangularNumber(1*p, 2*p, 4*p)
#     tn2 = TriangularNumber(2*(p/10), 4*(p/10), 6*(p/10))
#     res = tn1.mul_alpha_cut(tn2)
#     print(x, timed_mul(x, res))
#     tn1 = TriangularNumber(1*p, 2*p, 4*p)
#     tn2 = TriangularNumber(2*p, 4*p, 6*p)
#     res = tn1.mul_alpha_cut(tn2)
#     print(x * 10, timed_mul(x*10, res))
#     x *= 100

print("====================== STANDARD-APPROX ==============================")
x = x_value
for i in range(iters):
    p = 10**i
    tn1 = TriangularNumber(1*p, 2*p, 4*p)
    tn2 = TriangularNumber(2*(p/10), 4*(p/10), 6*(p/10))
    res = tn1.mul_standard_approx(tn2)
    print(x, timed_mul(x, res))
    tn1 = TriangularNumber(1*p, 2*p, 4*p)
    tn2 = TriangularNumber(2*p, 4*p, 6*p)
    res = tn1.mul_standard_approx(tn2)
    print(x * 10, timed_mul(x*10, res))
    x *= 100

print("====================== EXTENSION-PRINCIPLE ==============================")
# x = x_value
# for i in range(iters):
#     p = 10**i
#     tn1 = TriangularNumber(1*p, 2*p, 4*p)
#     tn2 = TriangularNumber(2*(p/10), 4*(p/10), 6*(p/10))
#     res = tn1.mul_extension(tn2, step=1)
#     print(x, timed_mul(x, res))
#     tn1 = TriangularNumber(1*p, 2*p, 4*p)
#     tn2 = TriangularNumber(2*p, 4*p, 6*p)
#     res = tn1.mul_extension(tn2, step=1)
#     print(x * 10, timed_mul(x*10, res))
#     x *= 100

print("====================== NAIVE ==============================")
# x = x_value
# for i in range(iters):
#     p = 10**i
#     tn1 = TriangularNumber(1*p, 2*p, 4*p)
#     tn2 = TriangularNumber(2*(p/10), 4*(p/10), 6*(p/10))
#     res = tn1.mul_naive(tn2)
#     print(x, timed_mul(x, res))
#     tn1 = TriangularNumber(1*p, 2*p, 4*p)
#     tn2 = TriangularNumber(2*p, 4*p, 6*p)
#     res = tn1.mul_naive(tn2)
#     print(x * 10, timed_mul(x*10, res))
#     x *= 100
