#permutation with repetion

def generate_permutations_with_repetition(digits, length):
    if length == 0:
        return [[]]
    
    permutations = []
    smaller_permutations = generate_permutations_with_repetition(digits, length - 1)
    
    for digit in digits:
        for smaller_permutation in smaller_permutations:
            permutation = [digit] + smaller_permutation
            permutations.append(permutation)
    
    return permutations

# Example usage
digits = [1, 2, 3]
length = 3

permutations_with_repetition = generate_permutations_with_repetition(digits, length)
for permutation in permutations_with_repetition:
    print(permutation)

print("")
print("")

#Permutation Without repetition

def generate_permutations_without_repetition(digits):
    if len(digits) == 0:
        return [[]]
    
    permutations = []
    
    for i in range(len(digits)):
        smaller_permutations = generate_permutations_without_repetition(digits[:i] + digits[i+1:])
        for smaller_permutation in smaller_permutations:
            permutation = [digits[i]] + smaller_permutation
            permutations.append(permutation)
    
    return permutations

# Example usage
digits = [1, 2, 3]

permutations_without_repetition = generate_permutations_without_repetition(digits)
for permutation in permutations_without_repetition:
    print(permutation)
