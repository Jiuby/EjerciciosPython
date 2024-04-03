# https://www.codeabbey.com/index/task_view/sums-in-loop

Lista1 = []
Lista2 = []

resultado = []
tamano = int(input("Ingrese el tamaño de las listas: "))



for i in range(tamano):
    numeros = input("Ingrese un par de números separados por un espacio: ").split(" ")
    Lista1.append(int(numeros[0]))
    Lista2.append(int(numeros[1]))
    resultado.append(int(numeros[0]) + int(numeros[1]))

if len(Lista1) != tamano:
    print("La longitud de la lista1 no coincide con el número introducido")
elif len(Lista2) != tamano:
    print("La longitud de la lista2 no coincide con el número introducido")

print(' '.join(map(str, resultado)))

# Lista1 es la lista de los primeros números que se van a sumar
# Lista2 es la lista de los segundos números que se van a sumar

# resultado es la lista de los resultados de las sumas

# tamano es la cantidad de números que se van a sumar

# for es para que se repita el proceso de ingresar los números la cantidad de veces que se haya indicado en tamano

# numeros es la lista de los números que se van a sumar
# split es para separar los números que se ingresan
# append es para agregar los números a la lista
# int es para que los números ingresados sean enteros
# [0] es para que se tome el primer número de la lista por ejemplo si el usuario ingreso 1 y 2 se tomara el 1
# [1] es para que se tome el segundo número de la lista por ejemplo si el usuario ingreso 1 y 2 se tomara el 2

# la linea 13 es facil de explicar ya que estamos jugando con el input y el split para que se ingresen los números y se sumen

# el join es para agregar los resultados de la lista de resultados al print y el map es para que los resultados sean enteros

# para entender el map normalmente se usa con una función y en este caso se usa con int para que los resultados sean enteros y se use la variable resultado para que sus componentes sean enteros