# ==============================
#  MÁQUINA EXPENDEDORA REAL
# ==============================

class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = float(precio)
        self.stock = int(stock)

    def __str__(self):
        return f"{self.codigo} - {self.nombre} | Precio: S/. {self.precio:.2f} | Stock: {self.stock}"

    def reducir_stock(self):
        if self.stock > 0:
            self.stock -= 1

class MaquinaExpendedora:
    def __init__(self, productos):
        self.productos = {p.codigo: p for p in productos}
        self.ventas = []

    def mostrar_productos(self):
        print("\n=== PRODUCTOS DISPONIBLES ===")
        for p in self.productos.values():
            print(p)

    def comprar(self, codigo, dinero):
        if codigo not in self.productos:
            print(" Código inválido.")
            return None

        producto = self.productos[codigo]
        if producto.stock <= 0:
            print(" Producto agotado.")
            return None

        if dinero < producto.precio:
            print(f" Dinero insuficiente. Precio: S/. {producto.precio:.2f}")
            return None

        cambio = dinero - producto.precio
        producto.reducir_stock()
        self.ventas.append([producto.codigo, producto.nombre, producto.precio])
        print(f" ¡Has comprado {producto.nombre}! Tu cambio es: S/. {cambio:.2f}")
        return producto

    def mostrar_ventas(self):
        print("\n=== REGISTRO DE VENTAS ===")
        if not self.ventas:
            print("Aún no hay ventas.")
        else:
            for v in self.ventas:
                print(f"{v[0]} - {v[1]} | S/. {v[2]:.2f}")


# --- Lista de productos ---
productos = [
    Producto("A1", "Doritos", 3.00, 8),
    Producto("A2", "Lays Clásicas", 3.20, 10),
    Producto("A3", "Cheetos", 3.00, 6),
    Producto("A4", "Inka Kola 500ml", 4.00, 5),
    Producto("A5", "Coca-Cola 500ml", 4.20, 7),
    Producto("A6", "Pepsi 500ml", 4.00, 6),
    Producto("A7", "Agua San Luis 600ml", 2.50, 12),
    Producto("A8", "Snickers", 3.80, 4),
    Producto("A9", "Sublime", 2.80, 10),
    Producto("B1", "Princesa", 2.50, 9),
    Producto("B2", "Choco Soda", 3.00, 8),
    Producto("B3", "Casino", 3.20, 6),
    Producto("B4", "Oreo", 3.50, 10),
    Producto("B5", "Trident Menta", 1.50, 15),
    Producto("B6", "Doña Pepa", 2.80, 7),
]

# --- Programa principal ---
maquina = MaquinaExpendedora(productos)

print(" Bienvenido a la Máquina Expendedora ")

while True:
    print("\n===== MENÚ =====")
    print("1. Ver productos")
    print("2. Comprar producto")
    print("3. Ver ventas")
    print("4. Salir")

    opcion = input(" Elige una opción: ")

    if opcion == "1":
        maquina.mostrar_productos()

    elif opcion == "2":
        codigo = input(" Ingresa el código del producto (ej: A1): ").upper()
        try:
            dinero = float(input(" Ingresa tu dinero (S/.): "))
        except ValueError:
            print(" Ingresa un número válido.")
            continue
        maquina.comprar(codigo, dinero)

    elif opcion == "3":
        maquina.mostrar_ventas()

    elif opcion == "4":
        print(" ¡Gracias por usar la máquina expendedora!")
        break

    else:
        print(" Opción inválida. Intenta otra vez.")