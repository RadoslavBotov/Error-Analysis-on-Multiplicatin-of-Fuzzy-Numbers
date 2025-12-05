from typing import override
from .membership_function_base import MembershipFunction


class MembershipFunctionNaive(MembershipFunction):
    def __init__(self, a1: float, a2: float, a3: float):
        super().__init__()
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3

    @override
    def __repr__(self) -> str:
        return "MembershipFunctionNaive" + super().__str__()

    @override
    def membership(self, x: float) -> float:
        if (self.a1 < x <= self.a2):
            return (x - self.a1) / (self.a2 - self.a1)
        
        if (self.a2 <= x < self.a3):
            return (self.a3 - x) / (self.a3 - self.a2)
        
        return 0.0

    @override
    def alpha_cut_left(self, alpha: float) -> float:
        return alpha * (self.a2 - self.a1) + self.a1

    @override
    def alpha_cut_right(self, alpha: float) -> float:
        return self.a3 - alpha * (self.a3 - self.a2)


if __name__ == "__main__":
    f = MembershipFunctionNaive(1, 2, 3)
    print(f)