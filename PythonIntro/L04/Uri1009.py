nome = input()
salario = float(input())
tvendas = float(input())

comissao = tvendas * 0.15
stotal = salario + comissao
print("TOTAL = R$ %.2f" % stotal)