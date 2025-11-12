def calcmedia(n1, n2, n3):
    m = (n1 + n2 + n3) / 3
    if m >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

# Bloco principal
a = float(input("Digite a nota 1: "))
b = float(input("Digite a nota 2: "))
c = float(input("Digite a nota 3: "))

resultado = calcmedia(a, b, c)

print("A média é:", (a + b + c) / 3)
print("Situação:", resultado)