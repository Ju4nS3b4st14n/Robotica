import matplotlib.pyplot as plt 


class Nombres():
        
    def Letras():
        # Definir los puntos para cada letra
        letra_A = [[0, 0], [0, 5], [2, 5], [2, 0], [2, 2.5],[0, 2.5]]
        letra_B = [[0, 0], [0, 5], [2, 5], [2, 2.5], [0, 2.5],[2, 2.5],[2,0],[0,0]]
        letra_C = [[2, 0], [0, 0], [0, 5], [2, 5]]
        letra_D = [[0, 0], [0, 5], [2, 5], [2, 0], [0, 0]]
        letra_E = [[2, 0], [0, 0], [0, 2.5], [1, 2.5],[0,2.5],[0,5],[2,5]]
        letra_F = [[0, 0], [0, 2.5], [1, 2.5],[0,2.5],[0,5],[2,5]]
        letra_G = [[1, 2.5], [2, 2.5], [2, 0], [0, 0],[0,5],[2,5]]
        letra_H = [[0, 0], [0, 5], [0, 2.5], [2, 2.5],[2,5],[2,0]]
        letra_I = [[0, 0], [2, 0], [1, 0], [1, 5],[0,5],[2,5]]
        letra_J = [[0, 2.5], [0, 0], [1, 0], [1, 5],[0,5],[2,5]]
        letra_K = [[0, 0], [0, 5], [0, 2.5], [2, 5],[0,2.5],[2,0]]
        letra_L = [[0, 5], [0, 0], [2, 0]]
        letra_M = [[0, 0], [0, 5], [1, 2.5], [2, 5],[2,5],[2,0]]
        letra_N = [[0, 0], [0, 5], [2, 0], [2, 5]]
        letra_O = [[0, 0], [0, 5], [2, 5], [2, 0], [0, 0]]
        letra_P = [[0, 0], [0, 5], [2, 5], [2, 2.5], [0, 2.5]]
        letra_Q = [[0, 0], [0, 5], [2, 5], [2, 0], [0, 0], [2, 0],[1,2.5],[2,0]]#arreglar
        letra_R = [[0, 0], [0, 5], [2, 5], [2, 2.5], [0, 2.5], [2, 0]]
        letra_S = [[0,0],[2, 0], [2, 2.5], [0, 2.5], [0, 5], [2, 5]]
        letra_T = [[1, 0], [1, 5], [0, 5], [2, 5]]
        letra_U = [[0, 5], [0, 0], [2, 0], [2, 5]]
        letra_V = [[0, 5], [1, 0], [2, 5]]
        letra_W = [[0, 5], [0, 0], [1, 2.5], [2, 0], [2, 5]]
        letra_X = [[0, 0], [2, 5], [1, 2.5], [0, 5], [2, 0]]
        letra_Y = [[0, 5], [1, 2.5], [2, 5], [1, 2.5], [1, 0]]
        letra_Z = [[2, 0], [0, 0], [2, 5], [0, 5]]

        # Combinar las letras en un diccionario
        letras = {
            'A': letra_A,'B': letra_B,'C': letra_C,'D': letra_D,'E': letra_E,'F': letra_F,'G': letra_G,'H': letra_H,'I': letra_I,'J': letra_J,'K': letra_K,'L': letra_L,
            'M': letra_M,'N': letra_N,'O': letra_O,'P': letra_P,'Q': letra_Q,'R': letra_R,'S': letra_S,'T': letra_T,'U': letra_U,'V': letra_V,'W': letra_W,'X': letra_X,
            'Y': letra_Y,'Z': letra_Z
        }

        # Unir los puntos de cada letra
        for letra in [letra_Z,letra_Z,letra_Z]:
            x = [punto[0] for punto in letra]
            y = [punto[1] for punto in letra]
            plt.plot(x, y, marker='o')

        # Configuraciones adicionales
        plt.title('Nombre "NOMBRES DEL GRUPO"')
        plt.grid(True)
        plt.show()

Nombres.Letras()