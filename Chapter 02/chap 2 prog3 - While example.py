while True:
    #Directly using True instead of a conditional statement
    #  will make it an infinite running loop
    s= input('Enter something: ')
    if s.lower()=='quit':
        #lower() will convert s content into lowercase break
        break
    print("Length of the given text is ", len(s))
print("Goodbye")

