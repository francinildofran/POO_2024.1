print("Digite a base e a altura do retângulo")
base = int(input())
altura = int(input())

area = base * altura
perimetro = 2 * (base + altura)
diagonal = (base ** 2 + altura ** 2) ** 0.5

print("Área = ", area ," Perímetro =", perimetro ," Diagonal =", diagonal)