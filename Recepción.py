cola_Pacientes = []
opcion = 0
while(opcion != 5):
    print("Bienvenido a Recepcion")
    print("A continuacion presentare un breve menu puede seleccionar la opcion que desee")
    print("1.- Registrar un nuevo paciente")
    print("2.- Atender al paciente")
    print("3.- Mostrar pacientes en cola")
    print("4.- Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
            Paciente = input("Nombre del paciente que va registrar: ")
            cola_Pacientes.append(Paciente)
            print(f"el paciente {Paciente} se agrego a la cola")
    elif opcion == "2":
        if cola_Pacientes:
            Atendido = cola_Pacientes.pop(0)
            print(f"el paciente {Atendido} fue atendido con éxito")
        else:
            print("No se ha registrado ningún paciente")
    elif opcion == "3":
        if cola_Pacientes:
            print ("La cola Acutal de pacientes es de: ")
            for Paciente in cola_Pacientes:
                    print(Paciente)
        else:
            print("No hay ningun paciente")
    elif opcion == "4":
        print("Gracias por utilizar nuestro programa")
        break
    else:
        print("Opcion No encontrada o no valida.")



