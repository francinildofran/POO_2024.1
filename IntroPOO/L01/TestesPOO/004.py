class Areaquad:
    def __init__(self, lado):
        self.lado = lado

    def Calc_area(self):
        area = self.lado**2


Area = Areaquad()
print(Area.lado(10))