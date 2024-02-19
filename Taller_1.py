import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

class Vectores:
    def __init__(self, x, y, z):
        
        self.componentes = np.array([x, y, z])

    def Imprimir(self, nombre):
        self.nombre = nombre
        print(f"Vector {self.nombre}:  {self.componentes}")
    # Suma de vectores
    def SumaV(self, vector):
        return Vectores(*self.componentes + vector.componentes)
    # Resta de vectores
    def RestaV(self, vector):
        return Vectores(*self.componentes - vector.componentes)
    # División de vectores
    def Division(self, vector):
        return Vectores(*self.componentes / vector.componentes)
    # Producto cruz
    def ProductoC(self, vector):
        op = np.cross(self.componentes, vector.componentes)
        return Vectores(*op)
    # Producto punto
    def ProductoP(self, vector):
        return np.dot(self.componentes, vector.componentes)
    
class ResultadoV():
    
    def suma():
        Resultado_sumav = vector1.SumaV(vector2)
        Resultado_sumav.Imprimir("suma")

    def resta():
        Resultado_restav = vector1.RestaV(vector2)
        Resultado_restav.Imprimir("resta")

    def division():
        Resultado_divisionv = vector1.Division(vector2)
        Resultado_divisionv.Imprimir("división")

    def punto():
        Resultado_puntov = vector1.ProductoP(vector2)
        print(f"Producto punto:  {Resultado_puntov}")

    def cruz():
        Resultado_cruzv = vector1.ProductoC(vector2)
        Resultado_cruzv.Imprimir("Producto cruz")

class Matrices:
    def __init__(self, componentes):
        
        self.componentes = np.array(componentes)

    def Imprimir(self, nombre):
        self.nombre = nombre
        print(f"Matriz {self.nombre}:\n{self.componentes}")
    # Suma de Matrices
    def Suma(self, matriz):
        op = self.componentes + matriz.componentes
        return Matrices(op)
    # Resta de matrices
    def Resta(self, matriz):
        op = self.componentes - matriz.componentes
        return Matrices(op)
    # División de matrices
    def Division(self, matriz):
        op = self.componentes / matriz.componentes
        return Matrices(op)
    # Producto cruz
    def ProductoC(self, matriz):
        op = np.cross(self.componentes, matriz.componentes)
        return Matrices(op)
    # Producto punto
    def ProductoP(self, matriz):
        return np.dot(self.componentes, matriz.componentes)
    
class ResultadoM():

    def suma():
        Resultado_suma = matriz1.Suma(matriz2)
        Resultado_suma.Imprimir("suma")

    def resta():
        Resultado_resta = matriz1.Resta(matriz2)
        Resultado_resta.Imprimir("resta")

    def division():
        Resultado_division = matriz1.Division(matriz2)
        Resultado_division.Imprimir("dicisión")
        
    def punto():
        Resultado_punto = matriz1.ProductoP(matriz2)
        print(f"Producto punto:\n{Resultado_punto}")

    def cruz():
        Resultado_cruz = matriz1.ProductoC(matriz2)
        Resultado_cruz.Imprimir("producto cruz")

class Imprimir():
    def Matriz():
        matriz1.Imprimir("1")
        matriz2.Imprimir("2")
        ResultadoM.suma()
        ResultadoM.resta()
        ResultadoM.division()
        ResultadoM.punto()
        ResultadoM.cruz()

    def Vector():
        vector1.Imprimir("1")
        vector2.Imprimir("2")
        ResultadoV.suma()
        ResultadoV.resta()
        ResultadoV.division()
        ResultadoV.punto()
        ResultadoV.cruz()

class Temperatura():
# Ecuación de la resistencia de una PT100 según la norma IEC 60751
    def resistencia(temperatura):
        
        a = 3.908e-3
        b = -5.775e-7
        R0 = 100.0  # Resistencia a 0°C
        return R0 * (1 + a * temperatura + b * temperatura**2)

