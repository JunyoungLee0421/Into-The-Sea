"""
Patty Hsu
A01280249
Tim(Junyoung) Lee
A01169132
"""

import random
import itertools
import events



# make board with 10 x 10, put every room as empty room
def make_board(row, col):
    board = {}
    for i in range(0, row):
        for j in range(0, col):
            board[(i, j)] = "empty_room"
    return board


def riddle_events(riddle, player):
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


def choice_events(choice, player):
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


def battle_events():
    pass


def determine_event(board, user_info, level_1_events, level_2_events, level_3_events):
    player_location = (user_info['x_coordinate'], user_info['y_coordinate'])
    # if board[user_info[user_info]] == "event":
    #     if player['level'] == 1:
    #         event = next(itertools.cycle(level_1_events))
    #     elif player['level'] == 2:
    #         event = next(itertools.cycle(level_2_events))
    #     else:
    #         event = next(itertools.cycle(level_3_events))

    if board[player_location] == "level_one_event":
        event = next(level_1_events)
    elif board[player_location] == "level_two_event":
        event = next(level_2_events)
    else:
        event = next(level_3_events)

    if event['event_type'] == 'riddle':
        riddle_events(event, user_info)
    elif event['event_type'] == 'choice':
        choice_events(event, user_info)
    else:
        battle_events(event, user_info)


# event > temporary event
# def event(level: str, user_info: dict):
#     problem_solved = False
#     while problem_solved is not True:
#         if level == "level_one":
#             user_answer = input("Is 1 + 1 = 2? T / F ")
#             if user_answer.lower() == "t":
#                 print("Congratulations! You solved the problem\n")
#                 user_info['exp'] += 1
#                 check_player_level(user_info)
#                 print(f"Current EXP is {user_info['exp']}")
#                 print(f"Current level is {user_info['level']}")
#                 problem_solved = True
#             else:
#                 print("Try again")
#         elif level == "level_two":
#             user_answer = input("Is 3 X 2 = 5? T / F ")
#             if user_answer.lower() == "f":
#                 print("Congratulations! You solved the problem\n")
#                 problem_solved = True
#             else:
#                 print("Try again")
#         elif level == "level_three":
#             user_answer = input("What is 12 X 5? ")
#             if user_answer == "60":
#                 print("Congratulations! You solved the problem\n")
#                 problem_solved = True
#             else:
#                 print("Try again")


# show board with player location on it.
def show_board(board, user_info, past_location):
    player_location = (user_info['x_coordinate'], user_info['y_coordinate'])
    # if board[player_location] == "level_one_event":
    #     event("level_one", user_info)
    # elif board[player_location] == "level_two_event":
    #     event("level_two", user_info)
    # elif board[player_location] == "level_three_event":
    #     event("level_three", user_info)

    board[past_location] = "empty_room"

    for key in board.keys():
        if key == player_location:
            board[key] = "player_location"

    for row in range(0, 10):
        for col in range(0, 10):
            if board[(row, col)] == "player_location":
                print("\033[33m|X|\033[0m", end=" ")
            elif board[(row, col)] == "level_one_event":
                print("\033[32m|!|\033[0m", end=" ")
            elif board[(row, col)] == "level_two_event":
                print("\033[34m|!|\033[0m", end=" ")
            elif board[(row, col)] == "level_three_event":
                print("\033[31m|!|\033[0m", end=" ")
            else:
                print("|_|", end=" ")
        print()


# generate 30 events and randomly place it into the board.
def generate_events(board):
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



# create character with inputs from user
def create_user(name: str, ship_name: str) -> dict:
    user_info = {
        'name': name,
        'ship_name': ship_name,
        'x_coordinate': 0,
        'y_coordinate': 0,
        'level': 1,
        'exp': 0,
        'morale': 0
    }
    return user_info

# check if user can level up
def check_player_level(user_info):
    if user_info['exp'] <= 5:
        user_info['level'] = 1
    elif 5 < user_info['exp'] <= 10:
        user_info['level'] = 2
    else:
        user_info['level'] = 3

# move player location based on the user's input
def player_move(user_info, move_input):
    if move_input == "1":
        user_info['x_coordinate'] -= 1
    elif move_input == "2":
        user_info['x_coordinate'] += 1
    elif move_input == "3":
        user_info['y_coordinate'] += 1
    elif move_input == "4":
        user_info['y_coordinate'] -= 1
    return user_info

#  sonar function to tell users if they're close to octopus


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

#get user input for direction
def get_user_choice(user_info, game_board):

    directions = ["north", "south", "east", "west", "quit"]
    print("Curent Available Options : ", end="")
    for count, direction in enumerate(directions, start = 1):
        print(count, direction, end= " ")
    print("")
    if user_info['level'] < 3:
        user_input = input("Which direction do you want to move? ")
    else:
        user_input = input("Which direction do you want to move? Or press 's' for sonar")
        if user_input == 's':
            sonar(user_info, game_board)
            get_user_choice(user_info)

    return user_input

#validate user move
def validate_move(user, direction):
    player_location = (user['x_coordinate'], user['y_coordinate'])
    is_valid = True
    if player_location[0] == 0 and direction == "1":
        print("You're at the edge already, move in another direction!")
        is_valid = False
    elif player_location[0] == 9 and direction == "2":
        print("You're at the edge already, move in another direction!")
        is_valid = False
    elif player_location[1] == 9 and direction == "3":
        print("You're at the edge already, move in another direction!")
        is_valid = False
    elif player_location[1] == 0 and direction == "4":
        print("You're at the edge already, move in another direction!")
        is_valid = False
    return is_valid

#check if there is a challenge
def check_for_challenges(board, user_info):
    player_location = (user_info['x_coordinate'], user_info['y_coordinate'])
    if board[player_location] == "level_one_event":
        return True
    elif board[player_location] == "level_two_event":
        return True
    elif board[player_location] == "level_three_event":
        return True
    else:
        return False


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
    ship_name = input("How would you call your ship's name? : ")
    user_info = create_user(user_name, ship_name)

    print(f'Welcome to this new world {user_info["name"]}, it is time to start your advencture')

    show_board(game_board, user_info, (0, 0))
    level_1_events = itertools.cycle(events.level_1_events)
    level_2_events = itertools.cycle(events.level_2_events)
    level_3_events = itertools.cycle(events.level_3_events)
    #game starts
    while achieved_goal is not True:
        # get input from user
        direction = get_user_choice(user_info, game_board)
        if direction == "5":
            break
        valid_move = validate_move(user_info, direction)

        if valid_move:
            # save the past location
            past_location = (user_info["x_coordinate"], user_info["y_coordinate"])

            #update the player location
            player_move(user_info, direction)

            # check if there is an event
            there_is_a_challenge = check_for_challenges(game_board, user_info)

            # if user entered a challenge room
            if there_is_a_challenge is True:
                determine_event(game_board, user_info, level_1_events, level_2_events, level_3_events)

            # show board with new location
            show_board(game_board, user_info, past_location)

if __name__ == "__main__":
    main()
