x=int(input("Enter the number"))

if x%2 == 0:
    print("x is not a prime number")
else:
    for i in range(3,x,1):
        if x%i == 0:
            print("x is not a prime number")
            t=0
            break
        else:
            continue
        if t == 0:
            print("x  a prime number")
    