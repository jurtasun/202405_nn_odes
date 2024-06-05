# Neural Networks for ODEs
# Jesús Urtasun, ICL - June 2024
# Numerical integration - trapezoidal rule
print("Numerical integration - Trapezoidal rule")

# Import libraries
import math

# Function performing trapezoidal integration
def trapezoid_rule(f, a, b, n):
    """
    Approximate the integral of f from a to b by the trapezoid rule.
    
    Parameters:
    f (function): The function to integrate.
    a (float): The start point of the integration interval.
    b (float): The end point of the integration interval.
    n (int): The number of subintervals.
    
    Returns:
    float: The approximate value of the integral.
    """
    h = (b - a) / n
    integral = 0.5 * (f(a) + f(b))
    
    for i in range(1, n):
        x = a + i * h
        integral += f(x)
    
    integral *= h
    return integral

# Function to integrate
def f(x):
    return math.sin(x)

# Integration interval
a = 0
b = math.pi
n = 100000

# Calculate integral and error
approx_integral = trapezoid_rule(f, a, b, n)
exact_integral = 2.0
error = abs(exact_integral - approx_integral)

print(f"Integral: {approx_integral}")
print(f"Error: {error}")