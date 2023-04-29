"""
Jonathan Farkas' Integration project
"""
import sys
from colorama import Fore


def get_valid_move(direction, f_maze, position):
    """
    This function is used in the maze game to find if the desired movement
    direction is valid or not.
    :param direction: Desired movement of direction as inputted by the user in
    the Maze Game function
    :param f_maze: Maze as defined in Maze Game Function
    :param position: Player's current position as defined and iterated on in
    the Maze Game Function
    :return: Boolean indicating whether the player's desired movement is
    valid or not
    """
    if direction == 'w':
        if f_maze[position[0] - 1][position[1]] != '|':
            return True
        else:
            print("You bang your head into a wall, can't move that way!")
            return False
    if direction == 'a':
        if f_maze[position[0]][position[1] - 1] != '|':
            return True
        else:
            print("You bang your head into a wall, can't move that way!")
            return False
    if direction == 's':
        if f_maze[position[0] + 1][position[1]] != '|':
            return True
        else:
            print("You bang your head into a wall, can't move that way!")
            return False
    if direction == 'd':
        if f_maze[position[0]][position[1] + 1] != '|':
            return True
        else:
            print("You bang your head into a wall, can't move that way!")
            return False


def get_visible_maze(f_maze, f_visible_maze, f_position):
    """
    Function which finds the maze which is currently visible to the player
     based on their current location
    and the maze.
    :param f_maze: Maze as defined in the Maze Game function.
    :param f_visible_maze: Currently visible maze. Initially defined in Maze
    Game function, and iteratively updated each 'frame'
    :param f_position: Player's current position as defined and iterated on in
    the Maze Game function
    :return: Updated visible maze list
    """
    i = 0
    while i <= 3 and f_maze[f_position[0] - i][f_position[1]] != '|':
        f_visible_maze[f_position[0] - i - 1][f_position[1]] = \
            f_maze[f_position[0] - i - 1][f_position[1]]
        i += 1
    i = 0
    while i <= 3 and f_maze[f_position[0] + i][f_position[1]] != '|':
        f_visible_maze[f_position[0] + i + 1][f_position[1]] = \
            f_maze[f_position[0] + i + 1][f_position[1]]
        i += 1
    i = 0
    while i <= 3 and f_maze[f_position[0]][f_position[1] - i] != '|':
        f_visible_maze[f_position[0]][f_position[1] - i - 1] = \
            f_maze[f_position[0]][f_position[1] - i - 1]
        i += 1
    i = 0
    while i <= 3 and f_maze[f_position[0]][f_position[1] + i] != '|':
        f_visible_maze[f_position[0]][f_position[1] + i + 1] = \
            f_maze[f_position[0]][f_position[1] + i + 1]
        i += 1
    return f_visible_maze


