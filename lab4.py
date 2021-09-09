from sense_hat import SenseHat
import random
import time

def main():
    sense = SenseHat()

    #colors (to use if I want more contrasting colors, better against white)
    #dark red, dark green, dark blue, dark yellow, BLACK
    dr, dg, db, dy, blk = (139, 0, 0), (0, 100, 0), (0, 0, 139), (128, 140, 0), (0, 0, 0)
    #normal colors: red, green, blue, yellow, purple
    r, g, b, y, p = (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)
    colors = [r, g, b, y, p]
    dark_colors = [dr, dg, db, dy, blk]
    #in the end the arrow colour was fixed as green and red. oh well!

    #angles for rotation
    angles = [0, 90, 180, 270]
    #dictionary mapping angles to the relevant x, y values
    xydict = {0 : (0, 1),
            90 : (-1, 0),
            180: (0, -1),
            270: (1, 0)}

    #To keep track of the player's score
    score = 0

    #set the background to white
    x = (255, 255, 255)
    #set arrow colors
    w = r
    z = g
    #list of colors for each pixel for green arrow
    green_arrow = [x, x, x, x, x, x, x, x, 
                   x, x, x, z, x, x, x, x, 
                   x, x, z, z, z, x, x, x, 
                   x, z, x, z, x, z, x, x,  
                   x, x, x, z, x, x, x, x,  
                   x, x, x, z, x, x, x, x,  
                   x, x, x, z, x, x, x, x,  
                   x, x, x, x, x, x, x, x]
    red_arrow = [x, x, x, x, x, x, x, x, 
                 x, x, x, w, x, x, x, x, 
                 x, x, w, w, w, x, x, x, 
                 x, w, x, w, x, w, x, x,  
                 x, x, x, w, x, x, x, x,  
                 x, x, x, w, x, x, x, x,  
                 x, x, x, w, x, x, x, x,  
                 x, x, x, x, x, x, x, x]

    #while loop until arrow color changes!!
    while True:
        #get a random angle
        angle = random.choice(angles)
        sense.set_rotation(angle)
        #set colors of the pixels!
        sense.set_pixels(green_arrow)
        #set time to sleep
        level = score // 5
        interval = 1 - level * 0.1
        time.sleep(interval)
        #get orientation and x&y values
        acceleration = sense.get_accelerometer_raw()
        x = round(acceleration['x'])
        y = round(acceleration['y'])
        #if orientation does not match arrow direction
        if xydict[angle] != (x, y):
            break
        #if it matches, add 1 to the score
        else:
            score += 1
        #clear display
        sense.clear()

    #after the user loses
    sense.set_pixels(red_arrow)
    time.sleep(1)
    sense.clear()
    sense.set_rotation(0)
    sense.show_message("Score: {}".format(score), text_colour = (255, 0, 0), \
                                                  back_colour = (0, 0, 255), \
                                                  scroll_speed = 0.10)
    sense.clear()

#To use if you really want RANDOM colors
#Downside: very possible for the color contrast to be low
#Hence arrow is very hard to see
def random_color():
    rgbvalues = [i for i in range(0, 256)]
    x = random.choice(rgbvalues)
    y = random.choice(rgbvalues)
    z = random.choice(rgbvalues)
    return (x, y, z)

main()
