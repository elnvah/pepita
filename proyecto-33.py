print("===REGISTRO DE CLIENTE=")
nombre_user = input("ingrese el nombre del usuario")
edad_user = input("ingrese edad del usuario ")
correo_user = input("ingrese sus correo ")


print("===REGISTRO DE PRODUCTO===")
nombre_producto = input("ingrese le nombre del producto: ")
sku = input("ingrese sku: ")
ano_fabricacion = int(input("ingrese año de la fabricacion"))
cantidad = int(input("ingrese una cantidad"))

ano_actual = 2026
vida_util = ano_fabricacion - ano_actual

print("===ENTREGA DE INFORMACION===")
print(f"el nombre del cliente es: {nombre_user}")
print(f"la edad del cliente es:{edad_user}")
print(f"el correo del cliente del user es: {correo_user}")
print (f"el nombre del producto es: {nombre_producto}")
print (f"el sku es : {sku}")
print (f"año de fabricacion: {ano_fabricacion}")
print (f"la cantidad es: {cantidad}")
print (f"la vida del producto es:"{vida_util})