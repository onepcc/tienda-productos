#A continuación, crea una clase de Producto que tenga 3 atributos: 
# un nombre, un precio y una categoría. 
# Todo esto debe proporcionarse en el momento de la creación.
import logging
logging.basicConfig(filename='tienda.txt', filemode='a', format='%(asctime)s ---> %(message)s',datefmt='%d-%m-%Y %H:%M:%S')

class Productos:
    def __init__(self, nombre,categoria,precio=0):
        self.nombre=nombre
        self.precio=precio
        self.categoria=categoria
    
    # def __str__(self):
    #     """ Informacion de producto """
    #     return f"Producto: {self.nombre} Precio: ${self.precio} Categoria: {self.categoria}" 

    def printlog(self,mensaje):
        """Print y Log txt"""
        print(f"{mensaje}")
        logging.warning(f"{mensaje}") 

    def print_info (self) : #imprime el nombre del producto, su categoría y su precio.
            self.printlog(f"Producto: {self.nombre} Precio: ${self.precio} Categoria: {self.categoria}")
            # print(f"Producto: {self.nombre} Precio: ${self.precio} Categoria: {self.categoria}")
            return self
    
    def update_price(self, percent_change, is_increased = True):
        """actualiza el precio del producto. Si is_increased es True, el precio debería aumentar en el porcentaje de cambio proporcionado. 
        Si es False, el precio debe disminuir en el cambio porcentual proporcionado."""
        flag = bool (is_increased)
        if flag:
            self.precio += self.precio*(percent_change)/100
        else:
            self.precio -= self.precio*(percent_change)/100
        return self

if __name__ == "__main__":
    chocolate = Productos("Chocolate","Golosina", 500)
    lays = Productos("Lays","Golosina", 2000)
    ramitas = Productos("Ramitas","Golosina", 200)

    ron = Productos("Ron","Alcohol", 5000)
    cerveza = Productos("Ceveza","Alcohol", 1000)
    vino = Productos("Vino","Alcohol", 2500)
