class bird :
    def fly (self):
        print ("some birds fly")
class sparrow(bird):
    def fly (self):
        print ("sparrows can fly")
class ostrich (bird):
    def fly (self):
        print ("ostriches cannot fly")
#objects
a = bird ()
b = sparrow ()
c = ostrich ()
a.fly()
b.fly() 
c.fly()