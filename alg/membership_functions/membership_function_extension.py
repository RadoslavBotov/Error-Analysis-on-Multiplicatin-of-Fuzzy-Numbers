from typing import override

import numpy as np
from .membership_function_base import MembershipFunction


class MembershipFunctionExten(MembershipFunction):
    def __init__(self,
            a1: float, a3: float, b1: float, b3: float,
            u1: "MembershipFunction", u2: "MembershipFunction",
            *,
            step: float = 0.001) -> None:
        super().__init__()
        self.a1 = a1
        self.a3 = a3
        self.b1 = b1
        self.b3 = b3
        self.A = u1.membership
        self.B = u2.membership
        self.step = step
        self.error = 1e-6

    @override
    def __repr__(self) -> str:
        return "MembershipFunctionExten" + super().__str__()

    def membership(self, x: float) -> float: # membership(x) = sup(min{membership(z), membership(y)}) for x=z*y
        if (x <= self.a1*self.b1 or x >= self.a3*self.b3):
            return 0.0

        candidates = [ # generate x=y*z candidates
            (float(y), float(z))
            # for y in np.arange(self.a1, self.a3, self.step) 
            for y in np.linspace(self.a1, self.a3, int((self.a3 - self.a1) / self.step)) # original
            if (self.b1 - self.error < (z:= x/y) < self.b3 + self.error)
        ]

        if (len(candidates) == 0):
            return 0.0

        return max(min(self.A(y), self.B(z)) for y, z in candidates)

    def alpha_cut_left(self, alpha: float) -> float:
        raise NotImplementedError

    def alpha_cut_right(self, alpha: float) -> float:
        raise NotImplementedError
