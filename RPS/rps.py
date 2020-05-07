#Write by Chule
import random

def options():
    print("What would you like to do? \n")
    print("1. Play Again")
    print("2. View Statistics")
    print("3. Quit\n")
    option = int(input("Enter choice: "))
    return option

def loadGame():
    userName = input("Enter your name: ")
    try:
        savefile = open(userName+".rps","r")
        result = {"name": "", "wins": 0, "loss": 0, "tie": 0}
        i = 0
        for line in savefile:
            if i is 0:
                result['name'] = line.strip()
            elif i is 1:
                result['wins'] = int(line)
            elif i is 2:
                result['loss'] = int(line)
            elif i is 3:
                result['tie'] = int(line)
            i = i + 1
        return result
    except:
        print("Hello "+userName+" your game file does not found")
        result = loadGame()
        return result
  

def quitGame(result):
    fout = open(result["name"]+".rps","w")
    fout.write(result['name']+"\n"+str(result['wins'])+"\n"
               +str(result['loss'])+"\n"+str(result['tie']))
    fout.close()
    print(result['name']+", your game has been saved.")


def printStatistics(total,result):
    print(result['name']+", here are your game play statistics...")
    print("Wins: "+str(result['wins']))
    print("Losses: "+str(result['loss']))
    print("Ties: "+str(result['tie']))
    if result['loss'] is 0:
        print ("\nWin/Loss Ratio: 0")
    else:
        print("\nWin/Loss Ratio: "+str(round(result['wins']/result['loss'],2)))
    temp = options()
    if temp is 1:
        playGame(total + 1, result)
    elif temp is 2:
        printStatistics(total,result)
    elif temp is 3:
        quitGame(result)
    else:
        print("Enter a valid entry")
        printStatistics(total,result)
      
def getValue(x):
    if x is 1:
        return "Rock"
    elif x is 2:
        return "Paper"
    elif x is 3:
        return "Scissors"

def findWinner(user,comp):
     if user is 1 and comp is 2:
         return "comp"
     elif user is 1 and comp is 3:
         return "user"
     elif user is 2 and comp is 1:
         return "user"
     elif user is 2 and comp is 3:
         return "comp"
     elif user is 3 and comp is 1:
         return "comp"
     elif user is 3 and comp is 2:
         return "user"
     else:
         return "tie"

def playGame(total,result):
    print("Round "+str(total))
    print("\n1. Rock")
    print("2. Paper")
    print("3. Scissors\n")
    choice = int(input("What will it be? "))
    if choice <= 3 and choice >= 1:
        computerValue = random.randint(1,3)
        print(computerValue)
        winner = findWinner(choice,computerValue)
        if winner is "user":
            print("You chose "+getValue(choice)+". The computer chose "
                  +getValue(computerValue)+". You win!")
            result['wins'] = result['wins'] + 1
        elif winner is "comp":
            print("You chose " + getValue(choice) + ". The computer chose " + getValue(computerValue) + ". You lose!")
            result['loss'] = result['loss'] + 1
        elif winner is "tie":
            print("You chose " + getValue(choice) + ". The computer chose "
                  + getValue(computerValue) + ". Game Tied")
            result['tie'] = result['tie'] + 1
    else:
        print("Please enter a number that is in the range 1 to 3")
        playGame(total,result)
    temp = options()
    if temp is 1:
        playGame(total+1,result)
    elif temp is 2:
        printStatistics(total,result)
    elif temp is 3:
        quitGame(result)
    else:
        print("Enter a valid choice!")

def startNewGame():
    name = input("What is your name? ")
    print("Hello "+name+". Let's Play!")
    result = {"name":name,"wins":0,"loss":0,"tie":0}
    playGame(1,result)

print("Welcome to Rock, Paper, Scissors")
print()
print("1. Start New Game")
print("2. Load Game")
print("3. Quit")
print("")
option = int(input("Enter choice: "))
if option is 1:
    startNewGame()
elif option is 2:
    result = loadGame()
    print("Welcome back, "+result['name']+ " let's play again!")
    total = result['wins'] + result['loss'] + result['tie']
    temp = options()
    if temp is 1:
        playGame(total + 1, result)
    elif temp is 2:
        printStatistics(total, result)
    elif temp is 3:
        quitGame(result)
    else:
        print("Enter a valid choice!")