class Delta:
    def __init__(self):
        print("No arguement method")
    def __init__(self, a):
        print("One arg method")
    def __init__(self, a, b):
        print("two args method")
d = Delta()              
# d = Delta(10)
d = Delta(10,20)
