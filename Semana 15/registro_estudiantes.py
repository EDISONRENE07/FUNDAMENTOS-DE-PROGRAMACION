# Programa: Registro de nombres de estudiantes usando una lista

estudiantes = []

while True:
    print("\n===== REGISTRO DE ESTUDIANTES =====")
    print("1. Agregar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Buscar estudiante")
    print("4. Eliminar estudiante")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del estudiante: ")
        estudiantes.append(nombre)
        print("Estudiante agregado correctamente.")

    elif opcion == "2":
        if len(estudiantes) == 0:
            print("No hay estudiantes registrados.")
        else:
            print("\nLista de estudiantes:")
            for i, estudiante in enumerate(estudiantes, start=1):
                print(f"{i}. {estudiante}")

    elif opcion == "3":
        nombre = input("Ingrese el nombre a buscar: ")

        if nombre in estudiantes:
            print(f"El estudiante {nombre} está registrado.")
        else:
            print("El estudiante no se encuentra en la lista.")

    elif opcion == "4":
        nombre = input("Ingrese el nombre del estudiante a eliminar: ")

        if nombre in estudiantes:
            estudiantes.remove(nombre)
            print("Estudiante eliminado correctamente.")
        else:
            print("El estudiante no existe.")

    elif opcion == "5":
        print("Programa finalizado.")
        break

    else:
        print("Opción inválida. Intente nuevamente.")
