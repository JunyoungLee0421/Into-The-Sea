"""
Patty Hsu
A01280249
Tim(Junyoung) Lee
A01169132
"""

import random
import itertools
import events
import dialogue


def make_board(rows: int, columns: int) -> dict:
    """
    Make a board based on given row, col parameters.

    :param rows: a positive non-zero integer
    :param columns: a positive non-zero integer
    :precondition: both row and col must be integers greater than 0
    :postcondition: create a board with the size of row x column
    :postcondition: each specific row x column coordinate will be stored as a tuple key with row first, then column
    :postcondition: rows and columns will start at 0, and will stop at parameter - 1
    :postcondition: each room created will be given a value of "empty_room"
    :return: board as a dictionary

    >>> make_board(1, 1)
    {(0, 0): 'empty_room'}

    >>> make_board(2, 2)
    {(0, 0): 'empty_room', (0, 1): 'empty_room', (1, 0): 'empty_room', (1, 1): 'empty_room'}
    """
    board = {}
    for row in range(0, rows):
        for column in range(0, columns):
            board[(row, column)] = "empty_room"
    return board


def riddle_events(riddle: dict, player: dict) -> dict:
    """
    Play a riddle game with player.

    :param riddle: a dictionary
    :param player: a dictionary
    :precondition: player and riddle dictionary keys must be strings
    :precondition: riddle dictionary must have a 'question' key with a string value, a 'mc_answers' key with a list
    value, an 'answer' key with a string value, and a 'hint' key with a string value
    :precondition: answer key for riddle dictionary must have corresponding number to answer as position of answer in
    mc_answers
    :precondition: player dictionary must have a 'level' key with an int value, an 'exp' key with an int value, and a
    'morale' key with an int value
    :postcondition: will print the question and give player the mc_answer options enumerated and ask player to answer
    :postcondition: player will have option to quit or ask for hints during the playing
    :postcondition: player will play until their number of tries ore used up or they guess the correct answer
    :postcondition: player exp and morale will increase if they get the answer correct
    :postcondition: player morale will decrease if they quit or get the answer wrong
    :return: player dictionary
    """
    print("Welcome! Hope you're ready to use your brain in this dolphin approved riddle!")
    print(riddle['question'])
    for choice, answer in enumerate(riddle['mc_answers'], start=1):
        print(choice, answer)

    guess_counter = player['guesses']
    while guess_counter >= 1:
        guess = input(f"Please select the number corresponding to your answer. You have {guess_counter} tries. "
                      f"Press 5 for a hint, or press 6 to give up. ")
        if guess == riddle['answer']:
            print("Wow you're so smart! That's the right answer! Exp and morale has increased by 1.")
            player['exp'] += 1
            player['morale'] += 1
            return player
        elif guess == "6":
            print("Oh no, we're sad to see you go.")
            player['morale'] -= 1
            return player
        elif guess == "5":
            print(f"Here's your hint! {riddle['hint']}")
        else:
            print("That's not the right answer, try again.")
            guess_counter -= 1

    print("Oh no, you didn't get it! The crew has lost faith in your abilities.")
    player['morale'] -= 1
    return player


def choice_events(choice: dict, player: dict) -> dict:
    """
    Play a choice game with a player.

    :param choice: a dictionary
    :param player: a dictionary
    :precondition: player and choice dictionary keys must be strings
    :precondition: choice dictionary must contain a 'question' key with a string value, a 'yes_choice' key with a string
    value, a 'no_choice' key with a string value
    :precondition: the word 'increased' must be used in the correct choice to increase player exp and morale
    :precondition: player dictionary must have a level key with an int value, an exp key with an int value, and a morale
    key with an int value
    :postcondition: will print the value of question key as a question to player
    :postcondition: player will be given option to answer yes or no to the choice
    :postcondition: player will be printed yes_choice value if they selected yes, no_choice value if they selected no
    :postcondition: player exp and morale will be increased if they selected the correct option
    :return: player dictionary
    """
    print(choice['question'])
    user_choice = input("Please input 1 for yes or 2 for no ")
    if user_choice == "1":
        print(choice['yes_choice'])
        if "increased" in choice['yes_choice']:
            player['morale'] += 1
            player['exp'] += 1
        else:
            player['morale'] -= 1
        return player
    elif user_choice == "2":
        print(choice['no_choice'])
        if "increased" in choice['no_choice']:
            player['morale'] += 1
            player['exp'] += 1
        else:
            player['morale'] -= 1
        return player


