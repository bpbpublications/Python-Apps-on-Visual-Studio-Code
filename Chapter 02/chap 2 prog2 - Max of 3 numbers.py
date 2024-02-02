#Finding the highest value among 3 variables
a,b,c = 55,44,33

if a >= b:
    if a >= c:
        #A is either equal to or greater than all the given values
        print("A variable is greatest!")
    else:
        #C is greater hence C is the highest
        print("C variable is greatest!")
else:
    #Means B is greater than A
    if b >=c:
        #B is highest
        print("C variable is greatest!")
    else:
        #C is higher than C
        print("C variable is greatest!")

print("Thank you for using our program")

