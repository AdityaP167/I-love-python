import random
print("THE HIGHER LOWER GAME")
details = {
    'Rihanna' : ['a musician and businesswoman','from Barbados',150],
    'Kendall Jenner' : ['a model and businesswoman','from USA',288],
    'Kylie Jenner' : ['a model and businesswoman','from USA',390],
    'Priyanka Chopra' : ['an actress and businesswoman','from India',87.3],
    'Virat Kohli' : ['a criketer','from India',249],
    'Deepika Padukone' : ['an actress and businesswoman','from India',74],
    'Gigi Hadid' : ['a model and businesswoman','from USA',78.3],
    'Bella Hadid' : ['a model and businesswoman','from USA',58.8],
}
current_score = 0
flag = 0
A = random.choice(list(details.items()))
while flag!=1:
    B = random.choice(list(details.items()))

    print(f"\nYour current score is: {current_score}\n")
    print(f"Compare A: {A[0]}, {A[1][0]}, {A[1][1]}")
    print("V/S")
    print(f"Compare B: {B[0]}, {B[1][0]}, {B[1][1]}")
    ans = input("\nWho do you think has more followers on instagram? A or B? :").lower()
    if ans == 'a' and A[1][2]>=B[1][2]:
        flag = 0
        current_score+=1
        A,B = B,B    #swapping
    elif ans == 'b' and A[1][2]<=B[1][2]:
        flag = 0
        current_score+=1
        A,B = B,B    #swapping
    else:
        flag = 1
        print("\nEnd of the game,you lost!")
        

print(f"Your Final Score is: {current_score}")
    
        
    
