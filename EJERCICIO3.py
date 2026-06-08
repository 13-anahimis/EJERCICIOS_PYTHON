#indentificadores y variablas
#varuables con snake_case

#quiero obtener el combre de un alumno,¿como debo definir mi identificador?
nombre_alumno= "juan domingues"
edad_alumno= 28
promedio_final=9.5

#constante con screaming snake case
TASA_IVA= 0.16
#CALIFICACION_MINIMA= 7.0
PESO_PARCIAL= 0.20
PI= 3.1416
GRAVEDAD_PLANETA= 9.84
CAPACIDAD_MAXIMA_SALON=25

#tipado dinamico - la variable cambia de tipo
dato = 100
print (type(dato))
dato= "cien"
print(type(dato))

#uso de constante en un calculo
precio_base = 500
precio_final= precio_base* ( 1 + TASA_IVA)
print(f"precio con IVA:  $ {precio_final : .2f}")

#Define 3 constantes:PESO_PARCIAL=0.20, PESO_PROYECTO=0.40 y CALIFICACION_MINIMA=6.0. luego crea 4 variables con calificaciones y calcula el promedio usando las constantes.imprime si el alumno aprobo o reprobo
PESO_PROYECTO=0.40
CALIFICACION_MINIMA=6.0
parcial_1= 9.0
parcial_2=4.5
parcial_3=10.0
parcial_4=10.0
Calificacion_final = (parcial_1+parcial_2+parcial_3 + parcial_4)/ 4
#print ("La calificaion final es: " Calificacion_final "por ende")
print ("aprobabo" if Calificacion_final >= CALIFICACION_MINIMA else "reprobado")