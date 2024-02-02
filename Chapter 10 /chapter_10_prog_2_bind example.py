import tkinter
import random

#Create the main window
my_window = tkinter.Tk()
#set window size
my_window.geometry("300x300")
#Create button
button = tkinter.Button(my_window, text="Hit Any Key on YourKeybord!")
def button_function(e):
    print("Your score is: ",random.randint(1,100))

button.grid(row=0, column=0)
my_window.bind("<KeyPress>", button_function)


#Start the mainloop
my_window.mainloop()