def battle_events(monster: dict, player: dict) -> dict:
    """
    Play a battle game with a player.

    :param monster: a dictionary
    :param player: a dictionary
    :precondition: player and monster dictionary keys must be strings
    :precondition: monster dictionary must contain a monster_name key with a string value, a hp key with a positive
    non-zero integer value, and an attack key with a positive non-zero integer value
    :precondition: the word 'increased' must be used in the correct choice to increase player exp and morale
    :precondition: player dictionary must have a level key with an int value, an exp key with an int value, a morale
    key with an int value, a hp key with a positive non-zero integer value, and an attack key with a positive
    non-zero integer value
    :postcondition: will introduce monster to player and give player option to fight or run away
    :postcondition: if player fights, they will always attack first
    :postcondition: a random integer generated between player attack value-5 and attack value+10 will
    be generated as their attack for their turn and dealt to the monster hp
    :postcondition: the monster will attack next, and a random integer generated between their attack value-5 and
    attack value+5 will be generated as their attack for their turn and dealt to the monster hp
    :postcondition: player will be printed out their current hp and monster current hp, and given option to continue
    fighting or to run away
    :postcondition: battle will continue until monster hp <= 0 or player hp <= 0 or player runs away
    :postcondition: if player wins battle, player exp and morale increases
    :postcondition: if player runs away, player morale decreases
    :postcondition: if player loses battle they lose the game, an ASCII art will print
    :return: player dictionary
    """
    print("A challenger has appeared!!!")
    print(f"{monster['monster_name']} is staring you menacingly down")
    player_choice = input("Do you want to fight? Press 1 to fight, 2 to run away. ")
    player_current_hp = player['hp']
    if player_choice == '1':
        while monster['hp'] > 0 and player['hp'] > 0:
            player_attack = input("Fire your torpedoes captain! Type 't' to shoot or 'q' to run away and lose morale ")
            if player_attack == 't':
                attack = random.randint(player['attack']-5, player['attack'] + 10)
                print(f"Your attack hit! It dealt {attack} damage!")
                monster['hp'] -= attack
                print(f"{monster['monster_name']} only has {monster['hp']} health left")
                print(f"{monster['monster_name']} is attacking now!")
                monster_attack = random.randint(monster['attack'] - 5, monster['attack'] + 5)
                print(f"Ouch! {monster['monster_name']} hit you for {monster_attack}")
                player['hp'] -= monster_attack
                print(f"You only have {player['hp']} health left")
            elif player_attack == 'q':
                print("Well, at least you didn't die. Crew has lost morale from the defeat.")
                player['morale'] -= 1
                return player
    elif player_choice == '2':
        print(f"Sometimes running is the best option.")
    if monster['hp'] <= 0:
        print("Great job! You slayed the monster! Morale and exp has increased by 1.")
        player['exp'] += 1
        player['morale'] += 1
        player['hp'] = player_current_hp
    if player['hp'] <= 0:
        print("OH NO!!! You've perished and the ship is sunk.")
        player['death'] = True
    return player


