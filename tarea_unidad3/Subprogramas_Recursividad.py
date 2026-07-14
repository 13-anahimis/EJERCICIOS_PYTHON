OPC_POTENCIA = 1
OPC_SUMA_ACUMULADA = 2
OPC_FACTORIAL = 3
OPC_REPORTE = 4
OPC_SALIR = 5
OPC_SUMA_DIGITOS = 6

# Historial de operaciones 
historial = []

def potencia(base: int, exponente: int) -> int:
    if exponente == 0:
        return 1  # Caso base:
    else:
        return base * potencia(base, exponente - 1)  # Caso recursivo

def suma_acumulada(n: int) -> int:
    if n == 1:
        return 1  # Caso base
    else:
        return n + suma_acumulada(n - 1)  # Caso recursivo

def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1  # Caso base: factorial
    else:
        return n * factorial(n - 1)  # Caso recursivo

def suma_digitos(n: int) -> int:
    if n < 10:
        return n  # Caso base
    else:
        return (n % 10) + suma_digitos(n // 10)

def reporte():
    print("\n=== Reporte de la sesión ===")
    if len(historial) == 0:
        print("No hay operaciones registradas aún.")
        return
    
    print("-" * 65)
    for op in historial:
        print(f"{op['num']:<5}{op['tipo']:<20}{op['datos']:<25}{op['resultado']:<15}")
    print("-" * 65)
    
    cont_pot = 0
    cont_suma_ac = 0
    cont_fact = 0
    cont_digitos = 0
    
    for op in historial:
        if op['tipo'] == "Potencia":
            cont_pot += 1
        elif op['tipo'] == "Suma acumulada":
            cont_suma_ac += 1
        elif op['tipo'] == "Factorial":
            cont_fact += 1
        elif op['tipo'] == "Suma de dígitos":
            cont_digitos += 1
            
    print(f"Potencias calculadas:           {cont_pot}")
    print(f"Sumas acumuladas calculadas:    {cont_suma_ac}")
    print(f"Factoriales calculados:         {cont_fact}")
    print(f"Sumas de dígitos calculadas:    {cont_digitos}")
    print(f"Total de operaciones:           {len(historial)}")

def mostrar_menu():
    print("\n--- Menú principal ---")
    print(f"{OPC_POTENCIA}. Calcular potencia")
    print(f"{OPC_SUMA_ACUMULADA}. Calcular suma acumulada")
    print(f"{OPC_FACTORIAL}. Calcular factorial")
    print(f"{OPC_REPORTE}. Ver reporte de la sesión")
    print(f"{OPC_SALIR}. Salir")
    print(f"{OPC_SUMA_DIGITOS}. Calcular suma de dígitos")

def main():
    num_operacion = 0
    
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Elige una opción: "))
        except ValueError:
            print("Error: opción inválida. Ingresa un número entero.")
            continue

        if opcion == OPC_POTENCIA:
            try:
                base = int(input("Base: "))
                exponente = int(input("Exponente: "))
                if exponente < 0:
                    print("Error: el exponente no puede ser negativo.")
                    continue
                resultado = potencia(base, exponente)
                print(f"Resultado: {base}^{exponente} = {resultado}")
                num_operacion += 1
                historial.append({"num": num_operacion, "tipo": "Potencia", "datos": f"base={base}, exp={exponente}", "resultado": resultado})
            except ValueError:
                print("Error: Ingresa datos numéricos válidos.")

        elif opcion == OPC_SUMA_ACUMULADA:
            try:
                n = int(input("Número: "))
                if n <= 0:
                    print("Error: el número debe ser entero positivo mayor a cero.")
                    continue
                resultado = suma_acumulada(n)
                print(f"Resultado: suma(1..{n}) = {resultado}")
                num_operacion += 1
                historial.append({"num": num_operacion, "tipo": "Suma acumulada", "datos": f"n={n}", "resultado": resultado})
            except ValueError:
                print("Error: Debe ser un número entero.")

        elif opcion == OPC_FACTORIAL:
            while True:
                try:
                    n = int(input("Número: "))
                    if n < 0:
                        print("Error: el número debe ser mayor o igual a 0.")
                        continue
                    break
                except ValueError:
                    print("Error: Debe ser un número entero.")
            resultado = factorial(n)
            print(f"Resultado: {n}! = {resultado}")
            num_operacion += 1
            historial.append({"num": num_operacion, "tipo": "Factorial", "datos": f"n={n}", "resultado": resultado})

        elif opcion == OPC_REPORTE:
            reporte()

        elif opcion == OPC_SUMA_DIGITOS:
            try:
                n = int(input("Número: "))
                if n <= 0:
                    print("Error: el número debe ser positivo.")
                    continue
                resultado = suma_digitos(n)
                print(f"Resultado: suma dígitos({n}) = {resultado}")
                num_operacion += 1
                historial.append({"num": num_operacion, "tipo": "Suma de dígitos", "datos": f"n={n}", "resultado": resultado})
            except ValueError:
                print("Error: Debe ser un número entero.")

        elif opcion == OPC_SALIR:
            print("Gracias por usar el sistema. ¡Hasta pronto!")
            break

        else:
            print("Error: opción inválida.")

# Ejecutar programa de forma segura
if __name__ == "__main__":
    main()