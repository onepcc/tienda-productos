import logging
logging.basicConfig(filename='tienda.txt', filemode='a', format='%(asctime)s ---> %(message)s',datefmt='%d-%m-%Y %H:%M:%S')

# from productos import *

# t = Productos("daj","adsad",0)
# t.print_info()

class Tienda:		# Clase tienda 2 atributos un nombre y una lista de productos
    def __init__(self, name):
        self.nombre = name    
        self.productos = []
        # self.cuenta = CuentaBancaria(0.02,0) 
        # self.cuentas = {"ahorros":self.cuenta }
    
    def __str__(self):
        """ Informacion de Tienda """
        self.printlog(f"Tienda: {self.nombre} Productos: {self.productos}")
        return (f"Tienda: {self.nombre} Productos: {self.productos}")
    
    def prod_tienda(self):
        """ Informacion de todos los productos de la tienda"""
        self.printlog(f"Informacion de todos los productos de {self.nombre}")
        # print(f"Informacion de todos los productos de {self.nombre}")
        for producto in self.productos:
            producto.print_info()
        self.printlog("\n")
        # return self



    def add_product (self, new_product) : 
        """toma un producto y lo agrega a la tienda"""
        self.printlog(f"Se agrega nuevo producto {new_product.nombre.upper()} en {self.nombre.upper()}")
        self.productos.append(new_product)
        return self

    def sell_product (self, id):
        """elimina el producto de la lista de productos de la tienda dada la identificación (suponga que id es el índice del producto en la lista) 
        e imprima su información."""
        sell = self.productos.pop(id)
        self.printlog("Vendido-$$$-")
        # print("Vendido-$$$-",end="")
        sell.print_info()
        self.printlog("\n")
        # print("\n")
        return self

        # del self.productos.[id]
    def inflation(self, percent_increase ): 
        """Entero (%)
        Aumenta el precio de cada producto por el % dado """
        self.printlog(f"Aumento por IPC {percent_increase}%")
        # print(f"Aumento por IPC {percent_increase}%")
        for producto in self.productos:
            producto.update_price(percent_increase)
        return self
    
    def remate(self, categoria, porcentaje_descuento):
        """Entero (%)
        Descuento en el precio para la categoria dada por el % dado"""
        self.printlog(f"Remate descuento en {categoria} por {porcentaje_descuento}% ")
        # print(f"Remate descuento en {categoria} por {porcentaje_descuento}% ")
        for producto in self.productos:
            if producto.categoria == categoria:
                producto.update_price(porcentaje_descuento,False)
                producto.print_info()
        return self
    
    def printlog(self,mensaje):
        """Print y Log txt"""
        print(f"{mensaje}")
        logging.warning(f"{mensaje}")

    # def imprimelog(self,mensaje):
    #     "Imprime y loggea fuera de las clases"
    #     print(f"{self.nombre} - {mensaje}")
    #     self.printlog(f"{self.nombre} - {mensaje}")
    

    def muestraintereses(self):
        for cuenta in self.cuentas:
            if self.cuentas[cuenta].saldo > 0:
                self.cuentas[cuenta].intereses_ganados()
                print(f"""{self.name} - Intereses ganados en cuenta {cuenta} = $ {self.cuentas[cuenta].saldo*self.cuentas[cuenta].intereses}
*************************************************************************************""")
                self.printlog(f"""{self.name} - Intereses ganados en cuenta {cuenta} = $ {self.cuentas[cuenta].saldo*self.cuentas[cuenta].intereses}
*************************************************************************************""")
            else:
                print(f"{self.name} - cuenta {cuenta} No gano intereses")
                self.printlog(f"{self.name} - cuenta {cuenta} No gano intereses")
        return self

    