def maze_game():
    """
    Maze game function with fog-of-war functionality. The game operates almost
    entirely out of a single while loop which redraws the maze as the player
    inputs movement.
    """
    maze = [
        ['|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|',
         '|', '|', '|'],
        ['|', '+', 'O', 'O', 'O', 'O', 'O', '|', 'O', '|', 'O', 'O', 'O', 'O',
         'O', 'O', '|'],
        ['|', 'O', '|', '|', 'O', '|', 'O', '|', 'O', 'O', 'O', '|', '|', '|',
         'O', '|', '|'],
        ['|', 'O', '|', 'O', '|', 'O', 'O', '|', 'O', '|', 'O', '|', 'O', 'O',
         'O', 'O', '|'],
        ['|', 'O', 'O', 'O', '|', '|', '|', 'O', '|', 'O', 'O', '|', 'O', '|',
         '|', 'O', '|'],
        ['|', 'O', '|', 'O', '|', 'O', 'O', 'O', '|', 'O', '|', 'O', '|', 'O',
         'O', 'O', '|'],
        ['|', 'O', '|', 'O', '|', 'O', '|', 'O', '|', 'O', 'O', 'O', '|', 'O',
         '|', '|', '|'],
        ['|', 'O', 'O', 'O', 'O', 'O', '|', 'O', 'O', '|', '|', 'O', '|', 'O',
         'O', 'O', '|'],
        ['|', '|', '|', '|', 'O', '|', 'O', '|', 'O', 'O', '|', 'O', '|', '|',
         '|', 'O', '|'],
        ['|', 'O', 'O', 'O', 'O', '|', 'O', '|', 'O', '|', 'O', 'O', 'O', 'O',
         '|', 'O', '|'],
        ['|', 'O', '|', '|', '|', 'O', 'O', '|', 'O', 'O', '|', '|', '|', 'O',
         '|', 'O', '|'],
        ['|', 'O', 'O', 'O', 'O', '|', 'O', '|', '|', 'O', '|', 'O', 'O', 'O',
         '|', 'O', '|'],
        ['|', '|', '|', '|', 'O', '|', 'O', 'O', 'O', 'O', '|', 'O', '|', '|',
         '|', 'O', '|'],
        ['|', 'O', 'O', 'O', 'O', 'O', '|', 'O', '|', 'O', 'O', 'O', '|', 'O',
         'O', 'O', '|'],
        ['|', 'O', '|', '|', '|', '|', 'O', 'O', 'O', '|', '|', 'O', '|', 'O',
         '|', '|', '|'],
        ['|', 'O', 'O', '|', 'O', 'O', 'O', '|', 'O', '|', 'O', 'O', '|', 'O',
         'O', '+', '|'],
        ['|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|',
         '|', '|', '|']]
    visible_maze = [
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
         'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
         'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
         'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
         'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
         'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
         'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
         'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
         'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
         'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
         'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
         'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
         'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
         'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
         'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
         'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
         'X', 'X', 'X'],
        ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
         'X', 'X', 'X'], ]
    current_pos = [1, 1]
    print("\nWelcome to the maze game!\n"
          "You will start in the top left corner of the maze, your position"
          " is indicated by a plus sign (+).\n"
          "Walls are marked with |, empty space is marked with a O, and areas"
          " you have not discovered yet with a X.\n"
          "You can use w to move up, a to move left, s to move down, "
          "and d to move right.\n\n"
          "Input 'R' to begin, and 'Q' to quit\n")
    ready = False
    while not ready:
        is_user_ready = input()
        if is_user_ready.upper() == "R":
            ready = True
        elif is_user_ready.upper() == "Q":
            main()
        else:
            print("I can wait all day..")

    # While loop which runs the maze game, with the condition for the loop to
    # stop being the current position being that of the player's goal.
    while current_pos != [15, 15]:
        visible_maze[current_pos[0]][current_pos[1]] = maze[current_pos[0]][
            current_pos[1]]

        # Calls the get_visible_maze function to update the visible_maze
        # variable based on the player's current position
        visible_maze = get_visible_maze(maze, visible_maze, current_pos)

        # Simple nested for-loop which prints the visible maze
        for i in range(17):
            print("")
            for j in range(17):
                if maze[i][j] == '+':
                    print(Fore.LIGHTGREEN_EX + visible_maze[i][j], end=' ')
                else:
                    print(Fore.LIGHTWHITE_EX + visible_maze[i][j], end=' ')

        # While loop which accepts a correct input from the player and tests
        # the validity of that input using
        # the get_valid_move function
        move_is_valid = False
        while not move_is_valid:
            movement = input("\nInput movement, H for help, or Q to quit:\n")
            while (movement != 'w' and movement != 'a') \
                    and (movement != 's' and movement != 'd'):
                if movement.upper() == 'Q':
                    main()
                if movement.upper() == 'H':
                    print("Input w to move upwards, a to move the left, "
                          "s to move downwards, or d to move to the right.")
                movement = input("\nInvalid input, try again:\n")
            move_is_valid = get_valid_move(movement, maze, current_pos)

        # if-elif chain which changes the maze arrays variables based on the
        # player's direction of movement.
        if movement == 'w':
            maze[current_pos[0] - 1][current_pos[1]] = '+'
            maze[current_pos[0]][current_pos[1]] = 'O'
            current_pos[0] -= 1
        elif movement == 'a':
            maze[current_pos[0]][current_pos[1] - 1] = '+'
            maze[current_pos[0]][current_pos[1]] = 'O'
            current_pos[1] -= 1
        elif movement == 's':
            maze[current_pos[0] + 1][current_pos[1]] = '+'
            maze[current_pos[0]][current_pos[1]] = 'O'
            current_pos[0] += 1
        elif movement == 'd':
            maze[current_pos[0]][current_pos[1] + 1] = '+'
            maze[current_pos[0]][current_pos[1]] = 'O'
            current_pos[1] += 1

    print(
        "Congratulations, you've been reunited with your long "
        "lost plus sign shaped brother!\n\n"
        "This maze was drawn by Kaylynn Harris! We hope you enjoyed :)\n\n"
        "You will now be returned to module selection")
    main()


