class ArrayIntersection:
    def __init__(self, array1, array2):
        self.array1 = array1
        self.array2 = array2

    def find_intersection(self):
        result = []
        i, j = 0, 0
        
        
        while i < len(self.array1) and j < len(self.array2):
            if self.array1[i] < self.array2[j]:
                i += 1
            elif self.array1[i] > self.array2[j]:
                j += 1
            else:
                
                if not result or result[-1] != self.array1[i]:
                    result.append(self.array1[i])
                i += 1
                j += 1
        
        return result



array1 = [1, 2, 4, 5, 6]
array2 = [2, 4, 6, 8, 10]

intersection_finder = ArrayIntersection(array1, array2)
result = intersection_finder.find_intersection()

print("Intersection of the two arrays:", result)


