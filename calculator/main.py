def calc():
    choose = input("Enter what to do:"
                   "\n1. Addition"
                   "\n2. Subtraction"
                   "\n3. Multiplication"
                   "\n4. Division"
                   "\n=> ")

    if (choose == "1") or ("addition" in choose.lower()):
        import add
        print(add.addition())

    elif (choose == "2") or ("subtraction" in choose.lower()):
        import sub
        print(sub.sub())

    '''elif (choose == "3") or ("multiplication" in choose.lower()):
        import mul
        print(mul.multiply())

    elif (choose == "4") or ("division" in choose.lower()):
        import div
        print(div.divide())'''

'''   else:
        print("Invalid choice!")
'''
calc()
