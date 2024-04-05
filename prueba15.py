# https://www.codeabbey.com/index/task_view/average-of-array

lista = []

tamano = int(input("Ingrese el tamaño de la lista: "))

for i in range(tamano):
    numeros = input().split()
    numeros = list(map(int, numeros))
    if numeros[-1] == 0:
        numeros.pop()
    resultado = sum(numeros) / len(numeros)
    lista.append(int(resultado + 0.5))  # Redondea al entero más cercano

print(' '.join(map(str, lista)))