# snake - gun - water
import random
# list of word
game_list = ['snake','gun','water']
user_score = 0
computer_score = 0
# this loop run three times
print("=========Wellcome our game - SNAKE WATER GUN=========\n")
for _ in range(3):
    #user input
   
    user_choise = str(input("Enter any (snake, gun, water): "))
    #random word choice
    computer_choise = str(random.choice(game_list)).lower()

    #print choices
    print(f"Youe select: {user_choise}")
    print(f"Computer select: {computer_choise}")
    print()

    #condition check
    if user_choise == computer_choise:
        print("Game Draw😭")
    elif user_choise=='snake'and computer_choise=='water'\
        or user_choise =='gun' and computer_choise=='snkae'\
        or user_choise == 'water' and computer_choise == 'gun':
            print("You win,  1 point")
            user_score += 1 
    else:
         print("you loss, computer win")
         computer_score+=1
    
# game score
print()
print("Result: ")
print(f"your score: {user_score}")
print(f"computer score: {computer_score}")
if(user_score == computer_score):
        print("Game draw")

elif user_score > computer_score:
      print("you win")
else:
      print("computer win")



