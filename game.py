"""
Patty Hsu
A01280249
Tim(Junyoung) Lee
A01169132
"""

import random


# make board with 10 x 10, put every room as empty room
def make_board(row, col):
    board = {}
    for i in range(0, row):
        for j in range(0, col):
            board[(i, j)] = "empty_room"
    return board


# event > temporary event
def event(level: str):
    problem_solved = False
    while problem_solved is not True:
        if level == "level_one":
            user_answer = input("Is 1 + 1 = 2? T / F ")
            if user_answer.lower() == "t":
                print("Congratulations! You solved the problem\n")
                problem_solved = True
            else:
                print("Try again")
        elif level == "level_two":
            user_answer = input("Is 3 X 2 = 5? T / F ")
            if user_answer.lower() == "f":
                print("Congratulations! You solved the problem\n")
                problem_solved = True
            else:
                print("Try again")
        elif level == "level_three":
            user_answer = input("What is 12 X 5? ")
            if user_answer == "60":
                print("Congratulations! You solved the problem\n")
                problem_solved = True
            else:
                print("Try again")


# show board with player location on it.
def show_board(board, user_info, past_location):
    player_location = (user_info['x_coordinate'], user_info['y_coordinate'])
    if board[player_location] == "level_one_event":
        event("level_one")
    elif board[player_location] == "level_two_event":
        event("level_two")
    elif board[player_location] == "level_three_event":
        event("level_three")

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
    while counter < 30:
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


# create character with inputs from user
def create_user(name: str, age: int, gender: str) -> dict:
    user_info = {
        'name': name,
        'age': age,
        'gender': gender,
        'x_coordinate': 0,
        'y_coordinate': 0,
        'level': 1,
        'exp': 0
    }
    return user_info


# move player location based on the user's input
def player_move(user_info, move_input):
    if move_input == "North":
        user_info['x_coordinate'] -= 1
    elif move_input == "South":
        user_info['x_coordinate'] += 1
    elif move_input == "East":
        user_info['y_coordinate'] += 1
    elif move_input == "West":
        user_info['y_coordinate'] -= 1
    return user_info


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
    user_name = input("Welcome! What is your name? ")
    user_age = int(input('What is your age? '))
    while True:
        user_gender = input('what is your gender? M / F ')
        if user_gender.lower() not in ('m', 'f'):
            print("Not an appropriate choice.")
        else:
            break

    user_info = create_user(user_name, user_age, user_gender)

    print(f'Welcome to this new world {user_info["name"]}, it is time to start your advencture')

    show_board(game_board, user_info, (0, 0))

    while achieved_goal is not True:
        # get input from user
        print("Current availabe option : North, South, East, West")
        user_input = input("Enter which direction you want to move : ")

        if user_input == "quit":
            break

        # save the past location
        past_location = (user_info["x_coordinate"], user_info["y_coordinate"])

        # update the player location
        player_move(user_info, user_input)

        # show board with new location
        show_board(game_board, user_info, past_location)


if __name__ == "__main__":
    main()
