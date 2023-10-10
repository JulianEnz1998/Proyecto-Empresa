import os.path
import os
import pickle


class Producto:
    def __init__(self, codigo, descripcion, stock, precio):
        self.codigo=codigo
        self.descripcion=descripcion
        self.stock=stock
        self.precio=precio
    def getcod(self):
        return self.codigo
    def getdesc(self):
        return self.descripcion
    def getstock(self):
        return self.stock
    def getprecio(self):
        return self.precio
    def actualizar_stock(self, stockrestante):
        self.stock=stockrestante
        
        
class Pedido:
    def __init__(self, numpedido, codigoproducto, descripcionped, cantidad, importe):
        self.numpedido=numpedido
        self.codigoproducto=codigoproducto
        self.descripcionped=descripcionped
        self.cantidad=cantidad
        self.importe=importe
    def getnumped(self):
        return self.numpedido
    def getcodprod(self):
        return self.codigoproducto
    def getdescped(self):
        return self.descripcionped
    def getcant(self):
        return self.cantidad
    def getimp(self):
        return self.importe
    def actualizacionped(self, nuevocod, nuevadesc,nuevacant,nuevoimp):
        self.codigoproducto=nuevocod
        self.descripcionped=nuevadesc
        self.cantidad=nuevacant
        self.importe=nuevoimp
        
#Productos
def aperturastock():
    global rutastock
    rutastock="..\TP FINAL\\Stock.dat"
    global Archivostock
    if os.path.exists(rutastock):
        Archivostock=open(rutastock, "r+b") 
    else:
        Archivostock=open(rutastock, "w+b")
def listadoprod (Archivostock, rutastock):
    Archivostock.seek(0,0)
    tam=os.path.getsize(rutastock)    
    while Archivostock.tell() < tam:
        x=pickle.load(Archivostock)
        print(f"{x.getcod()} \t{x.getdesc()} \t{x.getstock()} \t{x.getprecio()}")
#Pedidos
def apertura():
    global ruta
    ruta="..\TP FINAL\\Pedidos.dat"
    global Archivo
    if os.path.exists(ruta):
        Archivo=open(ruta, "r+b") 
    else:
        Archivo=open(ruta, "w+b")
def carga_pedidos(Archivo, Archivostock, rutastock):
    while True:
        num_pedido=int(input("Inserte numero de pedido: "))
        codi_prod=int(input("Seleccione el codigo del producto a cargar (Codigos desde el 1 al 100): "))

        cant_prod=int(input("Inserte cuantos articulos del producto: "))
        Archivostock.seek(0,0)
        tam=os.path.getsize(rutastock)
        #
        while Archivostock.tell() < tam:
            pos=Archivostock.tell()
            x=pickle.load(Archivostock)       
            if x.getcod()==codi_prod:
                if x.getstock()>=cant_prod:
                    print("Cantidad de stock disponible",x.getstock())
                    print("Precio del producto", x.getprecio())
                    total_pedido=(cant_prod*x.getprecio())
                    print("Precio total del pedido",total_pedido)
                    stockrestante=x.getstock()-cant_prod
                    x.actualizar_stock(stockrestante)
                    Archivostock.seek(pos, 0)
                    pickle.dump(x, Archivostock)
                    Archivo.seek(0,2)
                    y=Pedido(num_pedido,codi_prod,x.getdesc(), cant_prod, total_pedido)
                    print("Se cargaron ", cant_prod, "unidades de ", x.getdesc())
                    pickle.dump(y, Archivo)
                    Archivo.flush()
                    Archivostock.flush()                    
                else:
                    print("STOCK INSUFICIENTE")
                    break                  
        seguir=input("Desea cargar otro pedido [s/n]:")
        seguir=seguir.lower()
        if seguir == "n":
            break
        
def modificacionped(Archivo, Archivostock, ruta, rutastock):
    codmod = int(input("Codigo pedido a modificar:"))
    nuevocod = int(input("Inserte codigo de producto nuevo: "))
    nuevacant = int(input("Inserte nueva cantidad: "))
    nuevoimp = 0
    Archivo.seek(0, 0)
    Archivostock.seek(0, 0)
    tam = os.path.getsize(ruta)
    tamstock = os.path.getsize(rutastock)
    while Archivo.tell() < tam:
        pos = Archivo.tell()
        x = pickle.load(Archivo)        
        if x.getnumped() == codmod:
            print("Numero de pedido valido")
            while Archivostock.tell() < tamstock:
                posstock = Archivostock.tell()
                y = pickle.load(Archivostock)
                if y.getcod() == x.getcodprod():
                    y.actualizar_stock(x.getcant() + y.getstock())
                    Archivostock.seek(posstock, 0)
                    pickle.dump(y, Archivostock)
                elif y.getcod() == nuevocod:
                    print("Precio del codigo nuevo", y.getprecio())
                    print("Cantidad nueva", nuevacant)
                    nuevoimp = y.getprecio() * nuevacant
                    print("Importe total nuevo", nuevoimp)
                    x.actualizacionped(nuevocod, y.getdesc(), nuevacant, nuevoimp)
                    stockrestante = y.getstock() - nuevacant
                    print("Stock restante del producto nuevo", stockrestante)
                    y.actualizar_stock(stockrestante)
            Archivo.seek(pos, 0)
            pickle.dump(x, Archivo)
    Archivo.flush()
    Archivostock.flush()


def listadoped(Archivo, ruta):
    Archivo.seek(0,0)
    tam=os.path.getsize(ruta)    
    print("")
    print("Listado de pedidos")
    while Archivo.tell() < tam:
        x=pickle.load(Archivo)
        print("")
        print("Numero de pedido: ", x.getnumped())
        print("Codigo del producto:", x.getcodprod())
        print("Producto: ", x.getdescped())
        print("Cantidad de unidades: ", x.getcant())
        print("Importe del final pedido: ", x.getimp())
        print("————————————————————————————————————")

    
def opcionesmenu():
    print("Menu opciones")
    print("1 - Carga de pedidos")
    print("2 - Listado de pedidos")
    print("3 - Modificar pedido")
    print("4 - Listar productos")
    print("5 - Salir")

def menu():
    while True:
        opcionesmenu()
        opc=int(input("Opcion de menu: "))
        if opc==1:
            carga_pedidos(Archivo, Archivostock, rutastock)
        elif opc==2:
            listadoped(Archivo, ruta)
        elif opc==3:
            modificacionped(Archivo, Archivostock, ruta, rutastock)
        elif opc==4:
            listadoprod (Archivostock, rutastock)
        elif opc==5:
            print ("Saliendo del menu")
            input()
            break
        else:
            print("Ninguna de las opciones fue valida, intente otra vez.")

global Archivo
global Archivostock
global ruta
global rutastock
apertura()
aperturastock()
menu()
input()
