def buscarProducto(productos, buscado):
    for producto in productos:
        if producto.lower() == buscado.lower():
            return True
    return False


productos = []

for i in range(5):
    producto = input(f"Ingrese el producto {i+1}: ")
    productos.append(producto)

buscado = input("Ingrese el producto a buscar: ")

if buscarProducto(productos, buscado):
    print("Producto encontrado")
else:
    print("Producto no encontrado")
