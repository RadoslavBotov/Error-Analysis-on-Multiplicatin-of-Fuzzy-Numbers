
from matplotlib import pyplot as plt
from triangular_number import TriangularNumber
from utility import plot_tn


if __name__ == "__main__":
    tn1 = TriangularNumber(2,3,5)
    tn2 = TriangularNumber(3,5,6)

    # tn1 = TriangularNumber(20,30,50)
    # tn2 = TriangularNumber(30,50,60)

    # tn1 = TriangularNumber(200,300,500)
    # tn2 = TriangularNumber(300,500,600)

    r1 = tn1.mul_naive(tn2)
    r2 = tn1.mul_standard_approx(tn2)
    r3 = tn1.mul_alpha_cut(tn2)
    r4 = tn1.mul_extension(tn2, 0.001) # bigger TN should use a bigger step

    plot_tn(r1)
    plot_tn(r2)
    plot_tn(r3)
    plot_tn(r4)

    plt.show()
