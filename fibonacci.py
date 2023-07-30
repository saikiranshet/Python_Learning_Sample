def fibo(n):
    if n < 0:
        print("Not a Valid Number")
    elif n == 0:
        return 0    
    elif n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

n = int(input("Enter n value:\n"))
print(fibo(n))