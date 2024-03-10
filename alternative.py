# This Python program explains string operations using split(), join(),
# lower() and upper() functions
continue_loop = True # to loop using while until string operations are completed

# Get a string as an input from user
input_string = input("Please enter a sentence: ")

"""
Following string operations are performed to make each alternate
character upper case and each other alternate character lower case
using upper() and lower() function
"""
formatted_string1 = ""
formatted_string2 = []
string_length = len(input_string)

while continue_loop:
# if-else condition used to check if valid string is given as input
    if string_length==0 or input_string.isnumeric():
        input_string = input("Please enter a valid sentence: ")
        string_length = len(input_string)
    else:
# for loop to read each character to achieve desired output
        for i in range(string_length):
            if(i%2 == 0):
                upper_char = input_string[i].upper()
                formatted_string1 += upper_char
            elif(i%2 != 0):
                lower_char = input_string[i].lower()
                formatted_string1 += lower_char
            else:
                formatted_string1 += input_string[i]

# splitting input string and storing in list
        input_string = input_string.split()
        no_of_string = len(input_string)
        
# for loop to read each string to achieve desired output
        for i in range(no_of_string):
            if i%2 == 0:
                lower_string = input_string[i].lower()
                formatted_string2.append(lower_string)
            else:
                upper_string = input_string[i].upper()
                formatted_string2.append(upper_string)

        continue_loop = False # set to False, to come out of while loop
print(f"Input string formatted as per first requirement: {formatted_string1}")
print(f"Input string formatted as per 2nd requirement: {" " .join(formatted_string2)}")