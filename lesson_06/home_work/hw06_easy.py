# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
import math

class Triangle ():
    def __init__(self, a_x, a_y, b_x, b_y, c_x, c_y):
        self.a_x = a_x
        self.a_y = a_y
        self.b_x = b_x
        self.b_y = b_y
        self.c_x = c_x
        self.c_y = c_y
        self.AB = round (math.sqrt(int (math.fabs(((b_y - a_y)**2) + ((b_x - a_x)**2)))),2)
        self.BC = round(math.sqrt(int(math.fabs(((c_y - b_y) ** 2) + ((c_x - b_x) ** 2)))), 2)
        self.CA = round(math.sqrt(int(math.fabs(((a_y - c_y) ** 2) + ((a_x - c_x) ** 2)))), 2)

    def perimeter(self):
        self.perimeter = (self.AB + self.BC + self.CA)
        return (self.perimeter)

    def area(self):
        self.perimeter /=2
        self.area =  round(math.sqrt(self.perimeter*(self.perimeter - self.AB)*(self.perimeter - self.BC)* (self.perimeter - self.CA)),2)
        return (self.area)

    def height(self):
        self.area *=2
        self.height =  round((self.area / self.CA),2)
        return (self.height)

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class trapezium:
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4

    def all_side(self):
        a = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
        b = math.sqrt((self.x3 - self.x2) ** 2 + (self.y3 - self.y2) ** 2)
        c = math.sqrt((self.x4 - self.x3) ** 2 + (self.y4 - self.y3) ** 2)
        d = math.sqrt((self.x1 - self.x4) ** 2 + (self.y1 - self.y4) ** 2)
        return a, b, c, d

    def side(self):
        side = setting.all_side()
        if side[0] == side[2]:
            return "Трапеция равнобедренная."
        else:
            return "Трапеция не равнобедренная."

    def perimeter(self):
        side = setting.all_side()
        perimeter_trapeze = side[0] + side[1] + side[2] + side[3]
        return perimeter_trapeze

    def area(self):
        side = setting.all_side()
        area = ((side[1] + side[3]) / 2) * math.sqrt(side[0]**2 - ((((side[3]-side[1]) ** 2 + side[0] ** 2 - side[2] ** 2 )/(2 * (side[3]-side[1]))) ** 2))
        return area
