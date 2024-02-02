# defining a class AboutMe
class AboutMe:
    # defining the __init__ method
    def __init__(self, name, city):
        self.name = name
        self.city = city

    # defining the getCity method
    def getCity(self):
        print(self.name + " lives in the city " + self.city)


# defining the function hello
def hobbies():
    print("I love playing badminton and have my interest in"
          "Creative arts, including writing and painting.")

# creating a variable
work = 'I am a Technoculturist'

if __name__ == "__main__":
    print("Executed when invoked directly")
    # calling the function hobbies()
    hobbies()

    # creating the object captain
    captain = AboutMe('Dhoni','Ranchi')

    # calling the getCity() method for the object
    captain.getCity()

    #printing the variable work present in aboutme.py
    print(work)

