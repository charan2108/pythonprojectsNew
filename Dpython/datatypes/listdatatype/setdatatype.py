s = {100,200,300,400,500,'hello'}
print(s)
print(type(s))
s.add(334)
s.add(150)
print(s)
s.remove(500)
print(s)

# frozenset
s ={10,20,25,30,50}
fs= frozenset(s)
print(fs)
print(type(fs))
frozenset({30,50,607,0})
for i in fs:
    print(i)