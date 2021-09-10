import random

def main():
    #get 4 different random numbers
    numbers = random.sample([i for i in range(1, 10)], k = 4)
    print(numbers)

    #initialize counters
    a_counter = 0
    b_counter = 0
    try_counter = 0

    while True:
        #get user to input 4 numbers (in a row)
        usernum = input("Please input 4 digits: ")
        #checking for length of input (which should be 4)
        if len(usernum) != 4:
            print("Invalid input. Please enter 4 digits.")
            continue
        #call function number_check
        if number_check(usernum, numbers) == 1:
            #print error message
            print("Invalid input. Please enter 4 DIFFERENT numbers.")
            continue
        elif number_check(usernum, numbers) == 2:
            #print error message
            print("Invalid input. Please enter 4 digits. (Numbers from 0-9)")
            continue
        else:  
            #count the number of tries
            try_counter += 1
            #update the values of a_counter and b_counter
            a_counter, b_counter = number_check(usernum, numbers)
        #print success/progress message
        print_message(a_counter, b_counter, try_counter)


def number_check(usernum, randomnum):
    #initialize counters
    a = 0
    b = 0
    #iterate over ever number from the user's input
    for num in usernum:
        try:
            if int(num) in randomnum:
                #if the number matches AND the position matches
                if usernum.index(num) == randomnum.index(int(num)):
                    a += 1
                #if the number matches BUT the position DOES NOT match
                else:
                    b += 1
            #check if the numbers entered are all different
            if usernum.count(num) > 1:
                return 1
            else:
                continue
        except ValueError:
            return 2
    return a, b

def print_message(a_counter, b_counter, try_counter):
    if a_counter != 4:
        #print message showing progress
        print(a_counter, "A (Bulls)", b_counter, "B (Cows)")
    else:
        #success message
        print("You win!")
        print("Attempts:", try_counter)
        exit(0)

main()