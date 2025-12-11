class MembershipFunction:
    def __str__(self) -> str:
        return f"{self.__dict__}"
    
    def __repr__(self) -> str:
        return self.__str__()

    def membership(self, x: float) -> float:
        pass

    def alpha_cut_left(self, alpha: float) -> float:
        pass

    def alpha_cut_right(self, alpha: float) -> float:
        pass
