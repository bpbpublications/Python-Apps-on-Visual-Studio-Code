
# Example of Inheritance in Python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("%s says 'hello!'" % self.name)


class Dog(Animal):
    def bark(self):
        print("%s barks 'woof!'" % self.name)


# Create an instance of the Dog class
d = Dog("Fido")

# Call the speak() method
d.speak()

# Output
#Fido says 'hello!'

# Call the bark() method
d.bark()

#Output
#Fido barks 'woof!'