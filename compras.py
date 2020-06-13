
from datetime import datetime

class compras:
    def __init__(self, c_cliente,):
        self.cliente = c_cliente
        self.producto = []
        self.precio = []



    def saludar(self):
        print("--------------------------------------------------")
        return ("******Bienvenido {} que compra desea realizar****".format(self.cliente))

    def articulo(self):
        reg_producto = input("¿Qué producto desea comprar?:  ")
        reg_precio = int(input("precio del producto:  "))
        self.producto.append(reg_producto)
        self.precio.append(reg_precio)
        otro = input("Desea adquirir otro producto si/no: ")
        if(otro == "si"):
            self.articulo()
        elif(otro == "no"):
            print("----------------------------------")
            print ( "Su compra se realizó con éxito")
            hoy = datetime.now()
            fecha = hoy.strftime("%d-%m-%Y  %H-%M-%S")
            print(f"     {fecha}")
            print ("   ****Lista de artículos****")
            print("Artículo", "Precio", sep="\t")
            for i in range(len(self.producto)):
                print(f"{self.producto[i]}          {self.precio[i]}")
            print("****Total a pagar****")
            suma = 0
            for i in range(len(self.precio)):
                suma = suma + self.precio[i]
            print (f"        {suma} bs")
            print("----------------------------------")
            print("     Gracias por su compra")
            print("----------------------------------")


    def menu(self):
        productos = """
           Menu de compras
           
        1.- Añadir producto
        2.- volver
        
                    """
        print(productos)
        comprar = int(input('¿Que operacion desea realizar?: '))
        if(comprar == 1):
            print(self.articulo())
            self.menu()
        elif(comprar == 2):
            print(self.saludar())
            self.menu()
        else:
            print("Escoja una opcion")
            self.menu()

cliente = compras("Estimado cliente")



print(cliente.saludar())
print(cliente.menu())