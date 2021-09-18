#reverser function
def reverser(a_str):
    #base case
    if len(a_str) == 1:
        return a_str
    #recursive step
    else:
        new_str = reverser(a_str[1:])+ a_str[0]
        return new_str

#reverseandRepeat function
def reverseAndRepeat(a_str, repeats):
    #base case
    if len(a_str) == 1:
        return a_str
    #recursive step
    else:
        new_str = reverseAndRepeat(a_str[1:], 1)+ a_str[0]
        repeat_str = ""
        for char in new_str:
            for repetitions in range(repeats):
                repeat_str += char
        return repeat_str

#reverseandOpposite function
def reverseAndOpposite(a_str):
    #base case
    if len(a_str) == 1:
        #change character to opposite case
        if a_str.lower() == True:
            return a_str.upper()
        else:    
            return a_str.lower()
    #recursive step
    else:
        new_str = reverseAndOpposite(a_str[1:])+ a_str[0]
        #string with changed case
        newer_str = ""
        #add all the characters to the new string unchanged, less the last character
        for char in new_str:
            if char == new_str[-1]:
                if char.islower() == True:
                    newer_str += char.upper()
                else:
                    newer_str += char.lower()
            else:
                newer_str += char
        return newer_str

#symmetricString function
def symmetricString(a_str):
    #base case
    if len(a_str) == 1:
        return a_str + a_str
    #recursive step
    else:
        new_str = a_str[0] + symmetricString(a_str[1:]) + a_str[0]
        return new_str

myStr = "ABC"
mymyStr = "AbCdE"

str1 = reverseAndRepeat(myStr, 2)
str2 = reverseAndRepeat(myStr, 3)
str3 = reverseAndOpposite(mymyStr)
str4 = symmetricString(mymyStr)

print(str1)
print(str2)
print(str3)
print(str4)