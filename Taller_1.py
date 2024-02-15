import numpy as np

class Vectores:
    def __init__(self, x, y, z):
        
        self.componentes = np.array([x, y, z])

    def Imprimir(self, nombre):
        self.nombre = nombre
        print(f"Vector {self.nombre}:  {self.componentes}")
    
    def SumaV(self, vector):
        op = self.componentes + vector.componentes
        return Vectores(*self.componentes + vector.componentes)
    def RestaV(self, vector):
        return Vectores(*self.componentes - vector.componentes)
    
    def Division(self, vector):
        return Vectores(*self.componentes / vector.componentes)
    
    def ProductoC(self, vector):
        op = np.cross(self.componentes, vector.componentes)
        return Vectores(*op)
    
    def ProductoP(self, vector):
        return np.dot(self.componentes, vector.componentes)

class Matrices:
    def __init__(self, componentes):
        
        self.componentes = np.array(componentes)

    def ImprimirM(self, nombre):
        self.nombre = nombre
        print(f"Matriz {self.nombre}:\n{self.componentes}")

    def SumaM(self, matriz):
        op = self.componentes + matriz.componentes
        return Matrices(op)
    
    def RestaM(self, matriz):
        op = self.componentes - matriz.componentes
        return Matrices(op)
    
    def DivisionM(self, matriz):
        op = self.componentes / matriz.componentes
        return Matrices(op)
    
    def ProductoCm(self, matriz):
        op = np.cross(self.componentes, matriz.componentes)
        return Matrices(op)
    
    def ProductoPm(self, matriz):
        return np.dot(self.componentes, matriz.componentes)

vector3 = Vectores(1, 2, 3)
vector4 = Vectores(4, 5, 6)

matriz1 = Matrices([[1, 2], [6, 3]])
matriz2 = Matrices([[4, 1], [0, 5]])

Resultado_sumav = vector3.SumaV(vector4)
Resultado_restav = vector3.RestaV(vector4)
Resultado_divisionv = vector3.Division(vector4)
Resultado_cruzv = vector3.ProductoC(vector4)
Resultado_puntov = vector3.ProductoP(vector4)

Resultado_sumam = matriz1.SumaM(matriz2)
Resultado_restam = matriz1.RestaM(matriz2)
Resultado_divisionm = matriz1.DivisionM(matriz2)
Resultado_cruzm = matriz1.ProductoCm(matriz2)
Resultado_puntom = matriz1.ProductoPm(matriz2)

vector3.Imprimir("1")
vector4.Imprimir("2")
Resultado_sumav.Imprimir("suma")
Resultado_restav.Imprimir("resta")
Resultado_divisionv.Imprimir("división")
Resultado_cruzv.Imprimir("Producto cruz")
print(f"Producto punto:  {Resultado_puntov}")

matriz1.ImprimirM("1")
matriz2.ImprimirM("2")
Resultado_sumam.ImprimirM("suma")
Resultado_restam.ImprimirM("resta")
Resultado_divisionm.ImprimirM("división")
Resultado_cruzm.ImprimirM("producto cruz")
print(f"Producto punto:\n{Resultado_puntom}")