def determine_event(board: dict, player: dict, level_1_events: iter, level_2_events: iter, level_3_events: iter):
    """
    Determine what type and which event player will play call corresponding event.

    :param board: a dictionary
    :param player: a dictionary
    :param level_1_events: an iterable object containing dictionaries
    :param level_2_events: an iterable object containing dictionaries
    :param level_3_events: an iterable object containing dictionaries
    :precondition: player dictionary must have strings as keys
    :precondition: board dictionary must have tuples containing 2 integer coordinates as keys
    :precondition: player dictionary must have an 'row' key and a 'column' key
    :precondition: if tuple coordinates have events associated with them, must be formatted as 'level_one_event',
    'level_two_event', 'level_three_event', or 'octopus_event'
    :postcondition: will cycle through a shuffled event list and select an event
    :postcondition: all event lists must have dictionaries with a key of 'event_type'
    :postcondition: 'event_type' can have string values of 'riddle', 'choice', or 'battle'
    :postcondition: will call corresponding functions depending on what event type it is
    :postcondition: if event is 'octopus_event' will call final_game function and return after it is played
    :postcondition: if player morale reaches 0 during the events, sets death to True and player will lose
    """
    player_location = (player['row'], player['column'])
    event = {}
    if board[player_location] == "level_one_event":
        event = next(level_1_events)
    elif board[player_location] == "level_two_event":
        event = next(level_2_events)
    elif board[player_location] == "level_three_event":
        event = next(level_3_events)
    elif board[player_location] == "octopus_event":
        final_game(player)
        return

    if event['event_type'] == 'riddle':
        riddle_events(event, player)
    elif event['event_type'] == 'choice':
        choice_events(event, player)
    elif event['event_type'] == 'battle':
        battle_events(event, player)

    if player['morale'] == 0:
        player['death'] = True


def show_board(board: dict, player: dict, past_location: tuple, rows_to_show: int):
    """
    Display board based on player information

    :param board: a dictionary
    :param player: a dictionary
    :param past_location: a tuple
    :param rows_to_show: an integer
    :precondition: board must be a dictionary containing tuples as keys
    :precondition: board dictionary must have tuples containing 2 integer coordinates as keys
    :precondition: player dictionary must have an 'row' key and a 'column' key
    :precondition: rows_to_show should be a non-zero positive integer and smaller than size of row
    :precondition: past_location should contain two integers within the size of the board
    :post condition: player's current location will be displayed on the board with X symbol in yellow colour
    :post condition: event locations will be displayed on the board with ! symbol in corresponding colour
    :post condition: player's past location will be changed into an empty room
    :post condition: octopus event should not be displayed in the board
    """

    player_location = (player['row'], player['column'])
    board[past_location] = "empty_room"

    for key in board.keys():
        if key == player_location:
            board[key] = "player_location"

    for row in range(0, rows_to_show):
        for col in range(0, 10):
            if board[(row, col)] == "player_location":
                print("\033[33m|X|\033[0m", end=" ")
            elif board[(row, col)] == "level_one_event":
                print("\033[32m|!|\033[0m", end=" ")
            elif board[(row, col)] == "level_two_event":
                print("\033[34m|!|\033[0m", end=" ")
            else:
                print("|_|", end=" ")
        print()

    if 10 - rows_to_show != 0:
        for row in range(rows_to_show, 10):
            for col in range(0, 10):
                if board[(row, col)] == "player_location":
                    print("\033[33m|X|\033[0m", end=" ")
                elif col == 0:
                    print("|  ", end=" ")
                elif col == 9:
                    print("  |", end=" ")
                else:
                    print("   ", end=" ")
            print()


