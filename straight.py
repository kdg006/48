from math import sqrt


class Straight:
    A, B, C = 1, 1, 1

    @classmethod
    def set_straight(cls, x1, y1, x2, y2):
        a = y2 - y1
        b = x1 - x2
        c = - b * y1 - a * x1
        if c > 0:
            sgn = -1
        else:
            sgn = 1
        j = sgn / sqrt(a ** 2 + b ** 2)
        cls.A = a * j
        cls.B = b * j
        cls.C = c * j
        return cls.A, cls.B, cls.C

    @classmethod
    def check(cls, x, y):
        if abs(cls.A * x + cls.B * y + cls.C) < 1:
            return 1
