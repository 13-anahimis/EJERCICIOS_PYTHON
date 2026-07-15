historial_clientes = []
historial_herramientas = []
historial_dias = []
historial_costos = []

def calcular_costo_dia(dia):
    if dia == 1:
        return 50
    else:
        return 2 * calcular_costo_dia(dia - 1)

def calcular_costo_total(dias):
    if dias == 1:
        return 50
    else:
        return calcular_costo_dia(dias) + calcular_costo_total(dias - 1)

def registrar_prestamo(cliente, herramienta, dias):
    costo = calcular_costo_total(dias)
    historial_clientes(cliente)
    historial_herramientas(herramienta)
    historial_dias(dias)
    historial_costos(costo)
    return costo

def mostrar_historial():
    if len(historial_clientes) == 0:
        return False
    else:
        for i in range(len(historial_clientes)):
            print("Cliente:", historial_clientes[i], "| Herramienta:", historial_herramientas[i], "| Dias:", historial_dias[i], "| Total: $", historial_costos[i])
        return True

def buscar_herramienta(nombre_herramienta):
    encontrado = False
    for i in range(len(historial_herramientas)):
        if historial_herramientas[i] == nombre_herramienta:
            print("Encontrado -> Cliente:", historial_clientes[i], "| Dias:", historial_dias[i], "| Total: $", historial_costos[i])
            encontrado = True
    if encontrado == False:
        print("La herramienta no fue prestada hoy.")
    return encontrado

# Menu 
def ejecutar_menu():
    print("~~~~ FERRETERIA - MENU PRINCIPAL ~~~~")
    print("1. Registrar prestamo y cobrar")
    print("2. Mostrar historial del dia")
    print("3. Buscar herramienta prestada")
    print("4. Salir del sistema")
    
    opcion = input("Seleccione una opcion: ")
    
    if opcion == "1":
        herramienta = input("Nombre de la herramienta: ")
        dias = int(input("Dias de prestamo: "))
        total = registrar_prestamo(herramienta, dias)
        print("Cobro realizado con exito. Total a pagar: $", total)
        return ejecutar_menu()
        
    elif opcion == "2":
        print("~~~~ HISTORIAL DE PRESTAMOS ~~~~")
        exito = mostrar_historial()
        if exito == False:
            print("No hay registros en el historial todavia.")
        return ejecutar_menu()
        
    elif opcion == "3":
        herramienta_buscar = input("Ingrese el nombre de la herramienta a buscar: ")
        buscar_herramienta(herramienta_buscar)
        return ejecutar_menu()
        
    elif opcion == "4":
        print("Cerrando el sistema. Buen dia!")
    else:
        print("Opcion invalida. Intente de nuevo.")
        return ejecutar_menu()
