x=50
#Function definition
def func(x):
    print("X is ",x)
    x=2
    output = "Changed X locally to " + str(x) + " in the function"
    return output

result = func(x)
print(result)
print("X is still ",x)