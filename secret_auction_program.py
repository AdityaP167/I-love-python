import os
#while loop to take input from the user
#fuction to find max
def max_of_dict(dictionary_name):
    maxi = 0
    for key in dictionary_name:
        if dictionary_name[key] >= maxi:
            maxi = dictionary_name[key]
            winner = key
    return winner

def clear():
    os.system('cls')

#empty dict
dict = {}
repeat = 'yes'
while repeat == 'yes':
    name = input("Enter your name:")
    bid = int(input("Enter your bid:"))
    dict[name] = bid
    repeat = input("Are there more bidders? Type 'yes' or 'no':").lower()
    clear()
    
print(dict)
print(f"The winner is {max_of_dict(dict)}")



