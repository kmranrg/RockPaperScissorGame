from random import choice

print("\t\tWelcome to Rock-Paper-Scissor Classic Game\n")

gameObjectsList = ["rock","paper","scissor"]

comp = choice(gameObjectsList)
print("------------------------------------------------")
user = input("\tEnter rock or paper or scissor:")
print("------------------------------------------------")

winRule1 = "rock beats scissor"
winRule2 = "paper beats rock"
winRule3 = "scissor beats paper"

winRulesList = [winRule1,winRule2,winRule3]

def winner():
    if user == comp:
        print("Your move:",user,"|| Computer's Move:",comp)
        print("------------------------------------------------")
        print("Match, tied!!!")
        print("------------------------------------------------")
    elif user+" beats "+comp in winRulesList:
        print("Your move:",user,"|| Computer's Move:",comp)
        print("==>",user.capitalize()+" beats "+comp.capitalize())
        print("------------------------------------------------")
        print("==>","Congratulations, You won!!!")
        print("------------------------------------------------")
    else:
        print("Your move:",user,"|| Computer's Move:",comp)
        print("==>",user.capitalize()+" can not beat "+comp.capitalize())
        print("------------------------------------------------")
        print("==>","You lost, try again!!!")
        print("------------------------------------------------")

winner()
