# https://www.codeabbey.com/index/task_view/body-mass-index

def Body_index(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        return "under"
    elif bmi < 25.0:
        return "normal"
    elif bmi < 30.0:
        return "over"
    else:
        return "obese"

tamano = int(input("Ingrese cuantas personas se analizaran: "))

total = []

for i in range(tamano):
    numeros = input("Ingrese el peso y la altura separados por un espacio: ").split(" ")
    resultado = Body_index(int(numeros[0]), float(numeros[1]))
    total.append(resultado)

print(' '.join(map(str, total)))