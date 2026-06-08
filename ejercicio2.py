#-Casting basico
#Implicita: int+ float =float automaticamente
resultado = 5 + 2.0
print(resultado)
print (type(resultado))

#Emplicita: str a int
texto_numero ="42"
numero_real =int (texto_numero)
print (numero_real + 8)

#Explicita: int a srt para concatenar
edad= 28
mensaje = "hola, soy juan y mi edad es " + str(edad)
print(mensaje)

#float a int
precio= 9.99
print(int(precio))

#simularemos input con variables fijas
dato_usuario = "25"
print(type(dato_usuario))
# print (dato_usuario + 5)
edad_correcta = int (dato_usuario)
print(edad_correcta + 5)
#patron correcto para entrada de datos:
edad =int (input("ingresa tu edad "))

#escribe un programa que pida al usuario su nombre (str) y su año de nacimiento (int). calcula e imprime su edad aproximada restando el año actual
nombre1= (input("ingresa tu nombre: "))
edad1 =(input("ingresa tu edad: "))
