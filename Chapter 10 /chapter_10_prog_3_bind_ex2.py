import tkinter as tk
#First, let’s create the window and set the title:
root = tk.Tk()
root.title("Event Example")

#Next, we will define a function to handle the mouse click event:
def on_click(event):
    # Get the coordinates of the mouse click
    x = event.x
    y = event.y
    print("Clicked at ", x, y)

#Finally, we will bind the mouse click event to the window and start the main loop:
root.bind("<Button-1>", on_click)
root.mainloop()