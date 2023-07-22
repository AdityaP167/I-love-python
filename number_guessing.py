import random
print('''
   _____                       _______ _            _   _                 _               
  / ____|                     |__   __| |          | \ | |               | |              
 | |  __ _   _  ___  ___ ___     | |  | |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __|    | |  | '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \    | |  | | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/    |_|  |_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   
''')
print("""Welcome to the number guessing game!
I'm thinking of a number between 1 to 100.""")
diff = input("Choose a difficulty level.Type 'easy' or 'hard':").lower()
if diff == 'easy':
    attempts = 10
elif diff == 'hard':
    attempts = 5
else:
    print("Check your spellings.")
    exit()

ans = random.randint(1,100)

for i in range(0,attempts):
    print(f"You have {attempts} attempts remaining to guess the number")
    guess = int(input("Make a guess:"))
    if guess == ans:
        print(f"You got it! The ans was {ans}")
        break
    elif guess>ans and attempts!=1:
        print("""Too High.
Guess again.""")
        attempts -= 1
    elif guess<ans and attempts!=1:
        print("""Too Low.
Guess again.""")
        attempts -= 1
if attempts == 1 and guess!=ans:
    print(f"YOU LOST! The number was {ans}")
    

