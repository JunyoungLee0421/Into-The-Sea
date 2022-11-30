import random

level_1 = {'hp': 100, 'attack': 20}
level_2 = {'hp': 150, 'attack': 30}
level_3 = {'hp': 250, 'attack': 45}



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






def glow_up(player):
    return True

"""figure out how to print map based on player level"""