def requirement_filler():
    """
    The Requirement Filler function fills the requirements from the previous
    sprints by solving simple math problems or demonstrating features such as
    string concatenation.
    """
    print("Welcome to the requirement filler\n"
          "the requirement filler utilizes code from my Sprint 1 project "
          "to fill out the list of required functions.")

    # Uses a while loop to find the factorial of a
    # number the user is prompted for.
    valid_input = False
    while not valid_input:
        try:
            factorial_number = int(
                input("What number would you like the factorial of?\n"))
            valid_input = True
        except:
            print("Invalid input, please enter an integer\n")
    factorial_stable = factorial_number
    factorial_multiply = factorial_number - 1
    # Inputted number is decremented by one so the first operation in
    # the while loop yields the first step in the factorial.
    while factorial_multiply > 0:
        factorial_number *= factorial_multiply
        factorial_multiply -= 1
    print("The factorial of", factorial_stable, "is", factorial_number)

    # Simple division with an option to display the remainder or not.
    # Used geeksforgeeks.org to remember the 'end=' parameter.
    # Utilizes floor division to display with no remainder
    # and the modulus function to display the remainder on its own.
    valid_input = False
    while not valid_input:
        try:
            division_numerator = float(
                input("What number would you like to be divided?\n"))
            division_divisor = float(
                input("What number would you like to be divided by?\n"))
            remainder_selection = int(
                input("Would you like the remainder?\n1. Yes\n2. No\n"))
            if remainder_selection == 1:
                remainder_result = (division_numerator / division_divisor)
                print("The quotient is", remainder_result,
                      "and the remainder is",
                      (division_numerator % division_divisor),
                      sep='-')
            else:
                remainder_result = division_numerator // division_divisor
                print("The quotient is", remainder_result)
            valid_input = True
        except:
            print(
                "One of your inputs were invalid, please limit your inputs to "
                "floats or integers where applicable\n")

    interest_principle = float(input("What is your starting balance?\n"))
    interest_rate = (float(input(
        "What is the interest rate? (For a rate of 5.2% type 5.2)\n"))) / 100
    # The rate inputted is divided by 100 to get the percentage
    valid_input = False
    while not valid_input:
        try:
            interest_period = int(
                input("How many times per year is interest applied?\n"))
            interest_years = float(
                input(
                    "How many years will you keep the "
                    "money in the account?\n"))
        except:
            print(
                "One of your inputs were invalid, please limit your inputs to "
                "floats or integers where applicable\n")

    interest_final = interest_principle * (
            (1 + (interest_rate / interest_period)) **
            (interest_period * interest_years))
    # Inputs are plugged into compound interest
    # formula which utilizes exponents.

    print("You initial investment of ", interest_principle,
          "will become %.2f" % interest_final, "after",
          interest_years, "years.")

    # Utilizes string multiplication to reflect emotional intensity
    emotion = input("How are you feeling emotionally?\n")
    emotion_intensity = 0
    while emotion_intensity < 1 or emotion_intensity > 1000:
        try:
            emotion_intensity = int(
                input("And from 1-1000, how intense is that emotion?\n"))
            if emotion_intensity < 1 or emotion_intensity > 1000:
                print(
                    "Your emotional intensity is "
                    "outside of the specified range.")
        except ValueError:
            print("Invalid input, please try again\n\n")

    print("I see, so you're feeling\n", emotion * emotion_intensity, sep='')

    print(
        "\n\n You have reached the end of the Requirement filler," +
        "you will now be returned to module selection.")
    main()


def main():
    """
    Menu function allowing the user to select between the two available
    modules.
    """
    print("\nHello and welcome to Jonathan Farkas' integration project!\n"
          "This iteration includes a maze module, "
          "along with a module which fulfills the rest of the project's "
          "requirements\n\n")
    module_selection = 0
    while module_selection != 1 and module_selection != 2 \
            and module_selection != 3:
        try:
            module_selection = int(
                input(
                    "Input the number for your desired module:"
                    "\n1. Maze Game\n2. Requirement fillers\n3. Quit\n\n"))
        except ValueError:
            print("Invalid input, please try again\n\n")
    if module_selection == 1:
        maze_game()
    if module_selection == 2:
        requirement_filler()
    if module_selection == 3:
        sys.exit()


main()
