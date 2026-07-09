from producto import Producto
from cliente import Cliente

def ejecutar():
    print("--- Iniciando Sistema del Taller ---")
    
    # Usando el código del Estudiante 1
    mi_producto = Producto(1, "Laptop Gamer", 1500)
    print(mi_producto.mostrar_detalle())
    
    # Usando el código del Estudiante 2
    mi_cliente = Cliente(101, "Jordy", "jordy@correo.com")
    print(mi_cliente.mostrar_informacion())
    print(mi_cliente.realizar_compra(mi_producto.nombre))
    
    print("✔ Ejecución exitosa.")

if __name__ == "__main__":
    ejecutar()