# generate 30 events and randomly place it into the board.
def generate_events(board: dict):
    """
    Generate random events on game board

    :param board: a dictionary
    :precondition: board must be a dictionary containing tuples as keys
    :precondition: tuple keys must contain 2 integer values representing the row and column coordinates respectively
    :postcondition: modifies the original board passed in
    :postcondition: will only overwrite an empty room, so will always generate 10 events of each level
    :postcondition: from rows 1 to 3 inclusive, will generate a level_one_event as a value to a specific key location
    :postcondition: from rows 4 to 6 inclusive, will generate a level_two_event as a value to a specific key location
    :postcondition: from rows 7 to 9 inclusive, will generate a level_three_event as a value to a specific key location
    :postcondition: from rows 7 to 9 inclusive, will generate an octopus event as a value to a specific key location
    """
    counter = 0
    while counter <= 30:
        if counter < 10:
            row = random.randint(1, 3)
            column = random.randint(0, 9)
            if board[row, column] == "empty_room":
                board[row, column] = "level_one_event"
                counter += 1
        elif counter < 20:
            row = random.randint(4, 6)
            column = random.randint(0, 9)
            if board[row, column] == "empty_room":
                board[row, column] = "level_two_event"
                counter += 1
        elif counter < 30:
            row = random.randint(7, 9)
            column = random.randint(0, 9)
            if board[row, column] == "empty_room":
                board[row, column] = "level_three_event"
                counter += 1
        elif counter == 30:
            row = random.randint(7, 9)
            column = random.randint(0, 9)
            board[row, column] = "octopus_event"
            counter += 1


def create_user(name: str, sub_name: str) -> dict:
    """
    Create player dictionary with inputs from user.

    :param name: a string
    :param sub_name: a string
    :precondition: name and sub_name must be strings
    :postcondition: creates a player with user inputted name and sub_name
    :postcondition: all players start at designated location of row 0 column 5
    :postcondition: all players start at level 1, exp 0, morale 3, hp 100, attack 20, guesses 3, treasure False,
    death False
    :return: a dictionary containing player info

    >>> test_name = "Patty"
    >>> test_sub_name = "Happy"
    >>> create_user(test_name, test_sub_name)
    {'name': 'Patty', 'sub_name': 'Happy', 'row': 0, 'column': 0, 'level': 1, 'exp': 0, 'morale': 3, 'hp': 100, 'attack': 20, 'guesses': 3, 'treasure': False, 'death': False}

    >>> test_name = "Tim"
    >>> test_sub_name = "Energized"
    >>> create_user(test_name, test_sub_name)
    {'name': 'Tim', 'sub_name': 'Energized', 'row': 0, 'column': 0, 'level': 1, 'exp': 0, 'morale': 3, 'hp': 100, 'attack': 20, 'guesses': 3, 'treasure': False, 'death': False}
    """
    player = {
        'name': name,
        'sub_name': sub_name,
        'row': 0,
        'column': 0,
        'level': 1,
        'exp': 0,
        'morale': 3,
        'hp': 100,
        'attack': 20,
        'guesses': 3,
        'treasure': False,
        'death': False,
    }
    return player


def check_player_level(player: dict) -> bool:
    """
    Check if player qualifies to level up based on their experience points.

    :param player: a dictionary
    :precondition: player must have strings as keys
    :precondition: player must have a 'level' key with an int value
    :precondition: player must have a 'exp' key with an int value
    :postcondition: determines if player qualifies for a level up based on current exp
    :postcondition: level 1 if exp <5, level 2 if exp is between 5 and 9, and level 3 if exp >= 10
    :return: True if player level has increased, False if it has not

    >>> test_player = {'level': 1, 'exp': 2}
    >>> check_player_level(test_player)
    False

    >>> test_player = {'level': 1, 'exp': 5}
    >>> check_player_level(test_player)
    True
    """
    original_level = player['level']

    if player['exp'] < 5:
        player['level'] = 1
    elif 5 <= player['exp'] < 10:
        player['level'] = 2
    else:
        player['level'] = 3

    if original_level != player['level']:
        return True
    else:
        return False


