class Animal:
    def make_sound(self):
        print("This animal makes a sound!")


class Dog(Animal):
    def make_sound(self):
        print("Woof!")


class Cat(Animal):
    def make_sound(self):
        print("Meow!")


dog = Dog()
cat = Cat()

dog.make_sound()
cat.make_sound()