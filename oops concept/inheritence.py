class animal :
    def speak(self) -> None:
        print ("animals make sounds")

class dog (animal):
    def speak (self):
        print ("dogs bark")


class cat (animal):
    def speak (self):
        print ("cats meow")

#objects 

a = animal ()
b = dog ()

c = cat ()


a.speak()
b.speak()   
c.speak()