def increase_stats(player: dict) -> dict:
    """
    Increase stats when player levels up.

    :param player: a dictionary
    :precondition: player must have strings as keys
    :precondition: player must have a 'hp' key with an int value greater than 0
    :precondition: player must have a 'attack' key with an int value greater than 0
    :precondition: player must have a 'guesses' key with an int value greater than 0
    :postcondition: player 'hp' increases by 75, 'attack' goes up by 10, 'guesses' goes down by 1
    :return: player dictionary

    >>> test_player = {'hp': 10, 'attack': 10, 'guesses': 3}
    >>> increase_stats(test_player)
    {'hp': 85, 'attack': 20, 'guesses': 2}
    """
    player['hp'] += 75
    player['attack'] += 10
    player['guesses'] -= 1
    return player


# move player location based on the user's input
def player_move(player: dict, move_input: str) -> dict:
    """
    Move player to a new location based on the user's input.

    :param player: a dictionary
    :param move_input: a string
    :precondition: player dictionary must contain a key of 'x-coordinate' as a string with an integer value
    :precondition: player dictionary must contain a key of 'y-coordinate' as a string with an integer value
    :precondition: move_input can only be strings containing '1', '2', '3', or '4'
    :postcondition: will subtract player row by 1 if input is 1
    :postcondition: will add player row by 1 if input is 2
    :postcondition: will subtract player column by 1 if input is 3
    :postcondition: will add player column by 1 if input is 4
    :return: player dictionary with new coordinates

    >>> test_player = {'row': 1, 'column': 1}
    >>> test_input = '1'
    >>> player_move(test_player, test_input)
    {'row': 0, 'column': 1}
    >>> test_player = {'row': 1, 'column': 1}
    >>> test_input = '2'
    >>> player_move(test_player, test_input)
    {'row': 2, 'column': 1}
    >>> test_player = {'row': 1, 'column': 1}
    >>> test_input = '3'
    >>> player_move(test_player, test_input)
    {'row': 1, 'column': 2}
    >>> test_player = {'row': 1, 'column': 1}
    >>> test_input = '4'
    >>> player_move(test_player, test_input)
    {'row': 1, 'column': 0}

    """
    if move_input == "1":
        player['row'] -= 1
    elif move_input == "2":
        player['row'] += 1
    elif move_input == "3":
        player['column'] += 1
    elif move_input == "4":
        player['column'] -= 1
    return player


def sonar(player: dict, game_board: dict):
    """
    Inform player if they are close to octopus boss.

    :param player: a dictionary
    :param game_board: a dictionary
    :precondition: player dictionary must contain a key of 'x-coordinate' as a string with an integer value
    :precondition: player dictionary must contain a key of 'y-coordinate' as a string with an integer value
    :precondition: game_board dictionary must contain tuples as keys, and each tuple contains 2 integers
    :precondition: for each tuple, the 1st integer represents x coordinates, 2nd integer represents y coordinates
    :precondition: game_board dictionary must have a value of 'octopus_event' as a string
    :postcondition: determines the x and y locations of octopus by searching for corresponding key with a value of
    'octopus_event'
    :postcondition: if player row is less than x_location of octopus, prints a string saying
    "The octopus is to the East of you"
    :postcondition: if player row is greater than x_location of octopus, prints a string saying
    "The octopus is to the West of you"
    :postcondition: if player x and octopus x is equal, prints "You're in the same column as the octopus"
    :postcondition: if player column is greater than y_location of octopus, prints a string saying
    "The octopus is to the North of you"
    :postcondition: if player column is less than y_location of octopus, prints a string saying
    "The octopus is to the South of you"
    :postcondition: if player y and octopus y is equal, prints "You're in the same row as the octopus"

    >>> test_game_board = {(0, 0) : 'octopus_event'}
    >>> test_player = {'row': 0, 'column': 0}
    >>> sonar(test_player, test_game_board)
    You're in the same row as the octopus
    You're in the same column as the octopus
    """
    octopus_location = [coordinate for coordinate in game_board if game_board[coordinate] == 'octopus_event']
    octopus_row = octopus_location[0][0]
    octopus_column = octopus_location[0][1]
    if player['row'] < octopus_row:
        print("The octopus is to the South of you")
    elif player['row'] > octopus_row:
        print("The octopus is to the North of you")
    else:
        print("You're in the same row as the octopus")

    if player['column'] < octopus_column:
        print("The octopus is to the East of you")
    elif player['column'] > octopus_column:
        print("The octopus is to the West of you")
    else:
        print("You're in the same column as the octopus")


