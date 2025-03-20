def add (a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if(b==0):
        return"Zero division is not possible"
    return a/b



while True:
    print("\nMenu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice=input("enter ur choice based on the above menu")
    if(choice=="5"):
        print("Exiting Program"
              )
        break
    num1=float(input("Enter the first number"))
    num2=float(input("Enter the second number"))

    if choice=="1":
        print("Result: ",add(num1,num2),),
    elif choice=="2":
        print("Result: ",subtract(num1,num2),),
    elif choice=="3":
        print("Result: ",multiply(num1,num2),),
    elif choice=="4":
        print("Result: ",divide(num1,num2),),
    else:
        print("invalid choice") 