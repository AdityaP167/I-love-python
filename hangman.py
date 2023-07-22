import random
import hangman_essentials as he

print(he.hangman_logo)
print("Following are to be filled up\n\n")
choice1 = random.choice(he.actors)
choice = choice1.lower()
choice_list = []

for x in range(0,len(choice)):
    if choice[x] == " ":
        choice_list.append('  ')
    else:    
        choice_list.append('- ')
print(''.join(choice_list))

guess_count = 6
print(he.hangman[0])
while guess_count !=0:        
    guess = input("\nEnter a letter:")
    if guess in choice:
        for x in range(0,len(choice)):
            if choice[x]==guess:
                choice_list[x]=guess
        print(''.join(choice_list))
        print(he.hangman[0])
    else:
        print(''.join(choice_list))
        guess_count-=1
        print(f"Incorrect guess. You have {guess_count} guesses left")
        he.hangman.pop(0)
        print(he.hangman[0])
    if '- ' not in choice_list:
        print("You did well. You saved a life")
        exit()
if guess_count==0:
    print(f"The word was {choice}")
    
    

    
