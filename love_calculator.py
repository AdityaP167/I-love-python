#love-calculator
name1=input("Enter your name:")
name2=input("Enter their name:")
last_digit = str(name1.lower().count("l") + name1.lower().count("o") + name1.lower().count("v") + name1.lower().count("e") + name2.lower().count("l") + name2.lower().count("o") + name2.lower().count("v") + name2.lower().count("e"))
first_digit = str(name1.lower().count("t") + name1.lower().count("r") + name1.lower().count("u") + name1.lower().count("e") + name2.lower().count("t") + name2.lower().count("r") + name2.lower().count("u") + name2.lower().count("e"))
print("Your love percent is "+ first_digit + last_digit +"%")
