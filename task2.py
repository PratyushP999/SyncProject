# Rock Paper Scissor Game
# Rock="r",Paper="p", Scissor="s"
import random

def playGame(system, you):
    if system == you:
        return None

    elif system == 'r':
        if you=='s':
            return False
        elif you=='p':
            return True
    
    elif system == 'p':
        if you=='r':
            return False
        elif you=='s':
            return True
    
    elif system == 's':
        if you=='p':
            return False
        elif you=='r':
            return True

print("Sysyem Turn: Rock(r) Paper(p) or Scissor(s)?")
randNo = random.randint(1, 3) 
if randNo == 1:
    system = 'r'
elif randNo == 2:
    system = 'p'
elif randNo == 3:
    system = 's'

you = input("Your Turn: Rock(r) Paper(p) or Scissor(s)?")
a = playGame(system, you)

print(f"Computer chose {system}")
print(f"You chose {you}")

if a == None:
    print("Result: Tie")
elif a:
    print("Result: You Won")
else:
    print("Result: You Lose")