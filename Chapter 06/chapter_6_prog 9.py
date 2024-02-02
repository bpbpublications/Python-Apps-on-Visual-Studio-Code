import string 
import random 

#Create a dictionary of all possible characters 
possible_characters = { 
    'lowercase_letters': string.ascii_lowercase, 
    'uppercase_letters': string.ascii_uppercase, 
    'numbers': string.digits, 
    'special_characters': string.punctuation
}

#Create an empty list to store the password 
password = [] 

#Loop 8 times and randomly pick one character from each dictionary 
for i in range(8): 
    #Randomly select one of the 4 character types 
    character_type = random.choice(list(possible_characters.keys())) 
    #Randomly select one character from the selected character type 
    character = random.choice(possible_characters[character_type]) 
    #Add the character to the password list 
    password.append(character) 

#Join the characters in the password list together 
password = ''.join(password) 

#Print the password 
print("Your new random password is:", password)