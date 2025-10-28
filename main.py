# ==============================
#  MAQUINA EXPENDEDORA 
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
        self.total_dinero = 0.0  # total acumulado

    def mostrar_productos(self):
        print("\n=== PRODUCTOS DISPONIBLES ===")
        for p in self.productos.values():
            print(p)

    def comprar(self, codigo, dinero):
        if codigo not in self.productos:
            print("Código inválido.")
            return None

        producto = self.productos[codigo]
        if producto.stock <= 0:
            print("Producto agotado.")
            return None

        if dinero < producto.precio:
            print(f"Dinero insuficiente. Precio: S/. {producto.precio:.2f}")
            return None

        cambio = dinero - producto.precio
        producto.reducir_stock()
        self.ventas.append([producto.codigo, producto.nombre, producto.precio])
        self.total_dinero += producto.precio
        print(f"Has comprado {producto.nombre}. Tu cambio es: S/. {cambio:.2f}")
        return producto

    def mostrar_ventas(self):
        print("\n=== REGISTRO DE VENTAS ===")
        if not self.ventas:
            print("Aún no hay ventas.")
        else:
            for v in self.ventas:
                print(f"{v[0]} - {v[1]} | S/. {v[2]:.2f}")

            print(f"\nTOTAL RECAUDADO: S/. {self.total_dinero:.2f}")
            self.mostrar_dinero_detallado()

    def mostrar_dinero_detallado(self):
        print("\n=== DISTRIBUCION DE DINERO ===")

        total = round(self.total_dinero, 2)
        billetes_monedas = {
            "S/50": 0,
            "S/20": 0,
            "S/10": 0,
            "S/5": 0,
            "S/2": 0,
            "S/1": 0,
            "S/0.50": 0,
            "S/0.20": 0,
            "S/0.10": 0
        }
        for valor in [50, 20, 10, 5, 2, 1, 0.50, 0.20, 0.10]:
            while total >= valor:
                billetes_monedas[f"S/{valor:.2f}"] += 1
                total -= valor
                total = round(total, 2)

        for m, cantidad in billetes_monedas.items():
            if cantidad > 0:
                print(f"{m}: {cantidad} unidades")


productos = [
    Producto("A1", "Doritos", 3.00, 20),
    Producto("A2", "Lays Clasicas", 3.20, 20),
    Producto("A3", "Cheetos", 3.00, 20),
    Producto("A4", "Inka Kola 500ml", 4.00, 20),
    Producto("A5", "Coca-Cola 500ml", 4.20, 20),
    Producto("A6", "Pepsi 500ml", 4.00, 20),
    Producto("A7", "Agua San Luis 600ml", 2.50, 20),
    Producto("A8", "Snickers", 3.80, 20),
    Producto("A9", "Sublime", 2.80, 20),
    Producto("B1", "Princesa", 2.50, 20),
    Producto("B2", "Choco Soda", 3.00, 20),
    Producto("B3", "Casino", 3.20, 20),
    Producto("B4", "Oreo", 3.50, 20),
    Producto("B5", "Trident Menta", 1.50, 20),
    Producto("B6", "Doña Pepa", 2.80, 20),
]

maquina = MaquinaExpendedora(productos)

print("Bienvenido a la Maquina Expendedora")

while True:
    print("\n===== MENU =====")
    print("1. Ver productos")
    print("2. Comprar producto")
    print("3. Ver ventas y ganancias")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        maquina.mostrar_productos()

    elif opcion == "2":
        codigo = input("Ingresa el código del producto (ej: A1): ").upper()
        try:
            dinero = float(input("Ingresa tu dinero (S/.): "))
        except ValueError:
            print("Ingresa un número válido.")
            continue
        maquina.comprar(codigo, dinero)

    elif opcion == "3":
        maquina.mostrar_ventas()

    elif opcion == "4":
        print("Gracias por usar la maquina expendedora.")
        break

    else:
        print("Opción inválida. Intenta otra vez.")
