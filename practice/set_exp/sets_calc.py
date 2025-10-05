
set_type = input("enter which type of set you want to include as input:\n"
                 "1.string sets:\n"
                 "2.integer sets:\n"
                 "                "
)
print(set_type)

def sets():
    if set_type == "1" or set_type.lower() == "string sets":
        A = input("enter the elements of sets separating by commas:")
        sets_ = set(A.split(","))
        print(sets_)
    elif set_type == "2" or set_type.lower() == "integer sets":
       opt= (input ("enter what to do :\n" \
        "1.to tabular form:"))
    if opt == "1." or opt.lower()=="to tabular form":
        def to_t():
            S_B_F=int (input (""))
    else:
        print ("enter a correct input")

sets()
