from matplotlib import pyplot as plt
import numpy as np

from alg.triangular_number import TriangularNumber


tn1 = TriangularNumber(1,2,4)
tn2 = TriangularNumber(2,4,6)
step = 0.1
x = 5

candidates1 = [ # generate x=y*z candidates
            (float(y), float(z))
            for y in np.arange(tn1.a1, tn1.a3+step, step) # int((self.a3 - self.a1) / 
            if (tn2.a1 < (z:= x/y) < tn2.a3)
        ]

candidates2 = [ # generate x=y*z candidates
            (float(y), float(z))
            for y in np.linspace(tn1.a1, tn1.a3, int((tn1.a3 - tn1.a1) / step))
            if (tn2.a1-1e-6 < (z:= x/y) < tn2.a3+1e-6)
        ]

print(candidates1)
print(candidates2)

print(max(min(tn1.membership(y), tn2.membership(z)) for y, z in candidates1))
print(max(min(tn1.membership(y), tn2.membership(z)) for y, z in candidates2))

print()
print()

# plt.plot([c[0] for c in candidates1], [c[1] for c in candidates1])
# plt.plot([c[0] for c in candidates2], [c[1] for c in candidates2])
# plt.show()

