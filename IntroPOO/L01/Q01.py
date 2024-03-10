class Raio:
  
  def __init__(self, raio):
      self.raio = raio

  def calc_area(self):
      return 3.14 * (self.raio ** 2)

  def cal_circf(self):
      return 2 * 3.14 * self.raio

circulo1 = Raio(5)
print(circulo1.cal_circf())
print(circulo1.calc_area())