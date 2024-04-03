# https://www.codeabbey.com/index/task_view/maximum-of-array     

lista = input("Ingrese los números separados por un espacio: ").split(" ")

lista = list(map(int, lista))
lista.sort()
print(f"{lista[-1]} {lista[0]}")

# en este caso estamos usando los index para encontrar el número mayor y menor de la lista
# el index [0] es para encontrar el número menor
# el index [-1] es para encontrar el número mayor

# el sort es para ordenar los números de menor a mayor
# para usar el index pedimos la lista de los números y el index que queremos usar

# tambien hay otra forma usando la función min y max si quiere lo consulta