def get_user_choice(player: dict) -> str:
    """
    Get player input for direction they want to move.

    :param player: a dictionary
    :precondition: player must have a 'level' key in string format with an integer value
    :postcondition: player will be able to select from a list of directions enumerated
    :postcondition: players less than level 3 will select from 1 north, 2 south, 3 east, 4 west, 5 stats, 6 quit
    :postcondition: players level 3 will select 1 north, 2 south, 3 east, 4 west, 5 stats, 6 quit, or s for sonar
    :postcondition: if player inputs keys not in 123456s, they will be informed key is invalid and to reselect
    :return: user_input as a string
    """
    valid_inputs = ['1', '2', '3', '4', '5', '6', 's']
    directions = ["north", "south", "east", "west", "stats", "quit"]
    print("Current Available Options : ", end="")
    for count, direction in enumerate(directions, start=1):
        print(count, direction, end=" ")
    print("")
    acceptable_key = False
    user_input = ''
    while acceptable_key is False:
        if player['level'] < 3:
            user_input = input("Which direction do you want to move? ")
        else:
            user_input = input("Which direction do you want to move? Or press 's' for sonar ")
        if user_input in valid_inputs:
            acceptable_key = True
        else:
            print("That was not an option, please select again!")

    return user_input


def stats(player: dict):
    """
    Print player statistics to the player.

    :param player: a dictionary
    :precondition: player keys must be strings
    :precondition: player keys must contain 'name', 'sub_name', 'exp', 'morale', 'hp', 'attack'
    :postcondition: prints a simple statement regarding each of the user stats

    >>> test_player = {'name': 'Patty', 'sub_name': 'Happy', 'row': 0, 'column': 0, 'level': 1, 'exp': 0, 'morale': 3, 'hp': 100, 'attack': 20}
    >>> stats(test_player)
    Patty captain of the Happy
    Level: 1
    Exp: 0
    Morale: 3
    Battle HP: 100
    Attack: 20
    """
    print(f"{player['name']} captain of the {player['sub_name']}")
    print(f"Level: {player['level']}")
    print(f"Exp: {player['exp']}")
    print(f"Morale: {player['morale']}")
    print(f"Battle HP: {player['hp']}")
    print(f"Attack: {player['attack']}")


def validate_move(player: dict, direction: str, board: dict) -> bool:
    """
    Validate player selected movement to see if they can move in that direction based on their current location.

    :param player: a dictionary
    :param direction: a string
    :param board: a dictionary
    :precondition: player dictionary must contain a key of 'x-coordinate' as a string with an integer value
    :precondition: player dictionary must contain a key of 'y-coordinate' as a string with an integer value
    :precondition: direction must be a string containing 1, 2, 3, or 4
    :precondition: direction 1 indicates moving north, direction 2 indicates moving south,
    direction 3 indicates moving east, and direction 4 indicates moving west
    :postcondition: if player row is 0 and direction is 1, will tell them it's invalid
    :postcondition: if player row is 9 and direction is 2, will tell them it's invalid
    :postcondition: if player column is 0 and direction is 4, will tell them it's invalid
    :postcondition: if player column is 9 and direction is 3, will tell them it's invalid
    :postcondition: if player tries to go to area where they're not strong enough to go based on level, tells them
    move is not valid
    :postcondition: if player input is a 5, calls the stats function and move is considered invalid
    :postcondition: if player input is a s, calls the sonar function and move considered invalid
    :return: True if move valid, False if move invalid
    """
    is_valid = True
    if player['row'] == 0 and direction == "1":
        print("You're at the edge already, move in another direction!")
        is_valid = False
    elif player['row'] == 9 and direction == "2":
        print("You're at the edge already, move in another direction!")
        is_valid = False
    elif player['column'] == 9 and direction == "3":
        print("You're at the edge already, move in another direction!")
        is_valid = False
    elif player['column'] == 0 and direction == "4":
        print("You're at the edge already, move in another direction!")
        is_valid = False

    if player['level'] == 1 and player['row'] == 3 and direction == "2":
        print("You're not strong enough to go there yet! Pick another direction")
        is_valid = False
    if player['level'] == 2 and player['row'] == 6 and direction == "2":
        print("You're not strong enough to go there yet! Pick another direction")
        is_valid = False

    if direction == "5":
        stats(player)
        is_valid = False
    if direction == "s":
        sonar(player, board)
        is_valid = False

    return is_valid


