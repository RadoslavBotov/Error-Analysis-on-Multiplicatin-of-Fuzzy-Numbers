import math
from typing import override

from .membership_function_base import MembershipFunction


class MembershipFunctionAlpha(MembershipFunction):
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
            return self._get_D(x, self.u1, self.u2, self.u3, True)
        
        if (self.a2 < x < self.a3):
            return self._get_D(x, self.v1, self.v2, self.v3, False)

        return 0.0

    def _get_D(self, x: float, a: float, b: float, c: float, sign: bool = True) -> float:
        if sign is True:
            return (-b + math.sqrt(b*b - 4*a*(c - x))) / (2*a)
        else:
            return (-b - math.sqrt(b*b - 4*a*(c - x))) / (2*a)

    @override
    def alpha_cut_left(self, alpha: float) -> float:
        return self.u1 * alpha * alpha + self.u2 * alpha + self.u3

    @override
    def alpha_cut_right(self, alpha: float) -> float:
        return self.v1 * alpha * alpha + self.v2 * alpha + self.v3
