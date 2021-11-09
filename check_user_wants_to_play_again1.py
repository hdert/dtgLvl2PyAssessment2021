"""Ask the user if they would like to continue playing."""


def check_user_wants_to_play_again() -> bool:
    """Ask the user if they would like to continue playing.

    Returns:
        bool: True if the user would like to continue playing, False otherwise.
    """
    while True:
        user_input = str(input("""Would you like to play some more [Y/N]: """))
        if user_input.lower() == 'y':
            return True
        if user_input.lower() == 'n':
            return False
        print("""Please enter either 'y' or 'n'.""")


if __name__ == '__main__':
    check_user_wants_to_play_again()
