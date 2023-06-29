def find_equation_solutions(n, C):
    solutions = []
    find_solutions_recursive(n, C, [], solutions)
    return solutions

def find_solutions_recursive(n, C, current_solution, solutions):
    if n == 0:
        if C == 0:
            solutions.append(list(current_solution))
        return
    
    for i in range(C + 1):
        current_solution.append(i)
        find_solutions_recursive(n - 1, C - i, current_solution, solutions)
        current_solution.pop()

# Example usage
n = 4
C = 5

solutions = find_equation_solutions(n, C)

for solution in solutions:
    print(solution)
