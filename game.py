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


def make_board(row: int, col: int) -> dict:
    """
    Make a board based on given row, col parameters.

    :param row: a positive non-zero integer
    :param col: a positive non-zero integer
    :precondition: both row and col must be integers greater than 0
    :postcondition: create a board with the size of row x column
    :postcondition: each specific row x column coordinate will be stored as a tuple key
    :postcondition: each room created will be given a value of "empty_room"
    :return: a dictionary
    """
    board = {}
    for i in range(0, row):
        for j in range(0, col):
            board[(i, j)] = "empty_room"
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
    guess_counter = 0
    for choice, answer in enumerate(riddle['mc_answers'], start=1):
        print(choice, answer)
    if player['level'] == 1:
        guess_counter = 3
    elif player['level'] == 2:
        guess_counter = 2
    elif player['level'] == 3:
        guess_counter = 1

    while guess_counter >= 1:
        guess = input(f"Please select the number corresonding to your answer. You have {guess_counter} tries. "
                      f"Press 5 for a hint, or press 6 to give up. ")
        if guess == riddle['answer']:
            print("Wow you're so smart! That's the right answer! Exp and morale has increased by 1")
            player['exp'] += 1
            player['morale'] += 1
            return player
        elif guess == "6":
            print("Oh no, we're sad to see you go")
            return player
        elif guess == "5":
            print(f"Here's your hint! {riddle['hint']}")
        else:
            print("That's not the right answer, try again")
            guess_counter -= 1

    print("Oh no, you didn't get it! The crew has lost faith in your abilities")
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
    user_choice = input("Please input 1 for yes or 2 for no")
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
                print("Well, at least you didn't die. Crew has lost morale from the defeat")
                player['morale'] -= 1
                return player
    elif player_choice == '2':
        print(f"Sometimes running is the best option")
    if monster['hp'] <= 0:
        print("Great job! You slayed the monster! Morale and exp has increased by 1")
        player['exp'] += 1
        player['morale'] += 1
        player['hp'] = player_current_hp
    if player['hp'] <= 0:
        print("OH NO!!! You've perished and the ship is sunk")
        player['death'] = 1
    return player


def determine_event(board: dict, player: dict, level_1_events: iter, level_2_events: iter, level_3_events: iter):
    """
    Determine what type and which event player will play.

    :param board: a dictionary
    :param player: a dictionary
    :param level_1_events: an iterable object containing dictionaries
    :param level_2_events: an iterable object containing dictionaries
    :param level_3_events: an iterable object containing dictionaries
    :precondition: player dictionary must have strings as keys
    :precondition: board dictionary must have tuples containing 2 integer coordinates as keys
    :precondition: player dictionary must have an 'row' key and a 'column' key
    :precondition: if tuple coordinates have events associated with them, must be formatted as 'level_one_event',
    'level_two_event', or 'level_three_event'
    :postcondition: will cycle through a shuffled event list and select an event
    :postcondition: all event lists must have dictionaries with a key of 'event_type'
    :postcondition: 'event_type' can have string values of 'riddle', 'choice', or 'battle'
    :postcondition: will call corresponding functions depending on what even type it is
    """
    player_location = (player['row'], player['column'])
    event = {}
    if board[player_location] == "level_one_event":
        event = next(level_1_events)
    elif board[player_location] == "level_two_event":
        event = next(level_2_events)
    elif board[player_location] == "level_three_event":
        event = next(level_3_events)
    else:
        """octopus event goes here"""

    if event['event_type'] == 'riddle':
        riddle_events(event, player)
    elif event['event_type'] == 'choice':
        choice_events(event, player)
    elif event['event_type'] == 'battle':
        battle_events(event, player)


def show_board(board, player, past_location, rows_to_show):
    """
    Display board so that players
    :param board:
    :param player:
    :param past_location:
    :param rows_to_show:
    :return:
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
                if col == 0:
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
            board[row, column] = "level_one_event"
            counter += 1
        elif counter < 20:
            row = random.randint(4, 6)
            column = random.randint(0, 9)
            board[row, column] = "level_two_event"
            counter += 1
        elif counter < 30:
            row = random.randint(7, 9)
            column = random.randint(0, 9)
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
    :postcondition: all players start at level 1, exp 0, morale 3, hp 100, and attack 20
    :return: a dictionary containing player info
    """
    player = {
        'name': name,
        'sub_name': sub_name,
        'row': 0,
        'column': 0,
        'level': 3,
        'exp': 0,
        'morale': 3,
        'hp': 100,
        'attack': 20,
    }
    return player


