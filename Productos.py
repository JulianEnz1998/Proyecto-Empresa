import os.path
import os
import random
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
    
lista=["Arroz", "Frijoles", "Pan", "Leche", "Queso", "Yogur", "Mantequilla", "Huevo", "Carne de res", "Pollo", "Pescado", "Mariscos", "Tocino", "Salchicha", "Jamón", "Atún", "Salmón", "Anchoas", "Aceitunas", "Tomate", "Pepino", "Lechuga", "Zanahoria", "Brócoli", "Coliflor", "Espinaca", "Pimiento", "Cebolla", "Ajo", "Patata", "Batata", "Calabaza", "Calabacín", "Berenjena", "Maíz", "Guisantes", "Fresas", "Frambuesas", "Arándanos", "Manzanas", "Plátanos", "Naranjas", "Limones", "Uvas", "Melón", "Sandía", "Piña", "Mango", "Papaya", "Kiwi", "Aguacate", "Aceite de oliva", "Aceite vegetal", "Vinagre", "Salsa de tomate", "Salsa de soja", "Mostaza", "Ketchup", "Mayonesa", "Miel", "Azúcar", "Sal", "Pimienta", "Hierbas frescas", "Especias molidas", "Harina de trigo", "Harina de maíz", "Levadura", "Azúcar moreno", "Arroz integral", "Harina integral", "Pasta", "Cereales", "Pan rallado", "Galletas", "Barritas energéticas", "Frutos secos", "Semillas", "Pasas", "Dátiles", "Chocolate negro", "Chocolate con leche", "Chocolate blanco", "Cacao en polvo", "Café", "Té", "Leche condensada", "Crema", "Helado", "Yogur helado", "Refrescos", "Jugos", "Agua mineral", "Vino tinto", "Vino blanco", "Cerveza", "Sidra", "Whisky", "Vodka", "Ron"]

def carga(Archivostock):
    print("INSERTAR PRODUCTOS A CARGAR:")
    cod=0
    for x in lista:   
        cod=cod+1
        descripcion=x
        descripcion=descripcion.ljust(20," ")
        precio=round(random.uniform(0, 1000))
        stock=random.randint(1,100)
        y=Producto(cod, descripcion, stock, precio)
        Archivostock.seek(0,2)
        pickle.dump(y, Archivostock)
        print("Cargado")

def listadoprod (Archivostock, rutastock):
    Archivostock.seek(0,0)
    tam=os.path.getsize(rutastock)    
    while Archivostock.tell() < tam:
        x=pickle.load(Archivostock)
        print(f"{x.getcod()} \t{x.getdesc()} \t{x.getstock()}")

def aperturastock():
    global rutastock
    rutastock="..\TP FINAL\\Stock.dat"
    global Archivostock
    if os.path.exists(rutastock):
        Archivostock=open(rutastock, "r+b") 
    else:
        Archivostock=open(rutastock, "w+b")

aperturastock()

carga(Archivostock)
listadoprod(Archivostock, rutastock)
Archivostock.close
input()