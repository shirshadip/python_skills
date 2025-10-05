def add_all(*numbers):

    
    total =sum(numbers)
    return total
print(add_all(2,3,4,5,6,7,8,9,90))

def print_info(**info):
    for key, value in info.items():
        print(key,"=", value)

print_info(name = "shirshadip", age= 16,city = "kolkata")
