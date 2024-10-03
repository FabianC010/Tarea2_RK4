# Metodo de Runge-Kutta de orden 4 (RK4)

Para un problema de valor inicial dinamico de como el siguiente:

\begin{gather}
    \frac{dy}{dt}=f(t,y)\\
    y_0=t_o
\end{gather}


se puede utilizar el metodo de RK4 para obtener la evolucion temporal que tiene este problema de valor inicial.
En nuestro caso utilizaremos la siguiente funcion para analizar

\begin{gather}
f(t, \mathbf{y}) = -i [O, \mathbf{y}(t)],
\end{gather}
