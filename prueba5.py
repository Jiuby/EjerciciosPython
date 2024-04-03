# https://www.codeabbey.com/index/task_view/min-of-three

tamano = int(input("Ingrese el tamaño de las listas: "))

lista1 = []
lista2 = []
lista3 = []

resultado = []

for i in range(tamano):
    numeros = input("Ingrese un par de números separados por un espacio: ").split(" ")
    lista1.append(int(numeros[0]))
    lista2.append(int(numeros[1]))
    lista3.append(int(numeros[2]))
    resultado.append(min(int(numeros[0]), int(numeros[1]), int(numeros[2])))

if len(lista1) != tamano:
    print("La longitud de la lista1 no coincide con el número introducido")
elif len(lista2) != tamano:
    print("La longitud de la lista2 no coincide con el número introducido")
elif len(lista3) != tamano:
    print("La longitud de la lista3 no coincide con el número introducido")

print(' '.join(map(str, resultado)))