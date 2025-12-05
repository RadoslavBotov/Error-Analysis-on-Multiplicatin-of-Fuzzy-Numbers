import math
from typing import override
from .membership_function_base import MembershipFunction


class MembershipFunctionAprox(MembershipFunction):
    def __init__(self,
            a1: float, a2: float, a3: float, b1: float, b2: float, b3: float,
            u1: float|None = None, u2: float|None = None, u3: float|None = None,
            u4: float|None = None, u5: float|None = None, u6: float|None = None):
        super().__init__()
        self.a1 = a1 * b1
        self.a2 = a2 * b2
        self.a3 = a3 * b3
        self.u1 = a2*b2 - a2*b1 - a1*b2 + a1*b1 if u1 is None else u1
        self.u2 = a2*b1 + a1*b2 - 2*a1*b1  if u2 is None else u2
        self.u3 = a1*b1  if u3 is None else u3
        self.v1 = a3*b3 - a3*b2 - a2*b3 + a2*b2  if u4 is None else u4
        self.v2 = a2*b3 + a3*b2 - 2*a3*b3  if u5 is None else u5
        self.v3 = a3*b3  if u6 is None else u6

    @override
    def __repr__(self) -> str:
        return "MembershipFunctionAlpha" + super().__str__()

    @override
    def membership(self, x: float) -> float:
        if (self.a1 < x < self.a2):
            return (x -self.u3) / (self.u1 + self.u2)
        
        if (self.a2 < x < self.a3):
            return (x -self.v3) / (self.v1 + self.v2)

        return 0.0

    @override
    def alpha_cut_left(self, alpha: float) -> float:
        return (self.u1 + self.u2) * alpha + self.u3

    @override
    def alpha_cut_right(self, alpha: float) -> float:
        return (self.v1 + self.v2) * alpha + self.v3
