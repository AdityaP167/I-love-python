import random
name = input("Enter player's name:")
rock ="""
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
paper = """
       .-.          
       | |    _   
   _   | |   / )  
  ( \  | |  / /   
   \ \ | | / / .-.
    \ \| |/ /.' .'
     \     `' .'  
.---. | `--   /
`--. `'   ||  |    
    \     '   /    
     |       |     
     |       |     

"""

list1 = [rock,paper,scissors]
play=0
com=0
for x in range(1,6):
    choice=input("What would you like to choose? Rock?Paper?Scissors? Type r,p,s: ")
    if (choice.lower() == 'r'):
        print(rock)
    elif (choice.lower() == 's'):
        print(scissors)
    elif (choice.lower() == 'p'):
        print(paper)
    print("Computer's choice is:")
    computer = random.choice(list1)
    print(computer)
    if(choice.lower()=='r' and computer == paper):
        com+=1
        print(f"Computer wins this round.Score is: {name}-{play} Computer-{com}")
        
    elif(choice.lower()=='r' and computer == scissors):
        play+=1
        print(f"{name} wins this round.Score is: {name}-{play} Computer-{com}")
        
    elif(choice.lower()=='p' and computer == scissors):
        com+=1
        print(f"Computer wins this round.Score is: {name}-{play} Computer-{com}")
        
    elif(choice.lower()=='p' and computer == rock):
        play+=1
        print(f"{name} wins this round.Score is: {name}-{play} Computer-{com}")
        
    elif(choice.lower()=='s' and computer == rock):
        com+=1
        print(f"Computer wins this round.Score is: {name}-{play} Computer-{com}")
        
    elif(choice.lower()=='s' and computer == paper):
        play+=1
        print(f"{name} wins this round.Score is: {name}-{play} Computer-{com}")
        
    elif(choice.lower()=='p' and computer == paper):
        print(f"Draw.Score is: {name}-{play} Computer-{com}")
        
    elif(choice.lower()=='s' and computer == scissors):
        print(f"Draw.Score is: {name}-{play} Computer-{com}")
        
    elif(choice.lower()=='r' and computer == rock):
        print(f"Draw.Score is: {name}-{play} Computer-{com}")

if(play>com):
    print(f"Hurray! {name} won the game 🎉🙌🎉")
elif(play==com):
    print("It was a draw 😕")
else:
    print("You lost Better luck next time 🙁")

    
    
