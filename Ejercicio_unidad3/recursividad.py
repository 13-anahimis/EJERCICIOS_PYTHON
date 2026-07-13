#la recursividad es cuando una funcion se llama a sí misma para resolver un problema, dividiéndolo en una versión más pequeña del mismo problema, hasta llegar a un punto tan simple que ya no necesita dividirse más.

def contar_sinlimite (numero):
    print(numero)
    #contar_sinlimite(numero + 1) #Se llama a si mismp siempre
    #NO HAY NINGUNA CONDICION QUE DETENGA ESTO
    
contar_sinlimite (1)

def factorial_interativo(n):
    resultado=1
    for i in range(1, n+1):
        resultado= resultado * i
    return resultado

print(f"Factorial interativo de 5:{factorial_interativo(5)}")

# caso base= condicion que detiene la recurcion. sin el, la funcion se llamaria infinitamente
#caso recursivio= donde la funcion se llama a si misma con un problema mas pequeño, acercandose al caso base

def factorial_recursiva(n):
    if n == 0 or n ==1: #CASO BASE
        return 1
    else: #CASO RECURSIVO
        return n * factorial_recursiva(n-1)
print (f"Factorial recursivo de 5: {factorial_recursiva(5)}")

#CARACTERISTICAS DE LOS PROCESOS RECURSIVOS
#Pila de llamada (call stack)

def factorial_visual (n, nivel=0):
    sangria= "  " * nivel
    print (f"{sangria}<- entrando con n={n}")
    
    if n == 0 or n== 1:
        print(f"{sangria}<-caso base, regresa 1")
        return 1
    else:
        resultado=n * factorial_visual (n-1, nivel+1)
        print(f"{sangria}<- resgresa {resultado} (n={n})")
        return resultado
    
factorial_visual(4)    

def fibonacci (n):
    if n ==0: #caso base 1
        return 0
    elif n==1: #caso base 2
        return 1
    else: #caso recursivo
        return fibonacci (n-1)+ fibonacci (n-2)
    
for i in range(10):
    print(f"fibonacci({i})={fibonacci(i)}") 
    
    