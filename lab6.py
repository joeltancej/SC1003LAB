from sense_hat import SenseHat
import time

#some colors
r, g, b, y, p, w = (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (255, 255, 255)

# This function checks the pitch value and the x coordinate  
# to determine whether to move the marble in the x-direction.
# Similarly, it checks the roll value and y coordinate to
# determine whether to move the marble in the y-direction.
def move_marble(pitch,roll,x,y): 
    new_x = x    #assume no change to start with
    new_y = y    #assume no change to start with
    if 1 < pitch < 179 and x != 0: 
        new_x -= 1    # move left
    elif 359 > pitch > 179 and x != 7: 
        new_x += 1    # move right
    if 1 < roll < 179 and y != 7: 
        new_y += 1    # move up
    elif 359 > roll > 179 and y != 0: 
        new_y -= 1    # move down
    new_x,new_y = check_wall(x,y,new_x,new_y) 
    return new_x, new_y

def check_wall(x,y,new_x,new_y): 
    if board[new_y][new_x] != r: 
        return new_x, new_y 
    elif board[new_y][x] != r: 
        return x, new_y 
    elif board[y][new_x] != r:
        return new_x, y 
    else:
        return x,y

sense = SenseHat()
#2d board WITH BOUNDARY and MAZE and TARGET
board = [[r,r,r,b,b,b,b,r], 
         [r,b,b,b,b,b,b,r],
         [b,b,b,b,g,r,b,r],
         [b,r,r,b,r,r,b,r],
         [b,b,b,b,b,b,b,b],
         [b,r,b,r,r,b,b,b],
         [b,b,b,r,b,b,b,r], 
         [r,r,b,b,b,r,r,r] ]
y = 2				# y coordinate of marble
x = 2				# x coordinate of marble
board[y][x] = w		# a white marble
board_1D = sum(board,[])        # convert to 1-dimension list
print(board_1D)               # for code debugging
sense.set_pixels(board_1D)    # display it
game_over = False   #status of game

while not game_over:
    #get pitch and roll
    pitch = sense.get_orientation()["pitch"]
    roll = sense.get_orientation()["roll"]
    #keep old x, y values
    oldx, oldy = x, y
    #get new x, y values
    x, y = move_marble(pitch, roll, x, y)
    print(x, y)
    #if marble reaches the TARGET, send message and end game
    if board[y][x] == g:
        sense.clear()
        print("yay")
        sense.show_message("yay!", text_colour = (255, 0, 0), \
                                    back_colour = (0, 0, 255), \
                                    scroll_speed = 0.5)
        game_over == True
        continue
    #revert previous location of marble to black
    board[oldy][oldx] = b
    #new location of white marble
    board[y][x] = w
    # convert to 1-dimension list
    board_1D = sum(board,[])
    #display board
    sense.set_pixels(board_1D)
    #sleep 0.05s
    time.sleep(0.05)
