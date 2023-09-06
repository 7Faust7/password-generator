#code inspired by tech with tim 
#code made and modified by 7faust7 

import random
import string

def generate_password(min_length,numbers=True, special_characters = True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    
    #to add letters,digits and special to the characters
    characters = letters
    if numbers: 
        characters += digits
    if special_characters: 
        characters += special
    #if the password is blank that it is false
    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False
    #set up to make the criteria 
    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char
        #if function to check if it have digits or special is true
        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True
        #criteria to check if there is numbers and has special for the password
        meets_criteria = True
        if numbers: 
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd 


min_length = int (input ("enter the minimum length :"))
has_number = input("do you want to have a number? (y/n)").lower () == "y"
has_special = input("do you want to have a special number? (y/n)").lower () == "y"

print("so the generated password is: ",generate_password(min_length,has_number,has_special))