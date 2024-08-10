import random
options=("rock","paper","scissors")
player=None
computer=random.choice(options)
player=input("enter your choice (Rock , Paper , Scissors): " )
print(f" player: {player}")
print(f" computer: {computer}")
if player==computer:
    print("tie")
elif player=="rock" and computer=="scissors":
    print("you won") 
elif player=="scissors" and computer=="rock":
    print("computer won")
elif player=="paper" and computer=="scissors":
    print("computer won")
elif player=="scissors" and computer=="paper":
    print("you won")
elif player=="paper" and computer=="rock":
    print("computer won")
elif player=="rock" and computer=="paper":
    print("you won")    
else:
    print("invalid ")          

