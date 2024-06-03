# Neural Networks for ODEs
# Jesús Urtasun, Imperial College London - May 2024
# Numerical integration - Monte Carlo
print("Numerical integration - Monte Carlo")

# Import libraries
import random
import math

# Function performing Monte Carlo integration
def monte_carlo_integration(f, a, b, n):
    """
    Approximate the integral of f from a to b using the Monte Carlo method.
    
    Parameters:
    f (function): The function to integrate.
    a (float): The start point of the integration interval.
    b (float): The end point of the integration interval.
    n (int): The number of random samples.
    
    Returns:
    float: The approximate value of the integral.
    """
    sum_f = 0.0
    
    for _ in range(n):
        x = random.uniform(a, b)
        sum_f += f(x)
    
    integral = (b - a) * sum_f / n
    return integral

# Define the function to integrate
def f(x):
    return math.sin(x)

# Integration interval
a = 0
b = math.pi

# Number of random samples
n = 100000

# Function to integrate
def f(x):
    return math.sin(x)

# Integration interval
a = 0
b = math.pi
n = 1000000

# Calculate integral and error
approx_integral = monte_carlo_integration(f, a, b, n)
exact_integral = 2.0
error = abs(exact_integral - approx_integral)

print(f"The approximate value of the integral is: {approx_integral}")
print(f"The error is: {error}")