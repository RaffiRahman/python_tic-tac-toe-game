from tkinter import *
import random

# FUNCTIONS__________________________________________________________________________
def next_turn(row, column):
    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:
        if player == players[0]:
            buttons[row][column]['text'] = player
            if check_winner() is False:
                player = players[1]
                label.config(text=player+" turns")
            elif check_winner() is True:
                label.config(text=player+" wins",fg='#94FC13')
            elif check_winner() == "Tie":
                label.config(text="Tie!")

        else:
            buttons[row][column]['text'] = player
            if check_winner() is False:
                player = players[0]
                label.config(text=player + " turns")
            elif check_winner() is True:
                label.config(text=player + " wins",fg='#94FC13')

            elif check_winner() == "Tie":
                label.config(text="Tie!")


def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg='#FDB827')
        return "Tie"

    else:
        return False

def empty_spaces():
    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True

def new_game():
    global player
    player = random.choice(players)
    label.config(text=player +" turns",fg="#EEEEEE")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg='#F15412')

# WINDOW_CONFIGURATION_______________________________________________________________
window = Tk()

window.title("Tic-Tac-Toe")
window.resizable(False, False)
window_icon = PhotoImage(file="tic-tac-toe.png")
window.iconphoto(False, window_icon)
window.configure(bg="#000000")

players = ["x","o"]
player = random.choice(players)

buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]


label = Label(text=player + " turns", font=("consolas",40),bg="#000000",fg="#EEEEEE")
label.pack(side="top")

reset_button = Button(text="Restart", font=("consolas",20),bg="#000000",fg="#EEEEEE",bd=0,
                      command=new_game)
reset_button.pack(side="bottom")

# BUTTON FRAME_________________________________________________________________________
frame = Frame(window,bg="black")
frame.pack()

# BUTTONS______________________________________________________________________________

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=("consolas",40), width=3, height=1,
                                      bg='#F15412',activebackground="#E88A1A",
                                      command= lambda row=row, column=column: next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)


window.mainloop()