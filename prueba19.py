# https://www.codeabbey.com/index/task_view/collatz-sequence
def collatz(n):
    pasos = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        pasos += 1
    return pasos

tamaño = int(input("Ingrese el tamaño de la lista: "))
lista = list(map(int, input().split()))

resultado = [collatz(n) for n in lista]

print(" ".join(map(str, resultado)))
