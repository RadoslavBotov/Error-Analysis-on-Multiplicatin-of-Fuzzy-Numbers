from matplotlib import pyplot as plt
from alg.triangular_number import TriangularNumber
from alg.utility import plot_tn


tn1 = TriangularNumber(1,2,4)
tn2 = TriangularNumber(2,4,6)
plot_tn(tn1, precision=500, label="A(1, 2, 4)")
plot_tn(tn2, precision=500, label="B(2, 4, 6)")


# res1 = tn1.mul_alpha_cut(tn2)
# plot_tn(res1, precision=500, label="C(2, 8, 24)")
# file_name = "figures\\figure_mul_alpha_cut_result.png"


# res2 = tn1.mul_standard_approx(tn2)
# plot_tn(res2, precision=500, label="C(2, 8, 24)")
# file_name = "figures\\figure_mul_standard_approx_result.png"


# res3 = tn1.mul_naive(tn2)
# plot_tn(res3, precision=500, label="C(2, 8, 24)")
# file_name = "figures\\figure_mul_naive_result.png"


# res4 = tn1.mul_extension(tn2, step=1)
# res5 = tn1.mul_extension(tn2, step=0.1)
# res6 = tn1.mul_extension(tn2, step=0.01)
# # res7 = tn1.mul_extension(tn2, step=0.001)
# plot_tn(res4, precision=500, label="C(2, 8, 24, стъпка=1)")
# plot_tn(res5, precision=500, label="C(2, 8, 24, стъпка=0.1)")
# plot_tn(res6, precision=500, label="C(2, 8, 24, стъпка=0.01)")
# # plot_tn(res7, precision=500, label="C(2, 8, 24)(стъпка=0.001)")
# file_name = "figures\\figure_mul_extension_result.png"


plt.xlabel("Universum")
plt.ylabel("Membership Function")
# plt.savefig(file_name, transparent=False, format="png", bbox_inches="tight")
plt.show()
