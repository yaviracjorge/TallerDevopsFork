class Producto:
    def __init__(self, id_producto, nombre, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio

    def calcular_descuento(self, porcentaje_descuento):
        descuento = self.precio * (porcentaje_descuento / 100)
        precio_final = self.precio - descuento
        return precio_final

    def mostrar_detalle(self):
        return f"Producto: {self.nombre} | Precio original: ${self.precio}"