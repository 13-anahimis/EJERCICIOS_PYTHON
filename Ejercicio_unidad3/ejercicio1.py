#que es un subprograma?
#un subprograma es un bloque de codigo independiente, con su propio nombre, que realiza una tarea especifica y puede ser invocado (llamado) desde cualquier parte del programa principal, las veces que necesite.

#funciones y procedimientos.
#funcion: subprograma que siempre regresa un valor al punto donde fue llamado, usando la sentencia return. se usa cuando necesitas un resultado para seguir trabajando con el.

#procedimiento: subprograma que realiza una accion (mostrar algo, modificar datos, guardar informacion), pero no necesariamente regresa un valor utilizable. se usa cuando el objetivo es ejecutar una tarea, no obtener un dato de vuelta.

#definicion de una funcion
#public static int suma(int a, int b){return a + b;}: java

#ejercicio 1: funcion vs procedimiento

def calcular_area_rectangulo(base, altura):
    area = base * altura
    # <- regresa un valor: es funcion

def mostrar_resultado(nombre, area):
    print(f"el area de {nombre} es {area} m2") #<- no regresa un valor: es procedimiento

    #uso de ambos subprogramas
    resultado = calcular_area_rectangulo(5, 10)
    mostrar_resultado("el terreno mide", resultado)

#esribe un procedimeinto llamado saludar (nombre) que imprima un saludo personalizado, y una funcion llamada es mayor_de_edad(edad) que regrese true o false. usa ambos en un mini programa.

def saludar(nombre):
    print(f"Hola, {nombre}! Bienvenido/a.")

def es_mayor_de_edad(edad):
    return edad >= 18

nombre_usuario = input("Ingresa tu nombre: ")
saludar(nombre_usuario) 
edad_usuario = int(input("Ingresa tu edad: "))
if es_mayor_de_edad(edad_usuario):
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

#ejerccicio2: el error de no usar return

def calcular_doble(numero):
    doble = numero * 2
    print(doble)

resultado = calcular_doble(10)
print(resultado)

#corrige el ejercicio2 para calcular_doble regrese el valor correctamente con return, y que sea el print(resultado) el que se encargue de mostrarlo
def calcular_doble(numero):
    doble = numero * 2
    return doble 
resultado = calcular_doble(10)  
print(resultado)