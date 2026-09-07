import math
import os

def bisection_method(f_function, a, b, file, problem_name, tolerance=1e-6, max_steps=100):
    """
    Runs the Bisection Method, writes steps to a text file, and returns the final root.
    """
    if f_function(a) * f_function(b) >= 0:
        file.write(f"--- {problem_name} ---\n")
        file.write(f"Error: Bisection fails. No sign change between {a} and {b}.\n\n")
        return None, 0

    file.write(f"--- {problem_name} [Interval: {a} to {b}] ---\n")
    step = 0
    
    while (b - a) / 2.0 > tolerance and step < max_steps:
        step += 1
        c = (a + b) / 2.0  # Find the midpoint
        
        file.write(f"Step {step:2}: a={a:.6f}, b={b:.6f}, midpoint(c)={c:.8f}\n")
        
        if f_function(c) == 0:
            break
            
        if f_function(a) * f_function(c) < 0:
            b = c  # Root is in the left half
        else:
            a = c 
            
    final_root = (a + b) / 2.0
    file.write(f"-> Success! Root is approx {final_root:.8f} (took {step} steps).\n\n")
    return final_root, step


# ==========================================
# MAIN EXECUTION
# ==========================================

with open("bisection_log.txt", "w") as f:
    f.write("BISECTION METHOD STEP-BY-STEP LOG\n")
    f.write("=================================\n\n")

    print("=== PROBLEM 1 (6 decimal places) ===")
    # 1(a) x^3 = 9 -> f(x) = x^3 - 9
    ans, steps = bisection_method(lambda x: x**3 - 9, 2.0, 3.0, f, "Problem 1(a)", tolerance=1e-6)
    print(f"1(a): x = {ans:.6f} (took {steps} steps)")

    # 1(b) 3x^3 + x^2 = x + 5 -> f(x) = 3x^3 + x^2 - x - 5
    ans, steps = bisection_method(lambda x: 3*(x**3) + x**2 - x - 5, 1.0, 2.0, f, "Problem 1(b)", tolerance=1e-6)
    print(f"1(b): x = {ans:.6f} (took {steps} steps)")

    # 1(c) cos^2(x) + 6 = x -> f(x) = cos^2(x) + 6 - x
    ans, steps = bisection_method(lambda x: math.cos(x)**2 + 6 - x, 6.0, 7.0, f, "Problem 1(c)", tolerance=1e-6)
    print(f"1(c): x = {ans:.6f} (took {steps} steps)")


    print("\n=== PROBLEM 2 (8 decimal places) ===")
    # 2(a) x^5 + x = 1 -> f(x) = x^5 + x - 1
    ans, steps = bisection_method(lambda x: x**5 + x - 1, 0.0, 1.0, f, "Problem 2(a)", tolerance=1e-8)
    print(f"2(a): x = {ans:.8f} (took {steps} steps)")

    # 2(b) sin(x) = 6x + 5 -> f(x) = sin(x) - 6x - 5
    ans, steps = bisection_method(lambda x: math.sin(x) - 6*x - 5, -1.0, 0.0, f, "Problem 2(b)", tolerance=1e-8)
    print(f"2(b): x = {ans:.8f} (took {steps} steps)")

    # 2(c) ln(x) + x^2 = 3 -> f(x) = ln(x) + x^2 - 3
    ans, steps = bisection_method(lambda x: math.log(x) + x**2 - 3, 1.0, 2.0, f, "Problem 2(c)", tolerance=1e-8)
    print(f"2(c): x = {ans:.8f} (took {steps} steps)")


    print("\n=== PROBLEM 3 (Find 3 roots, 6 decimal places) ===")
    # 3(a) 2x^3 - 6x - 1 = 0
    print("3(a):")
    func_3a = lambda x: 2*(x**3) - 6*x - 1
    ans, steps = bisection_method(func_3a, -2.0, -1.0, f, "Problem 3(a) - Root 1", tolerance=1e-6)
    print(f"  Root 1: x = {ans:.6f}")
    ans, steps = bisection_method(func_3a, -1.0, 0.0, f, "Problem 3(a) - Root 2", tolerance=1e-6)
    print(f"  Root 2: x = {ans:.6f}")
    ans, steps = bisection_method(func_3a, 1.0, 2.0, f, "Problem 3(a) - Root 3", tolerance=1e-6)
    print(f"  Root 3: x = {ans:.6f}")

    # 3(b) e^(x-2) + x^3 - x = 0
    print("3(b):")
    func_3b = lambda x: math.exp(x - 2) + x**3 - x
    ans, steps = bisection_method(func_3b, -2.0, -1.0, f, "Problem 3(b) - Root 1", tolerance=1e-6)
    print(f"  Root 1: x = {ans:.6f}")
    ans, steps = bisection_method(func_3b, -0.5, 0.5, f, "Problem 3(b) - Root 2", tolerance=1e-6)
    print(f"  Root 2: x = {ans:.6f}")
    ans, steps = bisection_method(func_3b, 0.5, 1.5, f, "Problem 3(b) - Root 3", tolerance=1e-6)
    print(f"  Root 3: x = {ans:.6f}")

    # 3(c) 1 + 5x - 6x^3 - e^(2x) = 0
    print("3(c):")
    func_3c = lambda x: 1 + 5*x - 6*(x**3) - math.exp(2*x)
    ans, steps = bisection_method(func_3c, -1.5, -0.5, f, "Problem 3(c) - Root 1", tolerance=1e-6)
    print(f"  Root 1: x = {ans:.6f}")
    ans, steps = bisection_method(func_3c, -0.5, 0.5, f, "Problem 3(c) - Root 2", tolerance=1e-6)
    print(f"  Root 2: x = {ans:.6f}")
    ans, steps = bisection_method(func_3c, 0.5, 1.5, f, "Problem 3(c) - Root 3", tolerance=1e-6)
    print(f"  Root 3: x = {ans:.6f}")

print("\nDONE! Opening the 'bisection_log.txt' file for you now...")

# This command automatically opens the file in your default text editor!
os.startfile("bisection_log.txt")