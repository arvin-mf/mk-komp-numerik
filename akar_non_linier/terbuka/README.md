# Newton-Raphson
## Teori

![](../../assets/akar_non_linier/newton_raphson_ilustrasi.png)

$$
\frac{\Delta y}{\Delta x} = \frac{y_b - y_a}{x_b - x_a} = \frac{f(x_n) - 0}{x_n - x_{n+1}} \text{ atau } \frac{f(x_n)}{x_n - x_{n+1}}
$$

$$
\begin{array}{rl}
f'(x_n) &= \frac{f(x_n)}{x_n - x_{n+1}}\\
x_n - x_{n+1} &= \frac{f(x_n)}{f'(x_n)}\\
x_{n+1} &= x_n - \frac{f(x_n)}{f'(x_n)}\\
\end{array}
$$


## Percobaan

![](../../assets/akar_non_linier/newton_raphson.png)

# Secant
