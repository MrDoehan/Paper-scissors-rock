import random
lost = "You lost"
win = "You win"

outcomes = {1: "paper", 2: "scissors", 3: "rock"}

def roll(sides=6):
  num = random.randint(1, 3)
  return num
def main():
  game = True
  while game:
    go_again = input("Ready to play? y/n: ")
    if go_again.lower() == "y":
      
      chosen = input("paper/scissors/rock: ")
      num = roll(outcomes)
      best = outcomes.get(num)
       
      if chosen == "paper" and best == "scissors":
        print(f"They picked {best}")
        print(lost)
      elif chosen == "scissors" and best == "rock":
        
        print(f"They picked {best}")
        print(lost)
      elif chosen == "rock" and best == "paper":
        print(f"They picked {best}")
        print(lost)  
      elif chosen == best:
        print(f"They picked {best}")
        print("Tie")
      elif chosen == "scissors" and best == "paper":
        
        print(f"They picked {best}")
        print(win)
      elif chosen == "rock" and best == "scissors":
        print(f"They picked {best}")
        print(win)
      elif chosen == "paper" and best == "rock":
        print(f"They picked {best}")
        print(win) 
    else:
      game = False
      
main()
