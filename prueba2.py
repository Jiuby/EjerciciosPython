# https://www.codeabbey.com/index/task_view/sum-in-loop

longitud = int(input("Introduce la longitud de la lista: "))
cadena = input("Inserte los números separados por un espacio: ")

lista = list(map(int, cadena.split()))

if len(lista) != longitud:
    print("La longitud de la lista no coincide con el número introducido")

print(sum(lista))

# longitud es la cantidad de números que se van a sumar
# cadena es la lista de números que se van a sumar
# lista es la lista de números que se van a sumar
# map es para que los números ingresados sean enteros
# int es para que los números ingresados sean enteros se coloca el int ya que el map requiere una función
# split es para separar los números que se ingresan

# if es para que si la longitud de la lista no coincide con el número introducido muestre un mensaje

# print es para mostrar el resultado de la suma de los números que se ingresaron
# sum es para sumar los números que se ingresaron

# Python tiene bastantes funciones asi que se pueden hacer muchas cosas con el