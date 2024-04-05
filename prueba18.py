# https://www.codeabbey.com/index/task_view/vowel-count

vocales = ['a', 'e', 'i', 'o', 'u', 'y']

tamano = int(input("Ingrese el tamaño de la lista: "))
resultado = []

for i in range(tamano):
    palabra = input()
    contador = 0
    for letra in palabra:
        if letra in vocales:
            contador += 1
    resultado.append(contador)

print(" ".join(map(str, resultado)))