from math import sqrt


class Straight:
    A, B, C = 1, 1, 1

    @classmethod
    def set_straight(cls, x1=None, y1=None, x2=None, y2=None):
        if x1 is None:
            x1 = float(input('x1 --> '))
        if y1 is None:
            y1 = float(input('y1 --> '))
        if x2 is None:
            x2 = float(input('x2 --> '))
        if y2 is None:
            y2 = float(input('y2 --> '))
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

    @classmethod
    def check(cls, x, y):
        if abs(cls.A * x + cls.B * y + cls.C) < 1:
            return 1

    @classmethod
    def draw_straight(cls, SIZE, SCALE):
        if cls.A == 0:
            x1, y1 = 0, SIZE / 2 - (-cls.C / cls.B) * SCALE
            x2, y2 = SIZE, SIZE / 2 - (-cls.C / cls.B) * SCALE
        elif cls.B == 0:
            x1, y1 = -cls.C / cls.A * SCALE + SIZE / 2, 0
            x2, y2 = -cls.C / cls.A * SCALE + SIZE / 2, SIZE
        else:
            y1, x1 = SIZE / 2 - SCALE * (-cls.C - cls.A * SIZE / 2) / cls.B, \
                SCALE * (SIZE / 2) + SIZE / 2
            y2, x2 = SIZE / 2 - SCALE * (-cls.C + cls.A * SIZE / 2) / cls.B, \
                SCALE * (-SIZE / 2) + SIZE / 2

        return (x1, y1), (x2, y2)
