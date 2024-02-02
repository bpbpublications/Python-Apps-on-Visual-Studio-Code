from tkinter import *
import tkinter.messagebox as msgbox
from PIL import ImageTk, Image
from Databank import level1_questions,level2_questions,level3_questions
import random
import time

answer = 0
score = 0
life = 3
player_name = ""
highest_score = 0
highest_name = ""
level2,level3=1,1
tower_height = 27
timer_text = 30

try:
    with open("MyQuizGameScore.txt", 'r') as hs:
        if hs.read():
            hs.seek(0)
            data = hs.read().split()
            highest_name = data[1]
            highest_score = int(data[3])

except FileNotFoundError:
    pass

r = random.choice(level1_questions)  #default level 1

def fetching_questions():
    """ This function will keep track of the score and fetch the questions from Level 1 or 2 or 3
    List based on the score. It doesnt take any input not does it return any value.
    Question content is updated everytime this is run. This function has to run to keep the
    game moving till the end.
    """
    global r, level1_questions,level2_questions,level3_questions, level2,level3

    if score<=5:
        level1_questions.remove(r)
        if level1_questions:
            r = random.choice(level1_questions)
        else:
            msgbox.showinfo("Gameover!" , "Sorry, we have run out of questions.")

            exit()
    elif score <=10:   #level 2
        if level2==1:
            msgbox.showinfo("Moving to the Next Level!","Congratulation! You now move to Level 2")
            level2=0

        if level2_questions:
            r = random.choice(level2_questions)
            level2_questions.remove(r)
        else:
            msgbox.showinfo("Gameover", "Sorry, we have run out of questions!")
            exit()
    else:  #level 3
        if level3==1:
            msgbox.showinfo("Moving to the Next Level!",
                            "Congratulation! You have now moved to the Level 3")
            level3=0

        if level3_questions:
            r = random.choice(level3_questions)
            level3_questions.remove(r)
        else:
            msgbox.showinfo("AWESOME!", "You have completed the game. Good Job Genius!")
            exit()
def a_response():
    """Handle answer response A if the answer is correct or not"""
    global answer
    answer = 1
    check_answer()

def b_response():
    """Handle answer response B if the answer is correct or not"""
    global answer
    answer = 2
    check_answer()

def c_response():
    """Handle answer response C if the answer is correct or not"""
    global answer
    answer = 3
    check_answer()

def d_response():
    """Handle answer response D if the answer is correct or not"""
    global answer
    answer = 4
    check_answer()

def check_answer():
    """This function checks the number of lives available and if indeed life is more than 1
    then continue with the main logic, if answer is correct build the tower at the
    specific position.
    If life becomes zero then the game exit but before that it checks if the current player
    has broken the highest score. If yes then the MyQuizGameScore.txt is updated with the
    player's name and score."""
    global score, answer, life, r, current_score
    if life > 1:
        if answer == r['answer']:
            score = score + 1
            loc = score * tower_height
            canvas_tower.create_image(2, 660 - loc, anchor=NW, image=new_image2)
            msgbox.showinfo("Correct!","That's Right! Congratulations!\n "
                                       "Your tower is now higher by one more block")

        else:
            msgbox.showerror("Incorrect!","Sorry, that's not correct. You lost a life")
            life = life - 1
        #Play the game
        fetching_questions()
        canvas.itemconfig(ques, text=r['question'])
        canvas1.itemconfig(rem_life, text=f"Remaining lives : {'❤' * life}")
        b1['text'] = r['choices'][0]
        b2['text'] = r['choices'][1]
        b3['text'] = r['choices'][2]
        b4['text'] = r['choices'][3]
        current_score_canvas.itemconfig(score_current, text=f"Your Current Score : {score}")

    else:
        if score >= highest_score:
            with open('MyQuizGameScore.txt','w') as f:
                f.write(f"Name: {player_name}\nScore: {score}")
            msgbox.showinfo("....ohhhh!","The Joys and Struggles of Life: "
                            "You are now the highest rated player and also the end of your game here")
        exit()

def gameover():
    """Game over function when all the lives are lost"""
    canvas_tower.delete("all")
    msgbox.showerror("GAME OVER!", "You lost third life too. The game is over")
    exit()

def start():
    """verifies the name entered during the welcome screen"""
    global player_name
    if name.get():
        player_name = name.get()
        first.destroy()
    else:
        msgbox.showerror("Name Error", 'Please Enter Your Name')

# Timer function
# Define a timer.
    def countdown():
        p = 30.00
        t = time.time()
        n = 0
        # Loop while the number of seconds is less than the integer defined in "p"
        while n - t < p:
            n = time.time()
            if n == t + p:
                timer_text ="Time's up!"
            else:
                timer_text = round(n - t)

