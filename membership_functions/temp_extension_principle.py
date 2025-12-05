# import math
# from typing import override

# import numpy as np
# from .membership_function_base import MembershipFunction


# class MembershipFunctionExten(MembershipFunction):
#     def __init__(self,
#             a1: float, a2: float, a3: float, b1: float, b2: float, b3: float,
#             u1: "MembershipFunction", u2: "MembershipFunction",
#             step: float = 0.1) -> None:
#         super().__init__()
#         self.a1 = a1
#         self.a2 = a2
#         self.a3 = a3
#         self.b1 = b1
#         self.b2 = b2
#         self.b3 = b3
#         self.A = u1.membership
#         self.B = u2.membership
#         self.step = step

#     @override
#     def __repr__(self) -> str:
#         return "MembershipFunctionExten" + super().__str__()

#     def membership(self, x: float) -> float: # membership(z) = sup(min{membership(x), membership(y)}) for z=x*y
#         result_domain = []
#         result_range = []

#         for c in np.linspace(self.a1*self.b1, self.a2*self.b2, int((self.a2*self.b2 - self.a1*self.b1) / self.step)):
#             result_domain.append(c)
#             t_max = max(self.a1, c/self.b2)
#             t_min = min(self.a2, c/self.b1)
#             result_range.append(max(
#                 self.A(t_min)+self.B(c/t_min)-1,
#                 self.A(t_max)+self.B(c/t_max)-1,
#                 0)
#             )
        
#         for c in np.linspace(self.a2*self.b2, self.a3*self.b3, int((self.a3*self.b3 - self.a2*self.b2) / self.step)):
#             result_domain.append(c)
#             xm = math.sqrt(((1/(self.b2-self.b1))*c)/(1/(self.a2-self.a1)))
#             ym = c/xm
#             t_max = max(self.a2, c/self.b3)
#             t_min = min(self.a3, c/self.b2)
#             if (t_min <= xm <= t_max):
#                 result_range.append(self.A(xm)*self.B(ym))
#             elif (t_max < xm):
#                 result_range.append(self.A(t_max)*self.B(c/t_max))
#             elif (xm < t_min):
#                 result_range.append(self.A(t_min)*self.B(c/t_min))

#         return result_domain, result_range

#     def alpha_cut_left(self, alpha: float) -> float:
#         pass

#     def alpha_cut_right(self, alpha: float) -> float:
#         pass
