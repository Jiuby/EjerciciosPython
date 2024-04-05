# https://www.codeabbey.com/index/task_view/rounding--es
import math

tamano = int(input("Ingrese el tamaño de las listas: "))

resultado = []

for i in range(tamano):
    procedimiento = list(map(int, input().split()))
    division = procedimiento[0] / procedimiento[1]
    division = int(division + 0.5 * math.copysign(1, division))
    resultado.append(division)

print(" ".join(map(str, resultado)))

# Aqui aprendimos que la variable siempre adentro