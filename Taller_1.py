import numpy as np
import math
import random
import cv2
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

class Coordenadas:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def a_cilindricas(self):
        r = math.sqrt(self.x ** 2 + self.y ** 2)
        theta = math.atan2(self.y, self.x)
        z_cilindrica = self.z
        return r, theta, z_cilindrica
    
    def a_esfericas(self):
        r = math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
        theta = math.atan2(self.y, self.x)
        phi = math.atan2(math.sqrt(self.x ** 2 + self.y ** 2), self.z)
        return r, theta, phi

class CilindroNeumatico:
    def __init__(self, diametro, presion):
        self.diametro = diametro
        self.presion = presion
    
    def calcular_fuerza_avance(self):
        area_piston = (self.diametro / 2) ** 2 * math.pi
        fuerza_avance = area_piston * self.presion
        return fuerza_avance
    
    def calcular_fuerza_retroceso(self):
        area_piston = (self.diametro / 2) ** 2 * math.pi
        area_vastago = (self.diametro / 4) ** 2 * math.pi  # Área del vástago es la mitad del área del pistón
        area_efectiva = area_piston - area_vastago
        fuerza_retroceso = area_efectiva * self.presion
        return fuerza_retroceso

class IteracionConsola():

    def Potencia():

        I, V = float(input("Ingrese el valor de la corriente: ")), float(input("Ingrese el valor del voltaje: "))

        P = I * V
        print(f"La potencia que consume el circuito es: {P} W")

    def Aleatorios():

        x = int(input("Cantidad de numeros a generar\nCantidad: "))
        min, max = int(input("Rango minímo: ")), int(input("Rango máximo: "))

        for _ in range(x):
            #print("Números aleatorios generados:")
            print(f"Número generado: {random.randint(min, max)}")

    def Volumenes():

        r = "s"
        while r != "n":

            opc = input("Seleccione para calcular el volumen\n1. Prisma\n2. Pirámide\n3. Cono truncado\n4. Cilindro\nSolido: ")

            if opc == "1" or opc == "prisma" or opc == "2" or opc == "piramide":
                b,a = float(input("Ingrese el valor de la base: ")), float(input("Ingrese el valor de la altura: "))

                if opc == "1" or opc == "prisma" :
                    v = b * a
                    print(f"El volumen del solido prisma es: {v:.2f}")

                if opc == "2" or opc == "piramide" :
                    v = (1/3) * b * a
                    print(f"El volumen de la pirámide es: {v:.2f}")

            if opc == "3" or opc == "cono truncado" or opc == "4" or opc == "cilindro":

                r, a = float(input("Ingrese el valor del radio: ")), float(input("Ingrese el valor de la altura: "))

                if opc == "3" or opc == "cono truncado" :

                    r2 = float(input("Ingrese el radio menor del cono truncado: "))
                    v = (math.pi * a / 3) * (r*2 + r2*2 + (r * r2))
                    print(f"El volumen del cono truncado es: {v:.2f}")

                if opc == "4" or opc == "cilindro":

                    v = math.pi * r**2 * a
                    print(f"El volumen del cilindro es: {v:.2f}")

            if opc != "1" or opc != "2" or opc == "3" or opc != "4" :
                if opc != "prisma" or opc != "piramide" or opc == "cono truncado" or opc != "cilindro" :

                    print("\nNo escogiste ningún solido")
            
            r = input("\n¿Quieres volver a escoger un solido? (s/n):  ")

            if r != "s" and r != "n":

                while r != "n" and r != "s":

                    r = input("\nla letra ingresada no es (s) o (n): ")

    def Robot():

        r = "s"
        while r != "n":

            robot = input("Seleccione el robot\n1. Cilíndrico\n2. Cartesiano\n3. Esférico\nRobot: ")

            if robot == "cilindrico" or robot == "1":
                print("\nRobot cilíndrico\nTiene tres articulaciones")
            
            elif robot == "cartesiano" or robot == "2":
                print("\nRobot cartesiano\nTiene tres articulaciones")

            elif robot == "esferico" or robot == "3":
                print("\nRobot esférico\nTiene dos articulaciones")

            else:
                print("No has escogido ningun robot.")

            r = input("\n¿Quiere escoger otro robot? (s/n):  ")

            if r != "s" and r != "n":

                while r != "n" and r != "s":

                    r = input("\nla letra ingresada no es (s) o (n): ")
                
    def Continuar():

        c = "s"
        while c != "n":

            c = input("¿Desea continuar? (s/n): ")
            if c != "s" and c != "n":
                print("la letra ingresada no es (s) o (n)")

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

    def Coordenadas():

        r_cilindrica, theta_cilindrica, z_cilindrica = coordenadas.a_cilindricas()
        r_esferica, theta_esferica, phi_esferica = coordenadas.a_esfericas()
        print(f"Coordenadas rectangulares: {(x, y, z)}\nCoordenadas cilíndricas: {(r_cilindrica, theta_cilindrica, z_cilindrica)}\nCoordenadas esféricas: {(r_esferica, theta_esferica, phi_esferica)}")

    def RTD():

        def calcular_resistencia(temperatura):
         # Coeficientes de la ecuación de Callendar-Van Dusen
            A = 3.9083e-3
            B = -5.775e-7
            R0 = 100.0  # Resistencia nominal a 0°C
    
            # Cálculo de la resistencia
            R = R0 * (1 + A * temperatura + B * temperatura**2)
            return R

        # Temperatura en grados Celsius
        temperatura = 25.0

        # Calcular la resistencia para la temperatura dada
        resistencia = calcular_resistencia(temperatura)

        print(f"Para una temperatura de {temperatura}°C, la resistencia es de {resistencia:.2f} ohms.")

    def Rotaciones():

        def rectangular_a_cilindricas(x, y, z):
            r = math.sqrt(x**2 + y**2)  # Calcula la distancia radial desde el origen al punto en el plano XY
            theta = math.atan2(y, x)     # Calcula el ángulo en el plano XY (en radianes)
            z_cilindrica = z             # La coordenada z en el sistema cilíndrico es la misma que en el sistema rectangular
            return r, theta, z_cilindrica

        # Función para convertir coordenadas rectangulares a coordenadas esféricas
        def rectangular_a_esfericas(x, y, z):
            r = math.sqrt(x**2 + y**2 + z**2)  # Calcula la distancia radial desde el origen al punto
            theta = math.atan2(y, x)           # Calcula el ángulo en el plano XY (en radianes)
            phi = math.acos(z / r)             # Calcula el ángulo entre el eje z y la línea que conecta el origen con el punto (en radianes)
            return r, theta, phi

        # Coordenadas rectangulares
        x = 1
        y = 1
        z = 1

        # Convertir coordenadas rectangulares a cilíndricas
        r_cilindrica, theta_cilindrica, z_cilindrica = rectangular_a_cilindricas(x, y, z)

        # Convertir coordenadas rectangulares a esféricas
        r_esferica, theta_esferica, phi_esferica = rectangular_a_esfericas(x, y, z)

        print(f"Coordenadas rectangulares (x, y, z): ({x}, {y}, {z})")
        print(f"Coordenadas cilíndricas (r, theta, z): ({r_cilindrica}, {theta_cilindrica}, {z_cilindrica})")
        print(f"Coordenadas esféricas (r, theta, phi): ({r_esferica}, {theta_esferica}, {phi_esferica})")

    def Fuerza():

        # Dimensiones físicas del cilindro (en metros)
        diametro = 0.05  # 50 mm

        # Valor de presión (en Pascals)
        presion = 500000  # 500 kPa

        # Crear instancia del cilindro con las dimensiones y presión especificadas
        cilindro = CilindroNeumatico(diametro, presion)

        # Calcular fuerza de avance
        fuerza_avance = cilindro.calcular_fuerza_avance()

        # Calcular fuerza de retroceso
        fuerza_retroceso = cilindro.calcular_fuerza_retroceso()

        print(f"Fuerza de avance del cilindro: {fuerza_avance} N")
        print(f"Fuerza de retroceso del cilindro: {fuerza_retroceso} N")

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

