from tkinter import *
import random
import time


class Block:
    squares = ['', '', '', '', '', '', '', '', '', '']
    def __init__(self):
        self.type = None

def game_over(first):
    end = False
    index = 10

    # Horizontal
    if first.squares[0] == first.squares[1] and first.squares[2] == first.squares[1] and first.squares[0] != '':
        end, index = True, 0

    elif first.squares[3] == first.squares[4] and first.squares[5] == first.squares[4] and first.squares[3] != '':
        end, index = True, 3

    elif first.squares[6] == first.squares[7] and first.squares[8] == first.squares[7] and first.squares[6] != '':
        end, index = True, 6

    # Vertical
    elif first.squares[0] == first.squares[3] and first.squares[6] == first.squares[3] and first.squares[0] != '':
        end, index = True, 0

    elif first.squares[1] == first.squares[4] and first.squares[7] == first.squares[4] and first.squares[1] != '':
        end, index = True, 1

    elif first.squares[2] == first.squares[5] and first.squares[8] == first.squares[5] and first.squares[2] != '':
        end, index = True, 2

    # Diagonal
    elif first.squares[0] == first.squares[4] and first.squares[8] == first.squares[4] and first.squares[0] != '':
        end, index = True, 0

    elif first.squares[2] == first.squares[4] and first.squares[6] == first.squares[2] and first.squares[2] != '':
        end, index = True, 2

    # Board full
    elif turn > 9:
        end, index = True, 9

    end_message(end, index)

def end_message(end, index):
    if not end:
        return
    global user
    global single_p
    canvas.delete(ALL)
    canvas.create_text(150, 150, font=('times new roman', 30), text="!!GAMEOVER!!", fill="red", tag="Gameover")
    if index == 9:
        canvas.create_text(150, 250, font=('times new roman', 40), text="DRAW", fill="blue", tag="Gameover")
    elif index != 10:
        type = user.squares[index]
        canvas.create_text(150, 250, font=('times new roman', 40), text=(type+" WON!!!"), fill="blue", tag="Gameover")
        if single_p == True:
            if user.type == type:
                canvas.create_text(150, 50, font=('times new roman', 20), text="You won the game!", fill="green",
                                   tag="Gameover")
            else:
                canvas.create_text(150, 50, font=('times new roman', 20), text="You lost", fill="green",
                                   tag="Gameover")
        else:
            if user.type == type:
                canvas.create_text(150, 50, font=('times new roman', 20), text="User 1 won the game!", fill="green",
                                   tag="Gameover")
            else:
                canvas.create_text(150, 50, font=('times new roman', 20), text="User 2 won the game!", fill="green",
                                   tag="Gameover")


def start_game():
    global btn_single_user
    btn_single_user = Button(window, text='1 Player', width=45)
    btn_single_user.config(command=single_player)
    btn_single_user.pack()
    global btn_two_users
    btn_two_users = Button(window, text='2 Player', width=45)
    btn_two_users.config(command=two_player)
    btn_two_users.pack()

def single_player():
    global single_p
    single_p = True

    btn_two_users.destroy()
    btn_single_user.destroy()

    global user
    global bot

    if random.randint(0, 1) == 1:
        user.type = 'X'
        bot.type = 'O'
    else:
        user.type = 'O'
        bot.type = 'X'

    button_maker()
    bot_player()


def bot_press_random():
    global bot
    if turn <= 9:
        i = random.randint(0, 9 - turn)
    else:
        i = 0
    while bot.squares[i] != '':
        i += 1
    if i == 0:
        button0()
    elif i == 1:
        button1()
    elif i == 2:
        button2()
    elif i == 3:
        button3()
    elif i == 4:
        button4()
    elif i == 5:
        button5()
    elif i == 6:
        button6()
    elif i == 7:
        button7()
    elif i == 8:
        button8()


def bot_player():
    global bot
    global turn
    global single_p
    if not single_p:
        return
    if bot.type == 'X' and turn % 2 == 1:
        bot_press_random()

    elif bot.type == 'O' and turn % 2 == 0:
        bot_press_random()

def button0():
    btn1.destroy()
    global user
    global turn
    if turn % 2 == 1:
        symbol = 'X'
        color = "green"
    else:
        symbol = 'O'
        color = "blue"
    turn += 1
    canvas.create_text(50, 50, font=('arial', 50), text=symbol, fill=color, tag="Gameover")
    user.squares.pop(0)
    user.squares.insert(0, symbol)
    game_over(user)
    bot_player()
    game_over(user)

def button1():
    btn2.destroy()
    global turn
    global user
    if turn % 2 == 1:
        symbol = 'X'
        color = "green"
    else:
        symbol = 'O'
        color = "blue"
    turn += 1
    canvas.create_text(150, 50, font=('arial', 50), text=symbol, fill=color, tag="Gameover")
    user.squares.pop(1)
    user.squares.insert(1, symbol)
    game_over(user)
    bot_player()
    game_over(user)