def check_for_challenges(board: dict, player: dict) -> bool:
    """
    Check if player current location has an event associated with it.

    :param board: a dictionary
    :param player: a dictionary
    :precondition: player dictionary must contain a key of 'row' as a string with an integer value
    :precondition: player dictionary must contain a key of 'column' as a string with an integer value
    :precondition: board dictionary must have tuples containing 2 integer coordinates as keys
    :precondition: if tuple coordinates have values associated with them, must be formatted as 'empty_room' if empty
    :postcondition: determines if the current player location on board has an event associated with it
    :return: True if location on board has event, else False

    >>> test_board = {(0, 0): 'empty_room'}
    >>> test_player = {'row': 0, 'column': 0}
    >>> check_for_challenges(test_board, test_player)
    False

    >>> test_board = {(0, 0): 'event'}
    >>> test_player = {'row': 0, 'column': 0}
    >>> check_for_challenges(test_board, test_player)
    True
    """
    player_location = (player['row'], player['column'])
    if board[player_location] == "empty_room":
        return False
    else:
        return True


def determine_row(player: dict) -> int:
    """
    Determine the number of rows to print for game map depending on user level.

    :param player: a dictionary
    :precondition: player dicitonary must contain a string key 'level' with an integer value of 1, 2, or 3
    :postcondition: determines the number of rows of the map to show depending on player level
    :return: an integer representing the rows to show

    >>> test_player = {'level': 1}
    >>> determine_row(test_player)
    4
    >>> test_player = {'level': 2}
    >>> determine_row(test_player)
    7
    >>> test_player = {'level': 3}
    >>> determine_row(test_player)
    7
    """
    rows_to_show = 0
    if player['level'] == 1:
        rows_to_show = 4
    elif player['level'] >= 2:
        rows_to_show = 7
    return rows_to_show


def generate_random_number():
    """
    Generate 3 digit secret number for the final game.

    :post condition: list contains 3 randomly generated numbers
    :post condition: first number in the list should not be 0
    :post condition: 3 numbers should not have repetition
    :return: list that contains 3 randomly generated numbers
    """
    secret_number = [random.randint(1, 9)]

    while len(secret_number) < 3:
        number = random.randint(0, 9)
        if number not in secret_number:
            secret_number.append(number)

    return secret_number


