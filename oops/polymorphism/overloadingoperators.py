class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def __a__(self, others):
        return self.marks>others.marks
    def __b__(self, others):
        return self.marks<=others.marks
c1 = Student('Alfa', 100)
c2 = Student('Beta', 150)
print("c1 > c2 =", c1 > c2)
print("c1 < c2 =", c1 < c2)    
            
        
    