def evaluate_polynomial(coefficients, n):
    result = 0
    for i, coeff in enumerate(coefficients):
        result += coeff * (n ** i)
    return result

# Example usage
coefficients = [4, 2, 9]
n = 5

result = evaluate_polynomial(coefficients, n)
print("The value of f(n) for n =", n, "is:", result)
