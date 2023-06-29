class SET:
    def __init__(self, elements):
        self.elements = elements
    
    def ismember(self, element):
        return element in self.elements
    
    def powerset(self):
        import itertools
        power_set = []
        for r in range(len(self.elements) + 1):
            power_set.extend(list(itertools.combinations(self.elements, r)))
        return power_set
    
    def subset(self, other_set):
        return set(self.elements).issubset(other_set.elements)
    
    def union(self, other_set):
        return list(set(self.elements).union(other_set.elements))
    
    def intersection(self, other_set):
        return list(set(self.elements).intersection(other_set.elements))
    
    def complement(self, universal_set):
        return list(set(universal_set.elements) - set(self.elements))
    
    def set_difference(self, other_set):
        return list(set(self.elements).difference(other_set.elements))
    
    def symmetric_difference(self, other_set):
        return list(set(self.elements).symmetric_difference(other_set.elements))
    
    def cartesian_product(self, other_set):
        import itertools
        return list(itertools.product(self.elements, other_set.elements))



# Creating sets
set1 = SET([1, 2, 3])
set2 = SET([2, 3, 4, 5])
universal_set = SET([1, 2, 3, 4, 5, 6, 7])

# Testing operations
print(set1.ismember(2))  # True
print(set1.ismember(4))  # False

print(set1.powerset())  # [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]

print(set1.subset(set2))  # False
print(set1.subset(SET([1, 2, 3, 4, 5])))  # True

print(set1.union(set2))  # [1, 2, 3, 4, 5]
print(set1.intersection(set2))  # [2, 3]

print(set1.complement(universal_set))  # [4, 5, 6, 7]

print(set1.set_difference(set2))  # [1]
print(set2.set_difference(set1))  # [4, 5]

print(set1.symmetric_difference(set2))  # [1, 4, 5]

print(set1.cartesian_product(set2))  # [(1, 2), (1, 3), (1, 4), (1, 5), (2, 2), (2, 3), (2, 4), (2, 5), (3, 2), (3, 3), (3, 4), (3, 5)]
