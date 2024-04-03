# https://www.codeabbey.com/index/task_view/median-of-three

tamano = int(input("Ingrese el tamaño de las listas: "))

resultado1 = []

for i in range(tamano):
    numeros = input("Ingrese un par de números separados por un espacio: ").split(" ")
    temp_list = sorted([int(numeros[0]), int(numeros[1]), int(numeros[2])])
    median = temp_list[1]
    resultado1.append(median)


print(' '.join(map(str, resultado1)))

# Gracias ñeifer por explicarme