#Menu bar functions
def closegame():
    """To end the program whenever the user want to"""
    choice = msgbox.askyesno(root, "Do You Really Want to Quit?")
    if choice:
        quit()


if __name__ == "__main__":
    first = Tk()

    first.geometry("1500x800")
    first.config(bg='#051BFD') #hexadecimal code for blue color
    #Bar to display the Title of the game
    cs = Canvas(first, width=1200, height=80, bg="#F2FD05") #yellow
    cs.create_text(600, 40, text="MY QUIZ GAME ", fill='Blue', font=('', '35', 'bold'))
    cs.place(relx=0.08, rely=0.25)
    #Second Bar to message and accept the input
    cs1 = Canvas(first, width=450, height=60, bg="#051BFD")
    cs1.create_text(245, 29, text="Enter Your Name: ", fill='white', font=('', '20','bold'))
    cs1.place(relx=0.17, rely=0.4)
    # accept the name in textbox
    name = Entry(first, width=19, font=('', '40'), relief=RIDGE)
    name.place(relx=0.47, rely=0.4)
    #add the button and the text on it
    sub = Button(text="Let's Play", background='#051BFD', fg='white',
                 padx=20,pady=20,bd=10,font=('', '35'), relief=GROOVE, command=start)
    sub.place(relx=0.43, rely=0.52)
    first.mainloop()

    #Start of second Window
    if player_name:
        root = Tk()
        root.geometry("1920x1080")
        #Create Menu
        menubar = Menu(root, background='blue', fg='white')
        file = Menu(menubar, tearoff=0)
        menubar.add_cascade(label='File', menu=file)

        file.add_command(label='New Game')
        file.add_command(label='Save Game')
        file.add_command(label='Exit', command=closegame)
        root.config(bg='blue', menu=menubar)
        root.title("My Quiz Game")

        # metrics and question block
        welcome = Canvas(root, width=1450, height=40, bg="#051BFD")
        welcome.create_text(700, 24, text=f"★   WELCOME {player_name.upper()}   ★", fill="#F2FD05", font=(" ", 24))
        welcome.place(relx=0.02, rely=0.02)

        canvas2 = Canvas(root, width=500, height=50, bg="#DF0A3A")
        curr_score = canvas2.create_text(200, 30, text=f"HIGHEST SCORE : "
                                                       f"{highest_score} towers by {highest_name}", fill="white", font=("", 16))
        canvas2.place(relx=0.6, rely=0.12)

        canvas1 = Canvas(root, width=500, height=50, bg="#F5AC03")
        rem_life = canvas1.create_text(200, 30, text=f"Remaining lives : {'❤️' * life}", fill="white", font=("", 16))
        canvas1.place(relx=0.6, rely=0.21)
        #Questions board
        canvas = Canvas(root, width=500, height=300, bg='black')
        ques = canvas.create_text(250, 60, text=r['question'], fill="white", font=("", 14), width=490)
        canvas.place(relx=0.6, rely=0.32)

        #placing option buttons
        b1 = Button(root, text=r['choices'][0],font=(" ", 10), padx=25,bd=10,command=a_response)
        b1.place(relx=0.585, rely=0.79)
        b2 = Button(root, text=r['choices'][1], font=(" ", 10), padx=25,bd=10,command=b_response)
        b2.place(relx=0.682, rely=0.79)
        b3 = Button(root, text=r['choices'][2], font=(" ", 10), padx=25,bd=10,command=c_response)
        b3.place(relx=0.780, rely=0.79)
        b4 = Button(root, text=r['choices'][3], font=(" ", 10), padx=25,bd=10,command=d_response)
        b4.place(relx=0.873, rely=0.79)

        # tower code
        canvas_tower = Canvas(root, width=245, height=660,background='white')
        img2 = (Image.open("block.png"))
        resized_image2 = img2.resize((245, tower_height), Image.LANCZOS)
        new_image2 = ImageTk.PhotoImage(resized_image2)
        canvas_tower.place(relx=0.04, rely=0.10)

        #Score label position
        current_score_canvas = Canvas(root, width=250, height=40, bg="#DF0A3A")
        score_current = current_score_canvas.create_text(140, 25, text=f"Your current Score : {score}", fill="white", font=("", 12))
        current_score_canvas.place(relx=0.36, rely=0.55)

        #Display the block  below score card
        canvas_always = Canvas(root, width=245, height=60,background='#051BFD')
        img1 = (Image.open("block.png"))
        resized_image1 = img1.resize((245, 60), Image.LANCZOS)
        new_image1 = ImageTk.PhotoImage(resized_image1)
        canvas_always.create_image(2, 2, anchor=NW, image=new_image1)
        canvas_always.place(relx=0.36, rely=0.73)

        root.mainloop()