from .membership_functions.membership_function_extension import MembershipFunctionExten
from .membership_functions.membership_function_aproximate import MembershipFunctionAprox
from .membership_functions.membership_function_alpha import MembershipFunctionAlpha
from .membership_functions.membership_function_base import MembershipFunction
from .membership_functions.membership_function_naive import MembershipFunctionNaive


class TriangularNumber:
    def __init__(self, a1: float, a2: float, a3: float, u: "MembershipFunction" = None):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.u = MembershipFunctionNaive(self.a1, self.a2, self.a3) if u is None else u

    def __str__(self) -> str:
        return f"TriangularNumber({self.__dict__})"
    
    def __repr__(self) -> str:
        return f"TriangularNumber('a1': {self.a1}, 'a2': {self.a2}, 'a3': {self.a3}, 'u': {str(self.u.__class__)[-7:-2]})"

    def save_to_file(self, file: str) -> None:
        with open(file, "a") as f:
            f.write(self + '\n')

    def membership(self, x: float) -> float:
        return self.u.membership(x)

    def alpha_cut_left(self, alpha: float) -> float:
        return self.u.alpha_cut_left(alpha)

    def alpha_cut_right(self, alpha: float) -> float:
        return self.u.alpha_cut_right(alpha)

    def mul_naive(self, other: "TriangularNumber") -> "TriangularNumber":
        a_new, b_new, c_new = self._calculate_new_values(other)
        return TriangularNumber(a_new, b_new, c_new)

    def mul_alpha_cut(self, other: "TriangularNumber") -> "TriangularNumber":
        a_new, b_new, c_new = self._calculate_new_values(other)
        newMembershipFunc = MembershipFunctionAlpha(self.a1, self.a2, self.a3, other.a1, other.a2, other.a3)
        return TriangularNumber(a_new, b_new, c_new, newMembershipFunc)

    def mul_standard_approx(self, other: "TriangularNumber") -> "TriangularNumber":
        a_new, b_new, c_new = self._calculate_new_values(other)
        newMembershipFunc = MembershipFunctionAprox(self.a1, self.a2, self.a3, other.a1, other.a2, other.a3)
        return TriangularNumber(a_new, b_new, c_new, newMembershipFunc)
    
    def mul_extension(self, other: "TriangularNumber", step: float = 0.001) -> "TriangularNumber":
        a_new, b_new, c_new = self._calculate_new_values(other)
        newMembershipFunc = MembershipFunctionExten(self.a1, self.a3, other.a1, other.a3, self.u, other.u, step=step)
        return TriangularNumber(a_new, b_new, c_new, newMembershipFunc)

    def _calculate_new_values(self, other: "TriangularNumber") -> tuple[float, float, float]:
        a_new = self.a1 * other.a1
        b_new = self.a2 * other.a2
        c_new = self.a3 * other.a3
        return a_new, b_new, c_new
