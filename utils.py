import math


class Utils:

    def square(a: int) -> int:
        print(math.sqrt(a))
        return math.sqrt((a))

    def pow(a: int) -> int:
        print(math.pow(a, 2))
        return math.pow((a, 2))

    def odd_value(a: int) -> bool:
        if a % 2 == 0:
            return True
        return False
