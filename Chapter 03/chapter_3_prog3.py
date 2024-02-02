def total(initial=10, *numbers, **keywords):
    count = initial
    for num in numbers:
        count+=num
    for key in keywords:
        count+=keywords[key]
    return count
print(total(10,5,10,15,twenty=20,thirty=30,fifty=50))