class CargaDescarga():

    def carga(voltaje, capacitancia, resistencia, tiempo):
        tau = resistencia * capacitancia
        carga = voltaje * (1 - np.exp(-tiempo / tau))
        return tiempo, carga

    def descarga(voltaje, capacitancia, resistencia, tiempo):
        tau = resistencia * capacitancia
        descarga = voltaje * np.exp(-tiempo / tau)
        return tiempo, descarga

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

    def CargaDescarga():

        def Grafica(voltaje, capacitancia, resistencia, tiempo):
            tiempo_carga, voltajes_carga = CargaDescarga.carga(voltaje, capacitancia, resistencia, tiempo)
            tiempo_descarga, voltajes_descarga = CargaDescarga.descarga(voltaje, capacitancia, resistencia, tiempo)

            plt.plot(tiempo_carga, voltajes_carga, label='Carga')
            plt.plot(tiempo_descarga, voltajes_descarga, label='Descarga')
            plt.title('Carga y Descarga de un Circuito RC')
            plt.xlabel('Tiempo (s)')
            plt.ylabel('Voltaje (V)')
            plt.grid(True)
            plt.legend()
            plt.show()

        voltaje = float(input("Ingrese el voltaje inicial en el capacitor (V): "))
        capacitancia = float(input("Ingrese el valor de la capacitancia del capacitor (μF): "))
        resistencia = float(input("Ingrese el valor de la resistencia (Ω): "))

        tiempo = np.linspace(0, 10 * resistencia * capacitancia, 1000)

        # Modifica aquí para que solo haya una llamada a la función
        Grafica(voltaje, capacitancia, resistencia, tiempo)

    def Vectores():

        def dibujar_vector(x, y, z):
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.quiver(0, 0, 0, x, y, z, color='b', label='Vector')
    
            # Configurar ejes
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')
            ax.set_xlim([0, max(x, 1)])  # Asegurarse de que los límites mínimos sean 1
            ax.set_ylim([0, max(y, 1)])
            ax.set_zlim([0, max(z, 1)])
            # Mostrar la leyenda
            ax.legend()
            plt.show()

        # Solicitar al usuario las coordenadas del vector
        x = float(input("Ingrese la coordenada X del vector: "))
        y = float(input("Ingrese la coordenada Y del vector: "))
        z = float(input("Ingrese la coordenada Z del vector: "))

        # Dibujar el vector en el sistema de coordenadas tridimensional
        dibujar_vector(x, y, z)

    def Imagen():

        #imagen = cv2.imread('/home/juansebastiantorres/Documentos/Estudio/Robotica/Laboratorios/Robotica/chevrolet.png')
        imagen = cv2.imread('/home/juansebastiantorres/Documentos/Estudio/Robotica/Laboratorios/Robotica/Kia.png')
        gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        ret, th = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)

        contornos, jerarquia = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        mostrar_imagen = True

        for i, contorno in enumerate(contornos):
            cv2.drawContours(imagen, [contorno], -1, (0, 255, 0), 3)
    
            # Mostrar las coordenadas de todos los puntos del contorno
            for punto in contorno:
                x, y = punto[0]
                cv2.putText(imagen, f'({x}, {y})', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255, 255, 255), 1)
    
            cv2.imshow('imagen', imagen)
    
            while True:
                key = cv2.waitKey(1)
                if key == ord('q'):  # Presiona 'q' para salir del bucle
                    mostrar_imagen = False
                    break
                elif key == ord('n'):  # Presiona 'n' para ir al siguiente contorno
                    break
    
            if not mostrar_imagen:
                break

        cv2.imshow('th', th)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def Nombres(): 

        # Definir los puntos para cada letra
        letra_S = [[7, 0], [1+7, 0], [1+7, 0.5], [7, 0.5], [7, 1], [8, 1]]
        letra_e = [[3+7, 0], [2+7, 0], [2+7, 0.5], [3+7, 0.5], [2+7, 0.5],[2+7, 1],[3+7, 1]]
        letra_r = [[4+7, 0], [4+7, 1], [5+7, 1], [5+7, 0.5], [4+7, 0.5],[5+7, 0]]
        letra_g = [[7+7, 1], [6+7, 1], [6+7, 0], [7+7, 0], [7+7, 0.5], [6+7, 0.5]]
        letra_i = [[8+7, 0], [8+7, 1]]
        letra_o = [[9+7, 0], [9+7, 1], [11+7, 1], [11+7, 0], [9+7, 0]]

        letra_J = [[20, 1], [21, 1], [20.5, 1], [20.5, 0], [20, 0]]
        letra_U = [[22, 1], [22, 0], [23, 0], [23, 1]]
        letra_A = [[24, 0], [24, 1], [25, 1], [25, 0], [25, 0.5],[24, 0.5]]
        letra_N = [[26, 0], [26, 1], [27, 0], [27, 1]]

        letra_C = [[30, 0], [29, 0], [29, 1], [30, 1]]
        letra_A1 = [[31, 0], [31, 1], [32, 1], [32, 0], [32, 0.5],[31, 0.5]]
        letra_M = [[33, 0], [33, 1], [33.5, 0.7], [34, 1], [34, 0]]
        letra_I1 = [[35, 0], [35, 1]]
        letra_L = [[36, 1], [36, 0], [37, 0]]
        letra_o1 = [[38, 0], [38, 1], [39, 1], [39, 0], [38, 0]]


        # Unir los puntos de cada letra
        for letra in [letra_S, letra_e, letra_r, letra_g, letra_i, letra_o, letra_J,letra_U, letra_A, letra_N,letra_C,letra_A1, letra_M, letra_I1, letra_o1,letra_L]:
            x = [punto[0] for punto in letra]
            y = [punto[1] for punto in letra]
            plt.plot(x, y, marker='o')

        # Configuraciones adicionales
        plt.title('Nombre "NOMBRES DEL GRUPO"')
        plt.grid(True)
        plt.show()      

