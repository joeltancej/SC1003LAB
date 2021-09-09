def main():
    #Show welcome message
    welcomeMessage()
    #Input option
    option = get_option()
    #Dictionary of grades (With group, id as key, grade as value)
    grades = dict()
    classgroups = ['FE1', 'FE2', 'FE3', 'FE4', 'FE5', 'FE6', 'FE7', 'FE8', 'FE9', 'FE10']
    for classgroup in classgroups:
        for id in range(1, 41):
            grades[classgroup, id] = id + 30
    #If user selected to exit, exit
    if option == 6:
        print("Exited.")
        exit(0)
    
    #If user selected option 5 (list all group names)
    if option == 5:
        print("Groups:", classgroups)
        exit(0)

    #Since all other functions 1-4 require a group, ask for the group first
    group = input("Group: ")
    if group not in classgroups:
        print("Invalid input. Group should be within FE(1-10).")
        exit(1)

    #Select function based on input
    #If input is 3 (list grades in group)
    if option == 3:
        print(group+":", listGrades(grades, group))
        exit(0)

    #If input is 4 (maximum grade in a group)
    if option == 4:
        print("Highest grade:", maxGrade(grades, group))
        exit(0)

    #Functions 1 and 2 require an ID. Ask for ID
    number = input("ID: ")
    if number.isdigit() == False:
        print("Invalid ID. ID should be within 1-40.")
        exit(1)
    try:
        if int(number) not in range(1, 41):
            print("Invalid ID. ID should be within 1-40.")
            exit(1)
    except ValueError:
        print("Invalid input. ID must be a number from 1-40.")
        exit(1)

    #If input is 2 (query to get a score of a student)
    if option == 2:
        score = query(grades, group, int(number))
        print("Score:", score)
        exit(0)

    #If input is 1 (to record a grade)
    grade = input("Grade: ")
    if grade.isdigit() == False:
        print("Invalid grade. Grade should be within 0-100.")
        exit(1)
    try:
        if int(grade) not in range(0, 101):
            print("Invalid grade. Grade should be within 0-100.")
            exit(1)
    except ValueError:
        print("Invalid input. Grade should be a number from 1-100.")
        exit(1)
    inputRecord(grades, group, int(number), int(grade))
    
    print("Group:"+group, ", ID:"+number, ", Grade:"+grade)
    
    


def inputRecord(dataBase, group, id, score):
    dataBase[group, id] = score

def query(dataBase, group, id):
    return dataBase[group, id]

def listGrades(dataBase, group):
    return [dataBase[key] for key in dataBase.keys() if key[0] == group]
    grades = []
    for key in dataBase.keys():
        if key[0] == group:
            grades.append(dataBase[key])
    return grades

def maxGrade(dataBase, group):
    return max(listGrades(dataBase, group))

#Function to get option while checking for errors
def get_option():
    option = input("option: ")
    #Check if input is an integer
    if option.isdigit() == False:
        print("Invalid input. Select an option from 1-6.")
        exit(0)
    #Check if input is within 1-6
    try:
        if int(option) not in range(1,7):
            print("Invalid input. Select an option from 1-6.")
            exit(0)
    except ValueError:
        print("Invalid input. Select an option from 1-6.")
        exit(0)
    #If function is okay
    return int(option)

#Function to display welcome message
def welcomeMessage():
    welcomeText = """Welcome to the grading system! Please enter your option:
    1: input record
    2: query a student
    3: list grades in a group
    4: get max in a group
    5: list all group names
    6: exit
    """
    print(welcomeText, end="")

main()