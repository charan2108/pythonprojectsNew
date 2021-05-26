class A:
    def a1(self):
        print("a1 from A")
class B(A):
    def a1(self):
        print("a1 from B")
class C(A):
    def a1(self):
        print("a1 from C")
class D(B, C):
        print("a1 from  D")
print(A.mro())
print(B.mro())
print(C.mro())
print(D.mro())  

# With c object we are caling the m1 method
class A:
    def a1(self):
        print("a1 from A")
class B(A):
    def a1(self):
        print("a1 from B")
class C(A):
    def a1(self):
        print("a1 from C")
class D(B, C):
        print("a1 from  D")
        
c = C()
c.a1()
print(C.mro())              


# m1 method not avialable

class A:
    def m1(self):
        print("m1 from A method")
class B(A):
    def m1(self):
        print("m1 from B method ")
class C(A):
    def m1(self):
        print("m1 from C method") 
class D(B,C):
    def m2(self):
        print("m2 from  d method")
        
c = C()
c.m1()
print(C.mro())    



# callling the m1 method with object d                        #    
class A:
    def m1(self):
        print("The M1 method A")
class B(A):
    def m1(self):
        print("The M1 method from B ")
class C(A):
    def m1(self):
        print("The M1  method  from c")
class D(B,C):
    def m1(self):
        print("The M1 method from D ")
d = D()
d.m1() 
print(D.mro())  


class A:
    def m1(self):
        print("The M1 method A")
class B(A):
    def m1(self):
        print("The M1 method from B ")
class C(A):
    def m1(self):
        print("The M1  method  from c")
class D(B,C):
    def m3(self):
        print("The M1 method from D ")
d = D()
d.m1()      
print(D.mro())

class A:
    def m1(self):
        print("The M1 method A")
class B(A):
    def m2(self):
        print("The M1 method from B ")
class C(A):
    def m1(self):
        print("The M1  method  from c")
class D(B,C):
    def m3(self):
        print("The M1 method from D ")
d = D()
d.m1() 
print(D.mro())
                                
                                
# X1 = [ 'a', 1, 2, 4, 'hexnbit']
# X2 = ( 4, 6, 7 , 'total')
# X3 = { 'Ram' : 'Engineer', 2: 'Mohan'}
# X4 = {1, 2, 3, 4}

# print(type(X1))
# print(type(X2))
# print(type(X3))
# print(type(X4))
# def detail(name='Anonymous',age='Unknown',marks=0,subject='Science'):
#        print(name,age,marks,subject)
# detail(age=15,name='Lita')

# x =(5)
# print(type(x))

# def info(name ,age, gender):
#     print(name, age, gender )
# info('Male', 'John', 17)   

# x = input("Enter number")
# print(type(x)) 

# scores = {'Smith': 80, 'Steve': 85}
# if scores['Smith']>80:
#        print('Civil Engineering')
# elif scores['Steve']>80:
#        print('Electronics Engineering')
# elif scores['John']>80:
#        print('Teaching')
# else: print('Invalid')

X = {'hexnbit', 'tevatron', 'stemrobo' }
X.update(['hexnbit', 'e3dify', 'cybricsoft'])
print(X)

A = {'1', '2', '3'}
A.update(['1', '4','5', '6'])
print(A)

4=='4'
print(4)

a=5
def func():
       global a
       a=7
       print('Value of a inside the function',a)
print('Value of a before calling the function',a)
func()
print('Value of a after calling the function',a)

X= "Welcome to Hexnbit Let’s start learning Python"
print(len(X))

i=10
while i>0:
       i-=3
       print('*')
       if i<=4:
              break
       else:
              print('*')