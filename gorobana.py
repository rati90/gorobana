import random 
from copy import copy, deepcopy

all_cards = [['A', 'Heart'], ['A', 'CLUB'], ['A', 'DIAMOND'], ['A', 'SPADE'],
            ['K', 'Heart'], ['K', 'CLUB'], ['K', 'DIAMOND'], ['K', 'SPADE'], 
            ['Q', 'Heart'], ['Q', 'CLUB'], ['Q', 'DIAMOND'], ['Q', 'SPADE'], 
            ['J', 'Heart'], ['J', 'CLUB'], ['J', 'DIAMOND'], ['J', 'SPADE'], 
            ['2', 'Heart'], ['2', 'CLUB'], ['2', 'DIAMOND'], ['2', 'SPADE'], 
            ['3', 'Heart'], ['3', 'CLUB'], ['3', 'DIAMOND'], ['3', 'SPADE'], 
            ['4', 'Heart'], ['4', 'CLUB'], ['4', 'DIAMOND'], ['4', 'SPADE'], 
            ['5', 'Heart'], ['5', 'CLUB'], ['5', 'DIAMOND'], ['5', 'SPADE'], 
            ['6', 'Heart'], ['6', 'CLUB'], ['6', 'DIAMOND'], ['6', 'SPADE'], 
            ['7', 'Heart'], ['7', 'CLUB'], ['7', 'DIAMOND'], ['7', 'SPADE'], 
            ['8', 'Heart'], ['8', 'CLUB'], ['8', 'DIAMOND'], ['8', 'SPADE'], 
            ['9', 'Heart'], ['9', 'CLUB'], ['9', 'DIAMOND'], ['9', 'SPADE'], 
            ['10', 'Heart'], ['10', 'CLUB'], ['10', 'DIAMOND'], ['10', 'SPADE']]

player = []
computer = []
table = []


def start():
    random.shuffle(all_cards)


def player_play():
    if len(player) == 0:
        table.append(all_cards[0])
        print(f"\nPlayers comes {all_cards[0]}")
        all_cards.pop(0)
        player_match()
    elif len(player) > 0:
        print(f"\nPlease choice cards {player}")
        while True:
            try:
                player_choice = int(input("\nPlease choose the index: "))
                table.append(player[player_choice])
                player.pop(player_choice)
                player_match()
                break
            except ValueError:
                print("Please enter numbers in range, start from 0")
                continue
            except IndexError:
                print("Please chopse in the range")
                continue
                        
def computer_play():
    if len(computer) == 0:
        table.append(all_cards[0])
        print(f"\nComputer comes {all_cards[0]}")
        all_cards.pop(0)
        computer_match()
    elif len(computer) == 1:
        computer_choice = 0      
        table.append(computer[computer_choice])
        print(f"\nComputer comes {computer[0]}")
        computer.pop(computer_choice)
        computer_match()
    elif len(computer) > 1:
        computer_choice = random.randrange(1, len(computer))
        table.append(computer[computer_choice])
        print(f"\nComputer comes {computer[computer_choice]}")
        computer.pop(computer_choice)
        computer_match()



def player_match():
    if len(table) > 1 and table[-1][1] == table[-2][1]:
        player.extend(table[:])
        print("\nYou take all the cards")
        print(f"there are {len(all_cards)} cards left in the deck")
        table.clear()  


def computer_match():
    if len(table) > 1 and table[-1][1] == table[-2][1]:
        computer.extend(table[:])
        print("\nComputer takes all the cards")
        print(f"there are {len(all_cards)} cards left in the deck")
        table.clear()


def finish():
    if len(player) > len(computer):
        print(f"You are a looser, say oinks {len(player)} times !")
    elif len(player) < len(computer):
        print("You are a Winner")
    else:
        print("Friendship wins")


def main():       
    start()
    while len(all_cards) > 0:
        player_play()
        computer_play()
    finish()

main()


