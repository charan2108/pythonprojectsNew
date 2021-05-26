class Book:
    def __init__(self, pages):
        self.pages = pages
        
b1=Book(200)
b2=Book(200)
print(type(b1))
print(type(b2))

print(b1.pages + b2.pages) 
print((b1.pages).__add__(b2.pages))
print(type(b1.pages))
print(type(b2.pages))
# print((b1.pages).__add__(b2.pages))

# class Home:
#     def __init__(self, area, location):
#         self.area = area
#         self.location = ''
      
# a1 = Home(6000)
# a2 = Home(Hyd)

# print(a1.area + a2.location)
# print(type(a1))
# print(type(a2))

# print((a1.area).__add__(a2.location))
# print(type(a1.area))
# print(a2.location)
        
       


       
        