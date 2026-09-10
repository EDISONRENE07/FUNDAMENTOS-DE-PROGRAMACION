# Programa con matriz 3x3
matriz = [
     [2, 4, 6],
     [1, 3, 5],
     [7, 8, 9]
     ]

for i in range(3):
    fila = ""
    for j in range(3):
        fila = fila + str(matriz[i][j]) + " "

    print(fila)
        
