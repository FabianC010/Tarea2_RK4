import numpy as np

def rk4(oper, state, h):
    """Calcula el estado y_n+1 con el metodo rk4

    Args:
        oper (numpy array): Es el operador lineal dado por una matriz 2x2 [[0 1][1 0]]
        state (numpy array): Es el estado actual de la evolucion temporal a partir de la condicion inicial de la matrix 2x2 [[1 0][0 0]]
        h (float): Es el incremento temporal donde se evalua
    
    Examples:
        >>> rk4(np.array([[0, 1], [1, 0]]),np.array([[1, 0], [0, 0]]),1/99)
        np.array([[0.0756005+0.j , 0.+0.26427933j]
        [0.       -0.26427933j, 0.9243995+0.j        ]])    



    Return:
        numpy array: Devuelve el siguiente estado temporal, a utilizar en la siguiente iteracion.
    """
    k_1= func(oper,state)
    k_2= func(oper, state+k_1/2)
    k_3= func(oper, state+k_2/2)
    k_4= func(oper, state+k_3)
    return state +1/6 * h*(k_1 + 2*k_2 + 2*k_3 + k_4)

oOper = np.array([[0, 1], [1, 0]])
yInit = np.array([[1, 0], [0, 0]])
