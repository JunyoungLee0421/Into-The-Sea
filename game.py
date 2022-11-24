"""
Patty Hsu
A01280249
Tim(Junyoung) Lee
A01169132
"""

import random


level_1_events = [
    {'event_type': 'riddle', 'question': 'What do you need to break before using? What am I?', 'mc_answers': ['an egg', 'a clock', 'a hand', 'a hammer'], 'answer': '1', 'hint': 'You eat these for breakfast'},
    {'event_type': 'riddle', 'question': 'I’m tall when I’m young, and I’m short when I’m old. What am I?', 'mc_answers': ['a tree', 'a waterfall', 'a candle', 'a watch'], 'answer': '3', 'hint': 'You light these when the powers out'},
    {'event_type': 'riddle', 'question': 'How many months of the year has 28 days?', 'mc_answers': ['1', '9', '11', '12'], 'answer': '4', 'hint': 'All months have more than 28 days'},
    {'event_type': 'choice', 'question': 'You see a dolphin in front of your submarine. Do you want to stop and say hi?', 'yes_choice': 'Your crew loved the dolphin! Morale and exp has increased by 1', 'no_choice': "Your crew is upset with you that you didn't stop. Morale has decreased by 1"},
    {'event_type': 'choice', 'question': 'An oyster shell is open and you see a pearl. Do you want to take the pearl?', 'yes_choice': 'The pearl is a nice trophy! Morale and exp increased by 1', 'no_choice': 'The crew respects you for not falling to greed. Morale and exp has increased by 1'},
    {'event_type': 'choice', 'question': 'A baby turtle is stuck in some plastic. Help it out?', 'yes_choice': 'The baby turtle gives the ship a high five as thanks! Morale and exp has increased by 1', 'no_choice': 'What kind of human are you?! The crew is outraged. Morale has decreased by 1'},

]

level_2_events = [
    {'event_type': 'riddle', 'question': 'What gets wet while drying?', 'mc_answers': ['towel', 'hair', 'skin', 'clothes'], 'answer': '1', 'hint': 'You use this after you shower'},
    {'event_type': 'riddle', 'question': 'I have branches, but no fruit, trunk or leaves. What am I?', 'mc_answers': ['an apple tree', 'a thought', 'a bank', 'a car'], 'answer': '3', 'hint': 'You deposit money at this place'},
    {'event_type': 'riddle', 'question': 'The more of this there is, the less you see. What is it?', 'mc_answers': ['darkness', 'sun', 'happiness', 'sadness'], 'answer': '1', 'hint': 'Hello _________ my old friend'},
    {'event_type': 'choice', 'question': 'A jellyfish is stuck on the hull of the sub. Should we try to shake it off?', 'yes_choice': 'All the shaking has made the crew sick and the jellyfish is still there. Morale has decreased by 1', 'no_choice': "The jellyfish calmly swam away. Morale and exp has increased by 1"},
    {'event_type': 'choice', 'question': 'You see some trash floating in the ocean. Pick it up?', 'yes_choice': "Great job! People who litter are the worst. Morale aned exp has increased by 1", 'no_choice': "You're part of the problem! The crew does not approve. Morale has decreased by 2"},
    {'event_type': 'choice', 'question': 'Someone in the crew offered you carbonated water. Drink the water?', 'yes_choice': "Haven't you learned Chris? Morale has decreased by 1 as have Patty's happiness.", 'no_choice': "Wow, I'm impressed! Even though I know it's a lie...Morale and exp has increased by 1"},

]

level_3_events = [
    {'event_type': 'riddle', 'question': 'David’s parents have three sons: Snap, Crackle. What’s the name of their third son?', 'mc_answers': ['Pop', 'Rice Krispie', 'Snip', 'David'], 'answer': '4', 'hint': 'Starts with a D and ends with a d'},
    {'event_type': 'riddle', 'question': 'Where does today come before yesterday?', 'mc_answers': ['your head', 'the dictionary', 'google', 'apple'], 'answer': '2', 'hint': 'Can look for meanings of words in this'},
    {'event_type': 'riddle', 'question': 'It belongs to you, but other people use it more than you do. What is it?', 'mc_answers': ['your name', 'your computer', 'your car', ], 'answer': '1', 'hint':"For you, it's Chris"},
    {'event_type': 'riddle', 'question': 'What has hands, but can’t clap?', 'mc_answers': ['your attitude', 'a clock', 'a map', 'you'], 'answer': '2', 'hint': 'it tocks, it tocks, but not tik tok'},
    {'event_type': 'choice', 'question': "One of your crew offers you some radioactive kelp to try. 'It's the bomb man! Take the kelp?", 'yes_choice': "the kelp made you sick and you threw up. The crew thinks you're uncool now. Morale has decreased by 1", 'no_choice': "The crew thinks you're uncool for not taking it. Morale has decreased by 1"},
    {'event_type': 'choice', 'question': 'OOH a shiny light...should you follow it?', 'yes_choice': "You got lured in by an anglerfish. Haven't you seen the movies? Shiny light = bad. The crew is not impressed. Morale has decreased by 1", 'no_choice': "Whew you avoided an anglerfish! The crew is thankful. Morale and exp has increased by 1"},
    {'event_type': 'choice', 'question': 'Tim and Patty have made an awesome game! Do you agree?', 'yes_choice': "Thanks :)! Morale and exp has increased by 1", 'no_choice': ":( Morale has decreased by 1"},
    {'event_type': 'choice', 'question': 'A stingray wants to play tag. Play tag with it?', 'yes_choice': "The stringray tagged you with its tail and stung your crew. They're not impressed. Morale has decreased by 1", 'no_choice': "hat's a good choice. Chances are the sting ray would have stung you when tagging you. Morale and exp has increased by 1."},
]

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
