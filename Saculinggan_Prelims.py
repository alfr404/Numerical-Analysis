#Saculinggan, Alfer L.
#CS4C
#Prelims Exam

import math

def bisection_method(f, a, b, iterations):
    print(f"{'Iter':<5} | {'a':<8} | {'b':<8} | {'c':<8} | {'f(c)':<8}")
    print("-" * 45)
    for i in range(iterations):
        c = (a + b) / 2
        fc = f(c)
        print(f"{i+1:<5} | {a:<8.4f} | {b:<8.4f} | {c:<8.4f} | {fc:<8.4f}")
        
        if fc == 0:
            break
            
        if f(a) * fc < 0:
            b = c
        else:
            a = c

def fixed_point_iteration(g, x0, tol_decimal_places):
    print(f"{'Iter':<5} | {'x_n':<8} | {'x_n+1':<8} | {'Error':<8}")
    print("-" * 45)
    x = x0
    # Tolerance for 3 decimal places accuracy
    tolerance = 0.5 * 10**(-tol_decimal_places) 
    
    for i in range(20): # Safety limit to prevent infinite loops
        x_next = g(x)
        error = abs(x_next - x)
        print(f"{i+1:<5} | {x:<8.4f} | {x_next:<8.4f} | {error:<8.4f}")
        
        if error < tolerance:
            print(f"\nRoot found at approx: {x_next:.3f}")
            break
        x = x_next

print("--- PROBLEM 1 ---")
# f(x) = cos(x) - x, interval [0, 1], 6 iterations
print("Bisection Method for f(x) = cos(x) - x on [0, 1]")
bisection_method(lambda x: math.cos(x) - x, 0.0, 1.0, 6)
print("\n")

print("--- PROBLEM 2 ---")
# f(x) = tan(x) - 2, interval [1.0, 1.5], 6 iterations
print("Bisection Method for f(x) = tan(x) - 2 on [1.0, 1.5]")
bisection_method(lambda x: math.tan(x) - 2, 1.0, 1.5, 6)
print("\n")

print("--- PROBLEM 3 ---")
print("Fixed-Point Iteration for x^3 + x - 4 = 0")
print("Using g(x) = (4 - x)^(1/3) with x0 = 1.5")

fixed_point_iteration(lambda x: (4 - x)**(1/3), 1.5, 3)
