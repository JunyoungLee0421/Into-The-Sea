import random

monster_events = {'event_type': 'battle', 'monster_name': 'Jelly the jellyfish', 'hp': 50, 'attack': 2 }

def sonar(user_info, game_board):
    octopus_location = [coordinate for coordinate in game_board if game_board[coordinate] == 'octopus_event']
    octopus_x_location = octopus_location[0][0]
    octopus_y_location = octopus_location[1][1]
    if user_info['x-coordinate'] < octopus_x_location:
        print("The octopus is to the West of you")
    elif user_info['x-coordinate'] > octopus_x_location:
        print("The octopus is to the East of you")
    else:
        print("You're in the same column as the octopus")

    if user_info['y-coordinate'] < octopus_y_location:
        print("The octopus is to the South of you")
    elif user_info['y-coordinate'] > octopus_y_location:
        print("The octopus is to the North of you")
    else:
        print("You're in the same row as the octopus")



def battle_event(monster, player):
    print("A challenger has appeared!!!")
    print(f"{monster['monster_name']} is staring you menacingly down")
    player_choice = input("Do you want to fight? Press 1 to fight, 2 to run away.")
    if player_choice == '1':
        while monster['hp'] > 0 and player['hp'] > 0:
            player_attack = input("Fire your torpedoes captain! Type 't' to shoot or 'q' to run away and lose morale")
            if player_attack == 't':
                attack = random.randint(range(player['torpedo_strength'], player['torpedo_strength'] + 10))
                print(f"Your attack hit! It dealt {attack} damage!")
                monster['hp'] -=  attack
                print(f"{monster['monster_name']} only has {monster['hp']} health left")
                print(f"{monster['monster_name']} is attacking now!")
                monster_attack = random.randint(range(monster['attack'] - 2, monster['attack'] + 2))
                print(f"Ouch! {monster['monster_name']} hit you for {monster_attack}")
                player['hp'] -= monster_attack
                print(f"You only have {player['hp']} health left")
            elif player_attack == 'q':
                print("Well, at least you didn't die. Crew has lost morale from the defeat")
                player['morale'] -= 1
                return player
    elif player_choice == '2':
        print(f"Sometimes running is the best option")
        return player


def glow_up(player):
    return True