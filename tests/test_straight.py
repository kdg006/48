from r2point import R2Point
from convex import Point, Segment, Polygon
from straight import Straight


class TestPoint:

    def setup_method(self):
        Straight.set_straight(1, 1, 0, 0)
        self.a = Point(R2Point(1, 1))

    # Точка не содержит рёбер
    def test_point(self):
        assert self.a.count == 0


class TestSegment1:

    def setup_method(self):
        Straight.set_straight(1, 1, 0, 0)
        self.a = Segment(R2Point(0, 0), R2Point(2, 2))

    # Окресность ребра равняется 1
    def test1_segment(self):
        assert self.a.count == 1

    # Окресность удлинённого ребра равняется 1
    def test2_segment(self):
        assert self.a.add(R2Point(5, 5)).count == 1


class TestSegment2:

    def setup_method(self):
        Straight.set_straight(1, 1, 0, 0)
        self.a = Segment(R2Point(0, 0), R2Point(5, 2))

    # Окресность ребра не равняется 1
    def test_segment(self):
        assert self.a.count == 0


class TestPolygon1:

    def setup_method(self):
        Straight.set_straight(1, 1, 0, 0)
        self.a = Polygon(R2Point(0, 0), R2Point(1, 1), R2Point(0.5, 1))

    # Сумма окресностей рёбер треугольника
    def test1_polygon(self):
        assert self.a.count == 3

    # Сумма окресностей многоугольника
    def test2_polygon(self):
        assert self.a.add(R2Point(0.5, 0)).count == 4


class TestPolygon2:

    def setup_method(self):
        Straight.set_straight(-1, 1, 1, -1)
        self.a = Polygon(R2Point(0, 0), R2Point(0.5, 0), R2Point(0, 0.5))

    # Сумма окресностей рёбер треугольника
    def test1_polygon2(self):
        assert self.a.count == 3

    # Сумма окресностей нового треугольника
    def test2_polygon2(self):
        assert self.a.add(R2Point(-3, -3)).count == 1

    # Cумма окресностей многоугольника
    def test3_polygon2(self):
        assert self.a.add(R2Point(-3, -3)).add(R2Point(3, 3)).count == 0
