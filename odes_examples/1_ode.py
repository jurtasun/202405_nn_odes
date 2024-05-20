# Neural Networks for ODEs
# Jesús Urtasun, Imperial College London - May 2024
# Example solution of ordinary differential equations
print("Example solution of ordinary differential equations")

# Import libraries
import numpy as np
import matplotlib.pyplot as plt

# Define the ODE function
def dydt(t, y):
    return -2 * y

# Euler method
def euler_method(f, y0, t0, t_end, h):
    n_steps = int((t_end - t0) / h)
    t_values = np.linspace(t0, t_end, n_steps + 1)
    y_values = np.zeros(n_steps + 1)
    y_values[0] = y0

    for i in range(n_steps):
        y_values[i + 1] = y_values[i] + h * f(t_values[i], y_values[i])
    
    return t_values, y_values

# Runge-Kutta 4th order method
def runge_kutta_method(f, y0, t0, t_end, h):
    n_steps = int((t_end - t0) / h)
    t_values = np.linspace(t0, t_end, n_steps + 1)
    y_values = np.zeros(n_steps + 1)
    y_values[0] = y0

    for i in range(n_steps):
        t = t_values[i]
        y = y_values[i]
        k1 = h * f(t, y)
        k2 = h * f(t + h / 2, y + k1 / 2)
        k3 = h * f(t + h / 2, y + k2 / 2)
        k4 = h * f(t + h, y + k3)
        y_values[i + 1] = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6

    return t_values, y_values

# Parameters
y0 = 1
t0 = 0
t_end = 5
h = 0.1

# Solve the ODE using both methods
t_euler, y_euler = euler_method(dydt, y0, t0, t_end, h)
t_rk, y_rk = runge_kutta_method(dydt, y0, t0, t_end, h)

# Exact solution for comparison
t_exact = np.linspace(t0, t_end, 100)
y_exact = y0 * np.exp(-2 * t_exact)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(t_euler, y_euler, "o-", label="Euler Method", markersize=4)
plt.plot(t_rk, y_rk, "s-", label="Runge-Kutta 4th Order", markersize=4)
plt.plot(t_exact, y_exact, "-", label="Exact Solution")
plt.xlabel("Time t")
plt.ylabel("y(t)")
plt.title("Comparison of Euler and Runge-Kutta Methods")
plt.legend()
plt.grid(True)
plt.show()