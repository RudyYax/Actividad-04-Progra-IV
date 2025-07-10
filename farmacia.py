

print("Farmacia Menu")
print("1. Agregara medicamentos a la pila")
print("2. Entregar mediacamentos")
print("3. Mostrar")
print("4. Salir")
opcion = input("Ingrese su opción ")
pila_medicamentos = []
if opcion == "1":
    medicamento = input("Ingrese el medicamento a agregar: ")
    pila_medicamentos.append(medicamento)
    print(f"{medicamento} ingresado corectamente")

elif