
my_dict = {
    "name": "Snehil Saurav",
    "age": 27,
    "country": "UK"
    }

# Accessing the dictionary items
print(my_dict["name"])
print(my_dict["age"])
print(my_dict["country"])

# Adding an item
my_dict["gender"] = "Male"

# Removing an item
del my_dict["age"]

# Looping through a dictionary
for key, value in my_dict.items():
    print(key + ": " + value)