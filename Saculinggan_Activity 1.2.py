import os
import math

def fixed_point_iteration(g_function, initial_guess, file, problem_name, tolerance=1e-8, max_steps=1000):
    """Runs the FPI, writes steps to a text file, and returns the final answer."""
    x_current = initial_guess
    
    # Write the starting information to our text file
    file.write(f"--- {problem_name} ---\n")
    file.write(f"Step 0: {x_current:.8f}\n")
    
    for step in range(1, max_steps + 1):
        x_next = g_function(x_current)
        
        # Write each step to the text file instead of printing to the terminal
        file.write(f"Step {step}: {x_next:.8f}\n")
        
        if abs(x_next - x_current) < tolerance:
            file.write(f"-> Success! Converged in {step} steps.\n\n")
            return x_next, step
            
        x_current = x_next
        
    file.write(f"-> Failed to reach the answer within max steps.\n\n")
    return None, max_steps

# ==========================================
# MAIN EXECUTION
# ==========================================

# This opens (or creates) a text file named "iterations_log.txt" in write mode ("w")
with open("iterations_log.txt", "w") as f:
    
    f.write("FIXED-POINT ITERATION STEP-BY-STEP LOG\n")
    f.write("======================================\n\n")

    print("=== PROBLEM 1 (8 decimal places) ===")
    ans, steps = fixed_point_iteration(lambda x: (2*x + 2)**(1/3), 1.0, f, "Problem 1(a)")
    print(f"1(a): x = {ans:.8f} (took {steps} steps)")

    ans, steps = fixed_point_iteration(lambda x: math.log(7 - x), 1.0, f, "Problem 1(b)")
    print(f"1(b): x = {ans:.8f} (took {steps} steps)")

    ans, steps = fixed_point_iteration(lambda x: math.log(4 - math.sin(x)), 1.0, f, "Problem 1(c)")
    print(f"1(c): x = {ans:.8f} (took {steps} steps)")


    print("\n=== PROBLEM 2 (8 decimal places) ===")
    ans, steps = fixed_point_iteration(lambda x: (1 - x)**0.2, 0.5, f, "Problem 2(a)")
    print(f"2(a): x = {ans:.8f} (took {steps} steps)")

    ans, steps = fixed_point_iteration(lambda x: (math.sin(x) - 5) / 6, -1.0, f, "Problem 2(b)")
    print(f"2(b): x = {ans:.8f} (took {steps} steps)")

    ans, steps = fixed_point_iteration(lambda x: math.sqrt(3 - math.log(x)), 1.5, f, "Problem 2(c)")
    print(f"2(c): x = {ans:.8f} (took {steps} steps)")


    print("\n=== PROBLEM 3 (Square roots, 8 decimal places) ===")
    ans, steps = fixed_point_iteration(lambda x: 0.5 * (x + 3/x), 1.5, f, "Problem 3(a) - sqrt(3)")
    print(f"3(a) sqrt(3): {ans:.8f} (took {steps} steps)")

    ans, steps = fixed_point_iteration(lambda x: 0.5 * (x + 5/x), 2.0, f, "Problem 3(b) - sqrt(5)")
    print(f"3(b) sqrt(5): {ans:.8f} (took {steps} steps)")


    print("\n=== PROBLEM 4 (Cube roots, 8 decimal places) ===")
    ans, steps = fixed_point_iteration(lambda x: (2*x + 2/(x**2)) / 3, 1.0, f, "Problem 4(a) - cbrt(2)")
    print(f"4(a) cbrt(2): {ans:.8f} (took {steps} steps)")

    ans, steps = fixed_point_iteration(lambda x: (2*x + 3/(x**2)) / 3, 1.5, f, "Problem 4(b) - cbrt(3)")
    print(f"4(b) cbrt(3): {ans:.8f} (took {steps} steps)")

    ans, steps = fixed_point_iteration(lambda x: (2*x + 5/(x**2)) / 3, 1.5, f, "Problem 4(c) - cbrt(5)")
    print(f"4(c) cbrt(5): {ans:.8f} (took {steps} steps)")


    print("\n=== PROBLEM 5 (6 decimal places) ===")
    ans, steps = fixed_point_iteration(lambda x: math.cos(x)**2, 0.5, f, "Problem 5", tolerance=1e-6)
    print(f"5:   x = {ans:.6f} (took {steps} steps)")

print("\nOpening the log file...")
os.startfile("iterations_log.txt")