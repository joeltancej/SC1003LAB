#--- function get_color() ---------------------------
def get_color(color):
    keep_looping = True
    no_of_try = 1
    while keep_looping:
        #If user has not input a valid value after 3 tries, return 0
        if no_of_try > 3:
            print("3 invalid inputs: system will use the value 0")
            #leaving a line so it looks nicer
            print("")
            return 0
        #get color input
        color_str = input("Enter the value of the " + color + \
                          " color for message (0 to 255) :")
        #error checking
        try:
            #if input is not rgb
            if int(color_str) not in range(0, 256):
                #print invalid input message
                print("Invalid input. Enter a value from 0-255.")
                #increment counter
                no_of_try += 1
                print("")
                continue
            else:
                #print valid value
                print(color+":"+color_str)
                #leaving a line so it looks nicer
                print("")
                return int(color_str)
        except ValueError:
            #print invalid input message
            print("Invalid input. Enter a value from 0-255.")
            #increment counter
            no_of_try += 1
            continue