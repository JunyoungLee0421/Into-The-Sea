import random

is_achieved_goal = False


def generate_random_number():
    # first one should not be 0
    secret_number = [random.randint(1, 9)]

    # append two more random numbers
    while len(secret_number) < 3:
        number = random.randint(0, 9)
        if number not in secret_number:
            secret_number.append(number)

    return secret_number


def final_game(goal):
    secret_number = generate_random_number()

    print(secret_number)

    chance = 10
    while chance <= 10:
        user_guess = input(f"Guess the number... you have {chance} chances left. ")

        try:
            guess_list = list(map(int, str(user_guess)))
        except ValueError:
            print("That input is invalid!!!")
            continue

        if len(guess_list) != 3:
            print("That guess is invalid!!!")
            continue

        count_A = 0
        count_B = 0

        for index in range(0, len(guess_list)):
            if guess_list[index] == secret_number[index]:
                count_A += 1
            elif guess_list[index] in secret_number:
                count_B += 1

        if count_A == 3:
            print("Congratulations... you got it right. Take your prize.")
            goal = True
            break
        elif count_A == 0 and count_B == 0:
            print("Out!")
        else:
            print(f"Your hint is  : {count_A} A | {count_B} B")

        chance -= 1
    return goal


final_game(is_achieved_goal)
