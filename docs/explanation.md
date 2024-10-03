
El metodo *RK4* nos permite analizar la evolucion temporal de un estado inical cualquiera, en nuesto caso es:
\begin{gather}
f(t, \mathbf{y}) = -i [O, \mathbf{y}(t)],
\end{gather}
Hay que tomar en cuenta que **no hay dependencia explicita** de la funcion *f(t,y)* con el tiempo.

- O es un operador lineal dado 
- i es la constante compleja
- y(t) es un estado que evoluciona con el tiempo

esta funcion lleva a cabo el producto del operador por el estado temporal, menos el producto del estado temporal por el operador:
\begin{gater}
[O, y(t)] = Oy(t) - y(t)O
\end{gather} 
Multiplicado por la constante compleja.

A partir de esta funcion podemos calcular con el metodo *RK4* esta evolucion temporal utilizando la siguiente ecuacion:

\begin{gather}
    y_{n+1} = y_n + \frac{1}{6} \left(k_1 + 2k_2 + 2k_3 + k_4\right) \\
    k_1 = h f(t_n, y_n) \\
    k_2 = h f\left(t_n + \frac{h}{2}, y_n + \frac{k_1}{2}\right) \\
    k_3 = h f\left(t_n + \frac{h}{2}, y_n + \frac{k_2}{2}\right) \\
    k_4 = h f\left(t_n + h, y_n + k_3\right)
\end{gather}

Donde:

- t_n es el operador lineal
- y_n es el estado actual
- h es el salto temporal(el tiempo que transcurre de un momento a otro) 
- f() es la funcion mostrada anteriormente
