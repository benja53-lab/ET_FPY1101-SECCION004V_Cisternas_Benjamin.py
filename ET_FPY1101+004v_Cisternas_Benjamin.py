
#linhk de repositorio    ///    https://github.com/benja53-lab/ET_FPY1101-SECCION004V_Cisternas_Benjamin.py.git




stock = {
    '8475HD': [387990, 10], '2175HD': [327990, 4], 'JjfFHD': [424990, 1],
    'fgdxFHD': [664990, 21], '123FHD': [290890, 32], '342FHD': [444990, 7],
    'GF75HD': [749990, 2], 'UWU131HD': [349990, 1], 'FS1230HD': [249990, 0]
}

producto = {
    '8475HD': 'HP', '2175HD': 'Lenovo', 'JjfFHD': 'Dell',
    'fgdxFHD': 'Asus', '123FHD': 'Lenovo', '342FHD': 'HP',
    'GF75HD': 'MSI', 'UWU131HD': 'Dell', 'FS1230HD': 'Acer'
}

def stock_por_marca(marca):
    total = sum(cantidad for modelo, (precio, cantidad) in stock.items()
                if producto.get(modelo, '').lower() == marca.lower())
    print(f"Stock total de {marca.title()}: {total}")

def buscar_por_precio(min_precio, max_precio):
    resultados = [f"{producto[modelo]}--{modelo}"
                  for modelo, (precio, cantidad) in stock.items()
                  if min_precio <= precio <= max_precio and cantidad > 0]
    
    if resultados:
        print("Notebook en rango de precio:", sorted(resultados))
    else:
        print("No hay notebooks en ese rango de precios.")

def actualizar_precio(modelo, nuevo_precio):
    if modelo in stock:
        stock[modelo][0] = nuevo_precio
        print("Precio actualizado.")
    else:
        print("Modelo no encontrado.")

def main():
    while True:
        print("\n--- MENÚ ---")
        print("1. Ver stock por marca")
        print("2. Buscar por rango de precio")
        print("3. Actualizar precio de modelo")
        print("4. Salir")

        opcion = input("Opción: ")

        if opcion == '1':
            marca = input("Marca: ")
            stock_por_marca(marca)

        elif opcion == '2':
            try:
                p_min = int(input("Precio mínimo: "))
                p_max = int(input("Precio máximo: "))
                buscar_por_precio(p_min, p_max)
            except ValueError:
                print("Ingrese valores numéricos válidos")

        elif opcion == '3':
            modelo = input("Modelo: ")
            try:
                nuevo_precio = int(input("Nuevo precio: "))
                actualizar_precio(modelo, nuevo_precio)
            except ValueError:
                print("Ingrese un precio válido")

        elif opcion == '4':
            print("no vemos!!")
            break
        else:
            print("Opción no válida.")

main()
