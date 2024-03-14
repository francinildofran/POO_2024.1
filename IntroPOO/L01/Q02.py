class Viagem:
  def __init__(self, distancia, tempo):
    self.distancia = distancia
    self.tempo = tempo

  def vel_media(self):
      return (self.distancia / self.tempo


viagem1 = Viagem(int(input()), int(input()))
print(viagem1.vel_media())