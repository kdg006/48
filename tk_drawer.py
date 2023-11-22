from tkinter import *
from straight import Straight

# Размер окна
SIZE = 600
# Коэффициент гомотетии
SCALE = 50


def x(p):
    """ преобразование x-координаты """
    return SIZE / 2 + SCALE * p.x


def y(p):
    """ преобразование y-координаты """
    return SIZE / 2 - SCALE * p.y


class TkDrawer:
    """ Графический интерфейс для выпуклой оболочки """

    # Конструктор
    def __init__(self):
        self.root = Tk()
        self.root.title("Выпуклая оболочка")
        self.root.geometry(f"{SIZE+5}x{SIZE+5}")
        self.root.resizable(False, False)
        self.root.bind('<Control-c>', quit)
        self.canvas = Canvas(self.root, width=SIZE, height=SIZE)
        self.canvas.pack(padx=5, pady=5)

    # Завершение работы
    def close(self):
        self.root.quit()

    def draw_straight(self):
        x1 = float(input('x1 --> '))
        y1 = float(input('y1 --> '))
        x2 = float(input('x2 --> '))
        y2 = float(input('y2 --> '))
        A, B, C = Straight.set_straight(x1, y1, x2, y2)
        if A == 0:
            x1, y1 = 0, SIZE / 2 - (-C / B) * SCALE
            x2, y2 = SIZE, SIZE / 2 - (-C / B) * SCALE
        elif B == 0:
            x1, y1 = C / A * SCALE + SIZE / 2, 0
            x2, y2 = -C / A * SCALE + SIZE / 2, SIZE
        else:
            y1, x1 = SIZE / 2 - SCALE * (-C - A * SIZE / 2) / B, \
                SCALE * (SIZE / 2) + SIZE / 2
            y2, x2 = SIZE / 2 - SCALE * (-C + A * SIZE / 2) / B, \
                SCALE * (-SIZE / 2) + SIZE / 2

        return (x1, y1), (x2, y2)

    def get_points(self):
        self.a, self.b = TkDrawer.draw_straight(self)

    # Стирание существующей картинки и рисование осей координат
    def clean(self):
        self.canvas.create_rectangle(0, 0, SIZE, SIZE, fill="white")
        self.canvas.create_line(0, SIZE / 2, SIZE, SIZE / 2, fill="blue")
        self.canvas.create_line(SIZE / 2, 0, SIZE / 2, SIZE, fill="blue")
        self.canvas.create_line(self.a[0], self.a[1], self.b[0], self.b[1],
                                fill="red")
        self.root.update()

    # Рисование точки
    def draw_point(self, p):
        self.canvas.create_oval(
            x(p) + 1, y(p) + 1, x(p) - 1, y(p) - 1, fill="black")
        self.root.update()

    # Рисование линии
    def draw_line(self, p, q):
        self.canvas.create_line(x(p), y(p), x(q), y(q), fill="black", width=2)
        self.root.update()


if __name__ == "__main__":

    import time
    from r2point import R2Point
    tk = TkDrawer()
    tk.clean()
    tk.draw_point(R2Point(2.0, 2.0))
    tk.draw_line(R2Point(0.0, 0.0), R2Point(1.0, 1.0))
    tk.draw_line(R2Point(0.0, 0.0), R2Point(1.0, 0.0))
    time.sleep(5)
