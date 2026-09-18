# Función que calcula el promedio de tres notas
def calcular_promedio(nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3) / 3
    return promedio

# Entrada de datos
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

# Llamada a la función
resultado = calcular_promedio(nota1, nota2, nota3)

# Mostrar el resultado
print("El promedio de las tres notas es:", resultado)
