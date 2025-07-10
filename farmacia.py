

print("Farmacia Menu")
print("1. Agregara medicamentos a la pila")
print("2. Entregar mediacamentos")
print("3. Mostrar")
print("4. Salir")

pila_medicamentos = []

while True:
    opcion = input("Ingrese su opción: ")

    if opcion == "1":
        medicamento = input("Ingrese el medicamento a agregar: ")
        pila_medicamentos.append(medicamento)
        print(f"{medicamento} ingresado corectamente")

    elif opcion=="2":
        if pila_medicamentos:
            entregado = pila_medicamentos.pop()
            print(f"Medicamento entregado {entregado}")
        else:
            print("No hay elementos en la pila")

    elif opcion == "3":
        if pila_medicamentos:
            print(f"La pila actual de medicamentos es: ")
            for i in pila_medicamentos:
                print(f"-{i}")
        else:
            print("La pila esta vacia.")

    elif opcion==4:
        print("Saliendo del programa .")
        break






