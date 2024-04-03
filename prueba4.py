# https://www.codeabbey.com/index/task_view/min-of-two

tamano = int(input("Ingrese el tamaño de las listas: "))

lista1 = []
lista2 = []

resultado = []

for i in range(tamano):
    numeros = input("Ingrese un par de números separados por un espacio: ").split(" ")
    lista1.append(int(numeros[0]))
    lista2.append(int(numeros[1]))
    resultado.append(min(int(numeros[0]), int(numeros[1])))

if len(lista1) != tamano:
    print("La longitud de la lista1 no coincide con el número introducido")
elif len(lista2) != tamano:
    print("La longitud de la lista2 no coincide con el número introducido")

print(' '.join(map(str, resultado)))

# tamano es la cantidad de numeros que deben de tener las listas

# lista1 es la lista de los primeros números que se van a comparar
# lista2 es la lista de los segundos números que se van a comparar

# resultado es la lista de los resultados de las comparaciones

# for es para que se repita el proceso de ingresar los números la cantidad de veces que se haya indicado en tamano
# numeros es para pedir los números que se van a comparar y se separan con split para cumplir con el formato de la pagina
# append es para agregar los números a la lista
# int es para que los números ingresados sean enteros
# [0] es para que se tome el primer número de la lista por ejemplo si el usuario ingreso 1 y 2 se tomara el 1
# [1] es para que se tome el segundo número de la lista por ejemplo si el usuario ingreso 1 y 2 se tomara el 2
# min es para que se tome el número menor de los dos números que se ingresaron