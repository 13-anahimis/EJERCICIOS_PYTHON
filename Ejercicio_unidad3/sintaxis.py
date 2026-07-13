#sintaxis de una FUNCION
#Encabezado - def nombre_funcion(parametros): - define el nombre y que recibe
#Cuerpo - las lineas de codigo indentadas que ejecutan la logica de una funcion
#parametros - los datos que la funcion recibe para trabajo (pueden ser cer, uno o varios)
#tetorno - la sentencia return valor que entrega el resultado de vuelta

def calcular_promedio(nota1, nota2, nota3, ): #encabezado de mi funcion
    suma= nota1 + nota2 + nota3 
    promedio= suma / 3
    return promedio

resultado = calcular_promedio(8.0,9.0,7.0)
print (f"promedio: {resultado:.2f}")

#Tu turno: Modifica la función para que reciba 4 calificaciones en lugar de 3, y ajusta el cálculo del promedio correctamente.
def calcular_promedio(nota1, nota2, nota3, nota4): #encabezado de mi funcion
    suma= nota1 + nota2 + nota3 + nota4
    promedio= suma / 4
    return promedio

resultado = calcular_promedio(8.0,9.0,7.0,6.0)
print (f"promedio: {resultado:.2f}")

def mostrar_bienvenida():
    print("==== Sistema de calificaciones====") #sin parametros
    
def calcular_iva(precio, tasa=0.16): #parametros con valor por defecto
    return precio*(1 + tasa)

mostrar_bienvenida()

total1= calcular_iva(100)
print(f"Total con iva por defecto: ${total1:.2f}") #usando valor por defecto por tasa

total2= calcular_iva (100,0.08) #especificando una tasa diferente
print(f"total con iva especial: ${total2:.2f}") 

#Tu turno: Escribe una función calcular_descuento(precio, porcentaje=10) que calcule el precio final con descuento. Pruébala una vez sin especificar el porcentaje y otra vez con un porcentaje distinto.

def calcular_descuento(precio, porcentaje=10):
    descuento = precio * (porcentaje / 100)
    precio_final = precio - descuento
    return precio_final

precio_con_descuento_defecto = calcular_descuento(500)
print(f"Precio con descuento por defecto (10%): ${precio_con_descuento_defecto:.2f}")

precio_con_descuento_especial = calcular_descuento(500, 25)
print(f"Precio con descuento especial (25%): ${precio_con_descuento_especial:.2f}")