# Vectores previamente inicializados
vector1 = Vectores(1, 2, 3)
vector2 = Vectores(4, 5, 6)
# Matrices previamente inicializadas
matriz1 = Matrices([[1, 2], [3, 4]])
matriz2 = Matrices([[5, 6], [7, 8]])
# Coordenadas rectangulares (x, y, z)
x = 3
y = 4
z = 5
coordenadas = Coordenadas(x, y, z)

#Descomentar la linea del ejercicio para ejecutarlos independientemente

# A. Sin iteración de consola

#Imprimir.Vector()              ##Punto 1
#Imprimir.Matriz()              ##Punto 2
#Imprimir.Coordenadas()         ##Punto 3
#Imprimir.RTD()                 ##Punto 4
#Imprimir.Rotaciones()          ##Punto 5
#Imprimir.Fuerza()              ##Punto 6


# B. Con iteración de consola

#IteracionConsola.Potencia()        ##Punto 1
#IteracionConsola.Aleatorios()      ##Punto 2
#IteracionConsola.Volumenes()       ##Punto 3
#IteracionConsola.Robot()           ##Punto 4
#IteracionConsola.Continuar()       ##Punto 5


# Uso de funsiones para gráficar

#Graficar.Temperatura()             ##Punto 1
#Graficar.FuncionTransferencia()    ##Punto 2
#Graficar.CargaDescarga()           ##Punto 3
#Graficar.Vectores()                ##Punto 4
#Graficar.Nombres()                 ##Punto 5
#Graficar.Imagen()                  ##Punto 6 para graficar, hay que descomentar la imagen que se quiera graficar