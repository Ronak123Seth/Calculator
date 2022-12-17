def addition(a,b):
    return a+b 

def substraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    return a/b

x=int(input("Enter the first number :"))

choice = int(input("1)Addition   2)substracion  3)multiplication  4)Division"))

y=int (input("Enter the second number :"))

s=0            
if choice == '+':
    s = addition(x,y)
elif choice == '-':
    s = substraction(x,y)
elif choice == '*':
    s = multiplication(x,y)
elif try: choice == '/':
    s = division(x,y)
    except Exception as e:
        print(e)
        s=Math.inf
        print("cannot divide by zero !")ṭ
else:
    print("NOT POSSIBLE")
print(s)
