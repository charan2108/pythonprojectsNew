class Dell:
    def sum(self, *a):
        delta = 0
        for x in a:
            delta=delta+x
        print("the sum is", delta)     
d = Dell()
d.sum(10,20,30)
d.sum(10,20)
d.sum(10)                