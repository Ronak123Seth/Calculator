def addition(a,b):
    return a+b
def substraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
x=int(input("Enter the first number :"))
y=int (input("Enter the second number :"))
choice = int(input("1)Addition   2)substracion  3)multiplication  4)Division"))
if choice == 1:
    a = addition(x,y)
    print(a)
elif choice == 2:
    s = substraction(x,y)
    print(s)
elif choice == 3:
    m = multiplication(x,y)
    print(m)
elif choice == 4:
    d = division(x,y)
    print(d)
