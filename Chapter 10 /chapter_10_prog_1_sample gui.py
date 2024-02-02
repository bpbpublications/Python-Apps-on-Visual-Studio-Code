import tkinter

#Create the main window
my_window = tkinter.Tk()

#set window size
my_window.geometry("300x300") #widthxheight

#Set window title
my_window.title("Mastering TKinter GUI capabilities using VS Code!")

#Create a label
label = tkinter.Label(my_window, text="This is a sample label!")
label.pack()

#Create a button
button = tkinter.Button(my_window, text="Click Here to Quit", command=my_window.quit)
button.pack()

#Start the mainloop
my_window.mainloop()