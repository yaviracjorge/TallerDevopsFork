class Cliente:
    def __init__(self, id_cliente, nombre, correo):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.correo = correo

    def mostrar_informacion(self):
        return f"Cliente: {self.nombre} | Correo: {self.correo}"

    def realizar_compra(self, nombre_producto):
        return f"El cliente {self.nombre} ha registrado la compra de: {nombre_producto}"