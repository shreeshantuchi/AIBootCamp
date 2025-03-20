def factorial(a):
    factorial=1
    while a!=0:
        factorial=factorial*a;
        a-=1
    return factorial




num=int(input("enter the number"))
print(f"Factrorial: {num} ", factorial(num))

