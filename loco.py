from operaciones import *

productos = []
continuar = True

while continuar:
    mostrar_menu()
    opcion = leer_opcion()
    
    if opcion == 1:
        agregar_producto(productos)
    elif opcion == 2:
        dato_busqueda = input("Ingrese el nombre del producto a buscar: ").strip()
        posicion = buscar_producto(productos, dato_busqueda)
        
        if posicion != -1:
            print("Registro encontrado:")
            print(productos[posicion])
        else:
            print("No se encontró el registro solicitado.")
    elif opcion == 3:
        eliminar_producto(productos)
    elif opcion == 4:
        actualizar_estado(productos)
        print("Estados actualizados correctamente.")
    elif opcion == 5:
        mostrar_productos(productos)
    else:
        continuar = False

print("Gracias por usar el sistema de inventario. Vuelva pronto.")