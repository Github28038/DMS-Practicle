class RELATION:
    def __init__(self, matrix):
        self.matrix = matrix
    
    def is_reflexive(self):
        n = len(self.matrix)
        for i in range(n):
            if self.matrix[i][i] != 1:
                return False
        return True
    
    def is_symmetric(self):
        n = len(self.matrix)
        for i in range(n):
            for j in range(n):
                if self.matrix[i][j] != self.matrix[j][i]:
                    return False
        return True
    
    def is_antisymmetric(self):
        n = len(self.matrix)
        for i in range(n):
            for j in range(n):
                if i != j and self.matrix[i][j] == 1 and self.matrix[j][i] == 1:
                    return False
        return True
    
    def is_transitive(self):
        n = len(self.matrix)
        for i in range(n):
            for j in range(n):
                if self.matrix[i][j] == 1:
                    for k in range(n):
                        if self.matrix[j][k] == 1 and self.matrix[i][k] != 1:
                            return False
        return True
    
    def determine_relation_type(self):
        if self.is_reflexive() and self.is_symmetric() and self.is_transitive():
            return "Equivalence Relation"
        elif self.is_reflexive() and self.is_antisymmetric() and self.is_transitive():
            return "Partial Order Relation"
        else:
            return "None"

# Example usage
matrix1 = [[1, 0, 1],
           [0, 1, 0],
           [1, 0, 1]]

matrix2 = [[1, 1, 0],
           [1, 1, 0],
           [0, 0, 1]]

relation1 = RELATION(matrix1)
relation2 = RELATION(matrix2)

print(relation1.is_reflexive())  # True
print(relation1.is_symmetric())  # True
print(relation1.is_antisymmetric())  # False
print(relation1.is_transitive())  # True
print(relation1.determine_relation_type())  # Equivalence Relation

print(relation2.is_reflexive())  # True
print(relation2.is_symmetric())  # True
print(relation2.is_antisymmetric())  # True
print(relation2.is_transitive())  # False
print(relation2.determine_relation_type())  # None
