nombre_cliente = input("Ingrese el nombre del cliente: ")
nombre_producto = input("Ingrese el nombre del producto: ")
cantidad_productos = int(input ("Ingresa el total de productos comprados: "))
precio_unitario = float (input ("Ingresa el precio unitario: "))

IVA = 0.16 
DESCUENTO = 0.10

subtotal = precio_unitario * cantidad_productos
cantidad_descuento= subtotal *DESCUENTO
#base para calcular el iva
el_descuento = subtotal - cantidad_descuento
#para calcular iva
precio_iva = el_descuento * IVA
tota_pago= el_descuento + precio_iva

print("~"*50)
print("                  TICKET DE COMPRA     ")
print("~"*50)
print("/n")
print (f"Cliente:   {nombre_cliente}")
print(f"Producto:   { nombre_producto }")
print(f"Cantidad de producto:  {cantidad_productos  } ")
print(f"Precio unitario:   ${precio_unitario:.2}")
print("-"*50)
print(f"El subtotal es de:                        ${subtotal:.2f}")
print(f"El descuento es de (10%):                 -${cantidad_descuento:.2f}")
print(f"El iva es de (16%):                       ${precio_iva:.2f}")
print(f"Cantida de producto:                      {cantidad_productos } pzas.")
print("-"*50)
print("~"*50)
print(f"El precio total es de:                    ${tota_pago:.2f}")
print("~"*50)
print("-"*50)
print("           GRACIAS POR SU PREFERENCIA             ")
print("-"*50)
#demostracion de datos
print("      Demostracion de datos      ")
print(f"*Variable 'nombre_cliente': {type(nombre_cliente)}")
print(f"*Variable 'nombre_producto': {type(nombre_producto)}")
print(f"*Variable 'cantidad_productos': {type(cantidad_productos)}")
print(f"*Variable 'precio_unitario': {type(precio_unitario)}")