# https://www.codeabbey.com/index/task_view/sum-of-digits

tamano = int(input("Ingrese el tamaño de las listas: "))

lista1 = []
lista2 = []
lista3 = []

resultado1 = []
resultado2 = []

for i in range(tamano):
    numeros = input("Ingrese un par de números separados por un espacio: ").split(" ")
    lista1.append(int(numeros[0]))
    lista2.append(int(numeros[1]))
    lista3.append(int(numeros[2]))
    resultado1.append(int(numeros[0]) * int(numeros[1]) + int(numeros[2]))
    resultado2.append(sum(map(int, str(resultado1[i]))))

print(' '.join(map(str, resultado2)))