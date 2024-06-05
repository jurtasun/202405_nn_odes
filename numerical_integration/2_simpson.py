# Neural Networks for ODEs
# Jesús Urtasun, ICL - June 2024
# Numerical integration - Simpson rule
print("Numerical integration - Simpson rule")

# Import libraries
import math

# Function performing Simpson integration
def simpson_rule(f, a, b, n):
    """
    Approximate the integral of f from a to b by Simpson's rule.
    
    Parameters:
    f (function): The function to integrate.
    a (float): The start point of the integration interval.
    b (float): The end point of the integration interval.
    n (int): The number of subintervals (must be even).
    
    Returns:
    float: The approximate value of the integral.
    """
    if n % 2 != 0:
        raise ValueError("Number of subintervals (n) must be even.")
    
    h = (b - a) / n
    integral = f(a) + f(b)
    
    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            integral += 2 * f(x)
        else:
            integral += 4 * f(x)
    
    integral *= h / 3
    return integral

# Function to integrate
def f(x):
    return math.sin(x)

# Integration interval
a = 0
b = math.pi
n = 100000

# Calculate integral and error
approx_integral = simpson_rule(f, a, b, n)
exact_integral = 2.0
error = abs(exact_integral - approx_integral)

print(f"Integral: {approx_integral}")
print(f"Error: {error}")