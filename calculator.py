def firstname():
    a = float(input("Write the first number: "))
    print(f'{a} you choose this number')
    
    return a

def lastname():
    b = float(input("Write the second number: "))
    print(f'{b} you choose this number')
    
    return b

def multiplication(a,b):
    operation = a * b

    return print(f'{operation} This is the result of the operation')

def division(a,b):
    operation = a / b

    return print(f'{operation} This is the result of the operation')

def Sum(a,b):
    operation = a + b

    return print(f'{operation} This is the result of the operation')

def rest(a,b):
    operation = a - b

    return print(f'{operation} This is the result of the operation')

def exponential(a,b):
    operation = a ** b

    return print(f'{operation} This is the result of the operation')

print ('Made by Ronaldo Romero Vergel')
while True:
    print("""-- What operation would you like to execute? --
    1 Multiplication
    2 Division
    3 Sum
    4 Rest
    5 Exponential
    6 Exit""")

    choose = int(input("Write the number of the operation that you want to do: "))

    if choose == 1:
        print("You chose Multiplication")
        multiplication(firstname(), lastname())
    elif choose == 2:
        print("You chose Division")
        division(firstname(), lastname())
    elif choose == 3:
        print("You chose Sum")
        Sum(firstname(), lastname())
    elif choose == 4:
        print("You chose Rest")
        rest(firstname(), lastname())
    elif choose == 5:
        print("You chose Exponential")
        exponential(firstname(), lastname())
    elif choose == 6:
        print("exiting the calculator..")
        break
    else:
        print('You entered an invalid option')