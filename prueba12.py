# https://www.codeabbey.com/index/task_view/arithmetic-progression
tamano = int(input("Ingrese el tamaño de las listas: "))

resultado1 = []

for i in range(tamano):
    numeros = input("Ingrese un par de números separados por un espacio: ").split(" ")
    lista = [int(numeros[0]), int(numeros[1]), int(numeros[2])]
    c = lista[2]
    a = lista[0]
    b = lista[1]
    ArithmeticProgression = c/2 * (2*a + (c-1)*b)
    ArithmeticProgression = int(ArithmeticProgression)
    resultado1.append(ArithmeticProgression)

print(' '.join(map(str, resultado1)))
