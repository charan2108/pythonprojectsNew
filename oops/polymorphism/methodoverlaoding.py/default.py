class Dell:
    def sum(self, a=None, b=None, c=None):
        if a!=None and b!=None and c!=None:
            print("the sum of the numbers is", a+b+c)
        elif a!=None and b!=None:
            print("the sum is ", a+b)
        else:
            print("provide the arguements")  
                  
d = Dell()
d.sum(10,20,30)
d.sum(10,20)
d.sum(10)                
            