class FuncionTransferencia():
        
        def __init__(self, numerdador, denomnador):
            self.numerador = numerdador
            self.denominador = denomnador
     
        def graficar_respuesta_al_escalon(self):
            sistema = signal.TransferFunction(self.numerador, self.denominador)
            tiempo, respuesta = signal.step(sistema)

            # Determinar el tipo de sistema
            num, den = signal.zpk2tf(*signal.tf2zpk(self.numerador, self.denominador))
            poles = np.roots(den)

            if len(poles) > 0 and np.isreal(poles[0]):
                damping_ratio = -np.real(poles[0]) / np.abs(poles[0])

                if damping_ratio < 1:
                    tipo_sistema = 'Sistema subamortiguado'
                elif damping_ratio == 1:
                    tipo_sistema = 'Sistema críticamente amortiguado'
                else:
                    tipo_sistema = 'Sistema sobreamortiguado'
            else:
                tipo_sistema = 'No se puede determinar el tipo de sistema'

            # Graficar la respuesta al escalón
            plt.plot(tiempo, respuesta)
            plt.title('Respuesta al Escalón')
            plt.xlabel('Tiempo')
            plt.ylabel('Respuesta')
            plt.grid(True)
            plt.show()
            print(tipo_sistema)

class Graficar():

    def Temperatura():

        # Crear datos para graficar
        temperaturas = np.linspace(-200, 200, 400)  # 400 puntos equidistantes en el rango [-200°C, 200°C]
        resistencias = Temperatura.resistencia(temperaturas)

        # Crear el gráfico
        plt.plot(temperaturas, resistencias, label='PT100')

        # Personalizar el gráfico
        plt.title('Comportamiento de una PT100')
        plt.xlabel('Temperatura (°C)')
        plt.ylabel('Resistencia (Ohm)')
        plt.legend()  # Mostrar leyenda
        
        # Mostrar el gráfico
        plt.grid(True)  # Agregar una cuadrícula
        plt.show()
    
    def FuncionTransferencia():
        # Solicitar al usuario los coeficientes
            numerador = [float(coeff) for coeff in input("Ingrese los coeficientes del numerador (separados por espacios): ").split()]
            denominador = [float(coeff) for coeff in input("Ingrese los coeficientes del denominador (separados por espacios): ").split()]

            # Graficar la respuesta al escalón y determinar el tipo de sistema
            Datos = FuncionTransferencia(numerador, denominador)
            Datos.graficar_respuesta_al_escalon()


# Vectores previamente inicializados
vector1 = Vectores(1, 2, 3)
vector2 = Vectores(4, 5, 6)
# Matrices previamente inicializadas
matriz1 = Matrices([[1, 2], [3, 4]])
matriz2 = Matrices([[5, 6], [7, 8]])
#Imprimiendo valores de vectores
#Imprimir.Vector()

#Imprimiendo valores de matrices
#Imprimir.Matriz()

#Graficar sensor PT100 desd -200°C a 200°C
#Graficar.Temperatura()

#Graficar función de transferencia de sugundo orden
#Graficar.FuncionTransferencia()


def carga_descarga(voltaje, capacitancia, resistencia, tiempo):
    """
    Calcula el voltaje a través del tiempo para la carga y descarga de un circuito RC.

    Parámetros:
    - voltaje: Voltaje inicial en el capacitor (V).
    - capacitancia: Valor de la capacitancia del capacitor (μF).
    - resistencia: Valor de la resistencia (Ω).
    - tiempo: Lista de valores de tiempo para evaluar la función.

    Retorna:
    - Lista de valores de voltaje a través del tiempo.
    """
    tau = resistencia * capacitancia  # Constante de tiempo del circuito RC
    carga_descarga = voltaje * (1 - np.exp(-tiempo / tau))
    return carga_descarga

def graficar_carga_descarga(voltaje, capacitancia, resistencia, tiempo):
    """
    Grafica la carga y descarga de un circuito RC.

    Parámetros:
    - voltaje: Voltaje inicial en el capacitor (V).
    - capacitancia: Valor de la capacitancia del capacitor (μF).
    - resistencia: Valor de la resistencia (Ω).
    - tiempo: Lista de valores de tiempo para evaluar la función.
    """
    voltajes = carga_descarga(voltaje, capacitancia, resistencia, tiempo)

    plt.plot(tiempo, voltajes)
    plt.title('Carga y Descarga de un Circuito RC')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Voltaje (V)')
    plt.grid(True)
    plt.legend(['Carga y Descarga'])
    plt.show()

if __name__ == "__main__":
    # Solicitar al usuario los valores
    voltaje = float(input("Ingrese el voltaje inicial en el capacitor (V): "))
    capacitancia = float(input("Ingrese el valor de la capacitancia del capacitor (μF): "))
    resistencia = float(input("Ingrese el valor de la resistencia (Ω): "))

    # Crear una lista de valores de tiempo
    tiempo = np.linspace(0, 5 * resistencia * capacitancia, 1000)

    # Graficar carga y descarga del circuito RC
    graficar_carga_descarga(voltaje, capacitancia, resistencia, tiempo)

