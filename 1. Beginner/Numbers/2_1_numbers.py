""" Write a function that takes two arguments, 145 and 'o' , and uses the `format` function to return a formatted string. Print the result. Try to identify the representation used. """

#-------- Function for formating --------#
def formated_string(number, character):
    return "You entered number {} and the character {}.".format(number, character)

#----- The "result" string becomes "You entered number 145 and the character o." -----#
result = formated_string(145, 'o')

#-------- Printing formated string --------#
print(result)

# ----- Exit Program ----- #
exit()