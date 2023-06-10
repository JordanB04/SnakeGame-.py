from tkinter import *
import random
from tkinter import font
from turtle import speed
from turtle import window_height, window_width


window = Tk()
window.title("SNAKE GAME BY JB")
window.resizable(0,0)

label = Label(window, font='Times 20 bold', text='Snake Game By Jordan Broomfield').pack(side=BOTTOM)#footer
score = 0
direction = 'down'
Height_G = 500
Game_Width = 500
Snake_Speed = 50
space_area = 20
BODY_PARTS = 4
SNAKE_COLOUR = '#0000FF'
FOOD_COLOUR = '#FF4040'


Label = Label(window, bg= "Blue", text = 'score:{}'.format(score), font=('gameplay', 50))
Label.pack()


canvas = Canvas(window, bg="Orange", height= Height_G, width= Game_Width  )
canvas.pack()


class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0,0])
        for x,y in self.coordinates:
            square = canvas.create_oval(x , y,  x + space_area, y +space_area, fill = SNAKE_COLOUR, tag = "snake")
            self.squares.append(square)
        


class Food:
    def __init__(self):
        x = random.randint(0, (Game_Width/space_area) - 1)* space_area
        y = random.randint(0, (Height_G/space_area) - 1)* space_area

        self.coordinates = [x,y]
        canvas.create_oval(x, y,  x + space_area, y +space_area, fill= FOOD_COLOUR, tag = 'food')

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2 , canvas.winfo_height()/2, font=("Time 60 bold"), text="GAME OVER", fill="Blue", tag="game over")


def next_turn(snake,food):
    x,y = snake.coordinates[0]
    if direction == 'up':
        y = y - space_area
    elif direction == 'down':
        y = y + space_area
    elif direction == 'left':
        x = x - space_area
    elif direction == 'right':
        x = x + space_area


    snake.coordinates.insert(0, (x,y))
    square = canvas.create_rectangle(x, y, x + space_area, y + space_area, fill = SNAKE_COLOUR )
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score

        score =  score + 1
        Label.config(text = 'score:{}'. format(score))
        canvas.delete("food")
        food = Food()

    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over()

    else:
        window.after(Snake_Speed, next_turn, snake, food)

def change_direction(new_direction):
    global direction
    if direction == "left":
        #if direction != "right":
        direction = new_direction
    elif direction == "right":
        #if direction != "left":
        direction = new_direction
    elif direction == "up":
        #if direction != "down":
        direction = new_direction
    elif direction == "down":
        #if direction != "up": 
        direction = new_direction

def check_collisions(snake):
    x,y = snake.coordinates[0]
    if x<0 or x >= Game_Width:
        return True
    elif y < 0 or y >= Game_Width:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    



window.update()

window_width = window.winfo_width()
window_height =window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind("<Left>", lambda event:change_direction('left'))
window.bind("<Right>", lambda event:change_direction('right'))
window.bind("<Up>", lambda event:change_direction('up'))
window.bind("<Down>", lambda event:change_direction('down'))

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()