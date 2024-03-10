class Somase():
    def __init__(self, a):
        self.a = a

    def Calc_soma(self):
        return self.a + 10
    


soma1 = Somase(int(input()))
print(soma1.Calc_soma())