def check_player_level(user_info):
    if user_info['exp'] <= 5:
        user_info['level'] = 1
    elif 5 < user_info['exp'] <= 10:
        user_info['level'] = 2
    else:
        user_info['level'] = 3


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
    """
    octopus_location = [coordinate for coordinate in game_board if game_board[coordinate] == 'octopus_event']
    octopus_x_location = octopus_location[0][0]
    octopus_y_location = octopus_location[0][1]
    if player['row'] < octopus_x_location:
        print("The octopus is to the East of you")
    elif player['row'] > octopus_x_location:
        print("The octopus is to the West of you")
    else:
        print("You're in the same column as the octopus")

    if player['column'] < octopus_y_location:
        print("The octopus is to the South of you")
    elif player['column'] > octopus_y_location:
        print("The octopus is to the North of you")
    else:
        print("You're in the same row as the octopus")


def get_user_choice(player: dict, game_board: dict) -> str:
    """
    Get player input for direction they want to move.

    :param player: a dictionary
    :param game_board: a dictionary
    :precondition: player must have a 'level' key in string format with an integer value
    :postcondition: player will be able to select from a list of directions enumerated
    :postcondition: 1 north, 2 south, 3 east, 4 west, 5 stats, 6 quit
    :postcondition: if user_input is 5, it will call the stats function to print user stats, and then call this function
    again to ask for movement input
    :postcondition: if user_input is s, it will call the sonar function and then call this function again to ask for
    movement input
    :return: user_input as a string
    """

    directions = ["north", "south", "east", "west", "stats", "quit"]
    print("Current Available Options : ", end="")
    for count, direction in enumerate(directions, start=1):
        print(count, direction, end=" ")
    print("")
    if player['level'] < 3:
        user_input = input("Which direction do you want to move? ")
    else:
        user_input = input("Which direction do you want to move? Or press 's' for sonar ")
        if user_input == 's':
            sonar(player, game_board)
            get_user_choice(player, game_board)
        if user_input == '5':
            stats(player)
            get_user_choice(player, game_board)

    return user_input




def stats(player: dict):
    """
    Print player statistics to the player.

    :param player: a dictionary
    :precondition: player keys must be strings
    :precondition: player keys must contain 'name', 'sub_name', 'exp', 'morale', 'hp', 'attack'
    :postcondition: prints a simple statement regarding each of the user stats
    """
    print(f"{player['name']} captain of the {player['sub_name']}")
    print(f"You are at level {player['level']}")
    print(f"Exp: {player['exp']}")
    print(f"Morale: {player['morale']}")
    print(f"Battle HP: {player['hp']}")
    print(f"Attack: {player['attack']}")


def validate_move(player: dict, direction: str, board: dict) -> bool:
    """
    Validate player selected movement to see if they can move in that direction based on their current location.

    :param player: a dictionary
    :param direction: a string
    :precondition: player dictionary must contain a key of 'x-coordinate' as a string with an integer value
    :precondition: player dictionary must contain a key of 'y-coordinate' as a string with an integer value
    :precondition: direction must be a string containing 1, 2, 3, or 4
    :precondition: direction 1 indicates moving north, direction 2 indicates moving south,
    direction 3 indicates moving east, and direction 4 indicates moving west
    :postcondition: if player row is 0 and direction is 1, will tell them it's invalid
    :postcondition: if player row is 9 and direction is 2, will tell them it's invalid
    :postcondition: if player column is 0 and direction is 4, will tell them it's invalid
    :postcondition: if player column is 9 and direction is 3, will tell them it's invalid
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
    :precondition: player dictionary must contain a key of 'x-coordinate' as a string with an integer value
    :precondition: player dictionary must contain a key of 'y-coordinate' as a string with an integer value
    :precondition: board dictionary must have tuples containing 2 integer coordinates as keys
    :precondition: if tuple coordinates have values associated with them, must be formatted as 'empty_room' if empty
    :postcondition: determines if the current player location on board has an event associated with it
    :return: True if location on board has event, else False
    """
    player_location = (player['row'], player['column'])
    if board[player_location] == "empty_room":
        return False
    else:
        return True


def determine_row(player):
    if player['level'] == 1:
        rows_to_show = 4
    elif player['level'] == 2:
        rows_to_show = 7
    else:
        rows_to_show = 10
    return rows_to_show


def intro():
    print("I am going to go over some instructions with you. Just imagine I'm your friendly neighbourhood dolphin.")
    print(dialogue.intro_1)
    input("Whew that was a lot! Press any button when you're ready to continue ")
    print()
    print(dialogue.intro_2)
    input("I'm just trying to keep you alive! Press any button when you're done reading ")
    print()
    print(dialogue.intro_3)
    input("Are you ready for a test? Jk, press any button to start. Have fun\n")

# excute the program
def main():
    # default values
    row = 10
    col = 10
    achieved_goal = False

    # create map
    game_board = make_board(row, col)

    # place events
    generate_events(game_board)

    # get user input
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
    level_1_events = itertools.cycle(events.level_1_events)
    level_2_events = itertools.cycle(events.level_2_events)
    level_3_events = itertools.cycle(events.level_3_events)
    # game starts
    while achieved_goal is not True or player['death'] != 1:
        # get input from user
        direction = get_user_choice(player, game_board)
        if direction == "6":
            break
        valid_move = validate_move(player, direction, game_board)

        if valid_move:
            # save the past location
            past_location = (player["row"], player["column"])

            # update the player location
            player_move(player, direction)

            # check if there is an event
            there_is_a_challenge = check_for_challenges(game_board, player)

            # if user entered a challenge room
            if there_is_a_challenge is True:
                determine_event(game_board, player, level_1_events, level_2_events, level_3_events)

            # check if player leveled up
            check_player_level(player)
            # determine rows to show
            rows_to_show = determine_row(player)
            # show board with new location
            show_board(game_board, player, past_location, rows_to_show)

    if player['death'] == 1:
        print('ASCII art showing death')
    if achieved_goal is True:
        print('ASCII art showing victory')


if __name__ == "__main__":
    main()