def button2():
    btn3.destroy()
    global turn
    global user
    if turn % 2 == 1:
        symbol = 'X'
        color = "green"
    else:
        symbol = 'O'
        color = "blue"
    turn += 1
    canvas.create_text(250, 50, font=('arial', 50), text=symbol, fill=color, tag="Gameover")
    user.squares.pop(2)
    user.squares.insert(2, symbol)
    game_over(user)
    bot_player()
    game_over(user)

def button3():
    btn4.destroy()
    global turn
    global user
    if turn % 2 == 1:
        symbol = 'X'
        color = "green"
    else:
        symbol = 'O'
        color = "blue"
    turn += 1
    canvas.create_text(50, 150, font=('arial', 50), text=symbol, fill=color, tag="Gameover")
    user.squares.pop(3)
    user.squares.insert(3, symbol)
    game_over(user)
    bot_player()
    game_over(user)

def button4():
    btn5.destroy()
    global turn
    global user
    if turn % 2 == 1:
        symbol = 'X'
        color = "green"
    else:
        symbol = 'O'
        color = "blue"
    turn += 1
    canvas.create_text(150, 150, font=('arial', 50), text=symbol, fill=color, tag="Gameover")
    user.squares.pop(4)
    user.squares.insert(4, symbol)
    game_over(user)
    bot_player()
    game_over(user)

def button5():
    btn6.destroy()
    global turn
    global user
    if turn % 2 == 1:
        symbol = 'X'
        color = "green"
    else:
        symbol = 'O'
        color = "blue"
    turn += 1
    canvas.create_text(250, 150, font=('arial', 50), text=symbol, fill=color, tag="Gameover")
    user.squares.pop(5)
    user.squares.insert(5, symbol)
    game_over(user)
    bot_player()
    game_over(user)

def button6():
    btn7.destroy()
    global turn
    global user
    if turn % 2 == 1:
        symbol = 'X'
        color = "green"
    else:
        symbol = 'O'
        color = "blue"
    turn += 1
    canvas.create_text(50, 250, font=('arial', 50), text=symbol, fill=color, tag="Gameover")
    user.squares.pop(6)
    user.squares.insert(6, symbol)
    game_over(user)
    bot_player()
    game_over(user)

def button7():
    btn8.destroy()
    global turn
    global user
    if turn % 2 == 1:
        symbol = 'X'
        color = "green"
    else:
        symbol = 'O'
        color = "blue"
    turn += 1
    canvas.create_text(150, 250, font=('arial', 50), text=symbol, fill=color, tag="Gameover")
    user.squares.pop(7)
    user.squares.insert(7, symbol)
    game_over(user)
    bot_player()
    game_over(user)

def button8():
    btn9.destroy()
    global turn
    global user
    if turn % 2 == 1:
        symbol = 'X'
        color = "green"
    else:
        symbol = 'O'
        color = "blue"
    turn += 1
    canvas.create_text(250, 250, font=('arial', 50), text=symbol, fill=color, tag="Gameover")
    user.squares.pop(8)
    user.squares.insert(8, symbol)
    game_over(user)
    bot_player()
    game_over(user)

def two_player():
    global single_p
    single_p = False

    btn_two_users.destroy()
    btn_single_user.destroy()

    global user
    global user2
    user.type = 'X'
    user2.type = 'O'

    button_maker()

def button_maker():
    global btn1
    global btn2
    global btn3
    global btn4
    global btn5
    global btn6
    global btn7
    global btn8
    global btn9

    btn7 = Button(window, text='Bottom Left')
    btn7.config(command=button6)
    btn7.pack()

    btn8 = Button(window, text='Bottom Center')
    btn8.config(command=button7)
    btn8.pack()

    btn9 = Button(window, text='Bottom Right')
    btn9.config(command=button8)
    btn9.pack()

    btn4 = Button(window, text='Middle Left')
    btn4.config(command=button3)
    btn4.pack()

    btn5 = Button(window, text='Middle Center')
    btn5.config(command=button4)
    btn5.pack()

    btn6 = Button(window, text='Middle Right')
    btn6.config(command=button5)
    btn6.pack()

    btn1 = Button(window, text='Top Left')
    btn1.config(command=button0)
    btn1.pack()

    btn2 = Button(window, text='Top Center')
    btn2.config(command=button1)
    btn2.pack()

    btn3 = Button(window, text='Top Right')
    btn3.config(command=button2)
    btn3.pack()

window = Tk()
window.title("!!! TicTacToe !!!")
window.resizable(False, False)

turn = 1

canvas = Canvas(window, bg="#000000", height=300, width=300)
canvas.pack()

window.update()


user = Block()
user2 = Block()
bot = Block()

start_game()

window.mainloop()
