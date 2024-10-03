def dyn_generator(oper, state):
    """Dinamica del problema

    Args:
        oper (numpy array): Es el operador lineal dado por una matriz 2x2 [[0 1][1 0]]
        state (numpy array): Es el estado actual de la evolucion temporal a partir de la condicion inicial de la matrix 2x2 [[1 0][0 0]]

    Examples:
        >>> func(np.array([[0, 1], [1, 0]]),np.array([[1, 0], [0, 0]]))
        -1.0j*np.array([[0, -1][1, 0]])

    Return:
        numpy array: Retorna la funcion dada por oper y state [A,B]= AB-BA multiplicado por "i" la constante compleja

    """
    return -1.0j *(np.dot(oper, state)-np.dot(state, oper))
