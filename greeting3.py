"""Greet the user, explain the rules of the game, and how to play."""


def greeting():
    """Greet the user and explain the rules of the game."""
    input("""
Hello, and welcome to hangman. You have ten turns to guess the randomly
selected word, letter by letter. If the letter you guess is in the word
you are guessing, the letter will appear on the word. If the letter you
guess is incorrect, you will lose a turn, and another part of the
gallows will be drawn. If the entire gallows and person is drawn, which
takes ten wrong guesses, you lose the game. You win the game by guessing
the word.
There will be three panels, one will have the amount of guesses you
have left, represented as a progressively drawn gallows and man.
There is another panel which will start out as a line of underscores,
and will fill up with your correctly guessed letters, The third panel
will fill up with your incorrectly guessed letters. You can guess
letters by pressing the corresponding key on your keyboard.

Press Enter to continue""")


if __name__ == "__main__":
    import unittest

    class SimpleTest(unittest.TestCase):
        """Test greeting()."""

        def setUp(self):
            pass

        def test_greeting(self):
            """Assert that greeting() returns nothing."""
            self.assertIsNone(greeting())

        def tearDown(self):
            pass

    unittest.main()
