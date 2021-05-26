class Book:
    def ___init___(self, pages):
        self.pages = pages
    def ___add___(self, others):
        return self.pages + others.pages
    
a1= Book(20)
a2= Book(20)

print(a1 + a2)    
    
    
