import logging
logging.basicConfig(filename='tienda.txt', filemode='a', format='%(asctime)s ---> %(message)s',datefmt='%d-%m-%Y %H:%M:%S')

from clases.productos import Productos
from clases.tienda import Tienda

#Creamos unos productos de la clase Productos
chocolate = Productos("Chocolate","Golosina", 500)
lays = Productos("Lays","Golosina", 2000)
ramitas = Productos("Ramitas","Golosina", 200)

ron = Productos("Ron","Alcohol", 5000)
cerveza = Productos("Ceveza","Alcohol", 1000)
vino = Productos("Vino","Alcohol", 2500)

# chocolate.print_info()
# lays.print_info()
# ramitas.print_info()
# ron.print_info()

#Creamos una tienda de la clase Tienda y añadimos los productos
kmart = Tienda("Kmart")

kmart.add_product(chocolate)
kmart.add_product(lays)
kmart.add_product(ramitas)
kmart.add_product(ron)
kmart.add_product(cerveza)
kmart.add_product(vino)

# print(locals())
# print(kmart.productos)

kmart.prod_tienda()
kmart.sell_product(3)
kmart.prod_tienda()

#Inflacion
kmart.inflation(15)
kmart.prod_tienda()
kmart.remate("Alcohol",50)
