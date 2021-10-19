"""Contain all of the user facing (frontend) related code of the game."""


def greeting():
    """Greet the user and explain the rules of the game."""
    print("""
Hello, and welcome to hangman. You have ten turns to guess the randomly
selected word, letter by letter. If the letter you guess is in the word
you are guessing, the letter will appear on the word. If the letter you
guess is incorrect, you will lose a turn, and another part of the
gallows will be drawn
""")
