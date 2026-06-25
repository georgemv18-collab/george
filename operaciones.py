def mostrar_menu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Agregar producto")
    print("2. Buscar producto")
    print("3. Eliminar producto")
    print("4. Actualizar estado")
    print("5. Mostrar registros")
    print("6. Salir")
    print("====================================")

def leer_opcion():
    opcion = 0
    while opcion < 1 or opcion > 6:
        try:
            opcion = int(input("Seleccione una opción (1-6): "))
            if opcion < 1 or opcion > 6:
                print("Error: la opción debe estar entre 1 y 6.")
        except ValueError:
            print("Error: debe ingresar un número entero.")
            
    return opcion

# ==========================================
# FUNCIONES DE VALIDACIÓN (RETORNAN BOOLEANO)
# ==========================================

def validar_nombre(valor):
    return valor.strip() != ""

def validar_stock(valor):
    return 0 <= valor <= 500

def validar_precio(valor):
    return valor > 0

# ==========================================
# FUNCIONES DE OPERACIONES DEL SISTEMA
# ==========================================

def agregar_producto(productos):
    nombre = input("Nombre del producto: ")
    
    try:
        stock = int(input("Cantidad en stock (0-500): "))
        precio = int(input("Precio del producto: "))
    except ValueError:
        print("Error: los datos numéricos no tienen el formato esperado.")
        return

    if not validar_nombre(nombre):
        print("Error: No puede estar vacío ni compuesto solo por espacios.")
    elif not validar_stock(stock):
        print("Error: Debe ser un número entero entre 0 y 500.")
    elif not validar_precio(precio):
        print("Error: Debe ser un número mayor que cero.")
    else:
        nuevo_producto = {
            "nombre": nombre.strip(),
            "stock": stock,
            "precio": precio,
            "reposicion": False
        }
        productos.append(nuevo_producto)
        print("Producto agregado correctamente.")

def buscar_producto(productos, dato_busqueda):
    posicion = -1
    i = 0
    
    while i < len(productos) and posicion == -1:
        if productos[i]["nombre"] == dato_busqueda:
            posicion = i
        i += 1
        
    return posicion

def eliminar_producto(productos):
    dato_busqueda = input("Ingrese el nombre del producto a eliminar: ").strip()
    posicion = buscar_producto(productos, dato_busqueda)
    
    if posicion != -1:
        productos.pop(posicion)
        print("Producto eliminado correctamente.")
    else:
        print(f"El registro '{dato_busqueda}' no se encuentra registrado.")

def actualizar_estado(productos):
    for producto in productos:
        if producto["stock"] <= 5:
            producto["reposicion"] = True
        else:
            producto["reposicion"] = False

def mostrar_productos(productos):
    actualizar_estado(productos)
    print("=== LISTA DE PRODUCTOS ===")
    
    if len(productos) == 0:
        print("No hay registros para mostrar.")
    else:
        for producto in productos:
            print(f"Nombre del producto: {producto['nombre']}")
            print(f"Cantidad en stock: {producto['stock']}")
            print(f"Precio: {producto['precio']}")
            if producto["reposicion"]:
                print("Estado: NECESITA REPOSICIÓN")
            else:
                print("Estado: SUFICIENTE")
            print("************************************")