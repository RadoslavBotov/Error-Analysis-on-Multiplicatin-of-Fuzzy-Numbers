
from matplotlib import pyplot as plt
from triangular_number import TriangularNumber
from utility import minkowski_distance_tn, plot_tn, plot_tn_alpha, timing

# @timing
def timed_membership(tn: TriangularNumber, x: float) -> float:
    return tn.membership(x)

def get_matching_points(baseline: str, observed: str):
    points = 0
    i = 2
    while (i < len(baseline) and i < len(observed)):
        if (baseline[i] == observed[i]):
            points += 1
            i += 1
        else:
            break
    print(f"Matching decimal numbers: {points}")

if __name__ == "__main__":
    tn1 = TriangularNumber(1,2,4)
    tn2 = TriangularNumber(2,4,6)
    x = 5
    # tn1 = TriangularNumber(10,20,40)
    # tn2 = TriangularNumber(20,40,60)
    # x = 500
    # tn1 = TriangularNumber(100,200,400)
    # tn2 = TriangularNumber(200,400,600)
    # x = 50000

    r1 = tn1.mul_naive(tn2)
    r2 = tn1.mul_standard_approx(tn2)
    r3 = tn1.mul_alpha_cut(tn2)
    r4_0 = tn1.mul_extension(tn2, 1)
    r4_1 = tn1.mul_extension(tn2, 0.1)
    r4_2 = tn1.mul_extension(tn2, 0.01)
    r4_3 = tn1.mul_extension(tn2, 0.001)

    # tm1 = timed_membership(r1, x)
    # tm2 = timed_membership(r2, x)
    # tm3 = timed_membership(r3, x)
    # tm4 = timed_membership(r4_0, x)
    # tm5 = timed_membership(r4_1, x)
    # tm6 = timed_membership(r4_2, x)
    # tm7 = timed_membership(r4_3, x)

    # print("Naive:", tm1)
    # print("Standard Approx:", tm2)
    # print("Alpha-cut:", tm3)
    # print("Extension 1:", tm4)
    # print("Extension 0.1:", tm5)
    # print("Extension 0.01:", tm6)
    # print("Extension 0.001:", tm7)

    # get_matching_points(str(tm3), str(tm1))
    # get_matching_points(str(tm3), str(tm2))
    # get_matching_points(str(tm3), str(tm4))
    # get_matching_points(str(tm3), str(tm5))
    # get_matching_points(str(tm3), str(tm6))
    # get_matching_points(str(tm3), str(tm7))

    # print(minkowski_distance_tn(r1, r2))
    # print(minkowski_distance_tn(r1, r3))
    # print(minkowski_distance_tn(r1, r4_0))
    # print(minkowski_distance_tn(r1, r4_1))
    # print(minkowski_distance_tn(r1, r4_2))
    # print(minkowski_distance_tn(r1, r4_3))

    plot_tn(tn1)
    plot_tn(tn2)
    # plot_tn(r1) # Naive
    # plot_tn(r2) # Standard Approximation
    plot_tn(r3) # Alpha-cut
    plot_tn_alpha(r3, label="alpha-cut")
    # plot_tn(r4_0, label="Exten 1") # Extension 1
    # plot_tn(r4_1, label="Exten 0.1") # Extension 0.1
    # plot_tn(r4_2, label="Exten 0.01") # Extension 0.01
    # plot_tn(r4_3, label="Exten 0.001") # Extension 0.001
    plt.show()
