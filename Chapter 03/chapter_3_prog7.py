def factorial(n):
    print("factorial has been called with n = " + str(n))
    if n == 1:
        return 1
    else:
        res = n * factorial(n-1)
        print("track ", n, " * factorial(" ,n-1, "): ",res)
        return res

#Now test the function:
print(factorial(5))