def final_game(player: dict) -> dict:
    """
    Play final number guessing game with player.

    :param player: a dictionary
    :precondition: player must have a 'treasure' key as a string with a boolean False value
    :precondition: player must have a 'death' key as a string with a boolean False value
    :postcondition: calls the generate_random_number function to generate a secret number
    :postcondition: if player guesses correctly, treasure value will be set to True
    :postcondition: if player does not guess correctly, death value set to True
    :return: a player dictionary with treasure or death information updated
    """
    secret_number = generate_random_number()
    print(dialogue.octopus_ASCII)
    print(dialogue.octopus_game)

    chance = 10
    trash_talk = itertools.cycle(dialogue.octopus_trash_talk)
    while chance > 0:
        user_guess = input(f"Guess the number... you have {chance} chances left. ")
        try:
            guess_list = list(map(int, str(user_guess)))
        except ValueError:
            print("That input is invalid!!!")
            continue

        if len(guess_list) != 3:
            print("That guess is invalid!!!")
            continue

        count_a = 0
        count_b = 0

        for index in range(0, len(guess_list)):
            if guess_list[index] == secret_number[index]:
                count_a += 1
            elif guess_list[index] in secret_number:
                count_b += 1

        chance -= 1

        if count_a == 3:
            print("Congratulations... you got it right. Take your prize.")
            player['treasure'] = True
            return player
        elif chance == 0:
            print("HAHAHAHAHA!!! YOU LOST ALL YOUR CHANCES. Now, you are staying with me FOREVER!!!")
            player['death'] = True
            return player
        elif count_a == 0 and count_b == 0:
            print(next(trash_talk))
            print(f"Your hint is : {count_a} A | {count_b} B, hummm... looks like a good hint.")
        else:
            print(next(trash_talk))
            print(f"Your hint is  : {count_a} A | {count_b} B")

    return player


def execute_glow_up(player):
    """
    Print ASCII and dialogue for when players level up.
    """
    if player['level'] == 2:
        print(dialogue.level_up_ASCII)
        print(dialogue.level_2_up)
    elif player['level'] == 3:
        print(dialogue.level_up_ASCII)
        print(dialogue.level_3_up)


def intro():
    """
    Print dialogue for players to get them oriented to game.
    """
    print("I am going to go over some instructions with you. Just imagine I'm your friendly neighbourhood dolphin.")
    print(dialogue.intro_1)
    input("Whew that was a lot! Press any button when you're ready to continue ")
    print()
    print(dialogue.intro_2)
    input("I'm just trying to keep you alive! Press any button when you're done reading ")
    print()
    print(dialogue.intro_3)
    input("Are you ready for a test? Jk, press any button to start. Have fun! ")


def main():
    """
    Drive the program.
    """
    row = 10
    col = 10

    game_board = make_board(row, col)
    generate_events(game_board)

    user_name = input("Welcome! What is your name? : ")
    sub_name = input("What's your submarine's name? : ")
    player = create_user(user_name, sub_name)

    print(f"Welcome to this new world {player['name']}, We’re glad to have you on board.")
    print("Your crew is excited for the expedition to find the long lost treasure of CST Student Souls "
          "buried deep in the ocean.")
    print()
    intro()
    rows_to_show = determine_row(player)
    show_board(game_board, player, (0, 0), rows_to_show)

    level_1_events = itertools.cycle(events.level_1_events)  # generate iter objects to cycle through in game
    level_2_events = itertools.cycle(events.level_2_events)
    level_3_events = itertools.cycle(events.level_3_events)
    # game starts
    while player['treasure'] is False and player['death'] is False:  # win or lose conditions
        direction = get_user_choice(player)
        if direction == "6":  # 6 is quit, game will break and close if player selects option
            break
        valid_move = validate_move(player, direction, game_board)

        if valid_move:
            past_location = (player["row"], player["column"])  # save past location to overwrite it
            player_move(player, direction)  # move player to their selected location
            there_is_a_challenge = check_for_challenges(game_board, player)

            if there_is_a_challenge is True:  # if user entered a challenge room
                determine_event(game_board, player, level_1_events, level_2_events, level_3_events)
                if player['treasure'] is True or player['death'] is True:  # if win or lose conditions met
                    break

            if check_player_level(player):
                execute_glow_up(player)
                increase_stats(player)

            rows_to_show = determine_row(player)  # determine rows to show of map depending on player level
            show_board(game_board, player, past_location, rows_to_show)

    if player['death'] is True:
        print(dialogue.you_lose_ASCII)
    if player['treasure'] is True:
        print(dialogue.you_win_ASCII)


if __name__ == "__main__":
    main()
