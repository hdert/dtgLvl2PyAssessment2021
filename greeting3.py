"""Greet the user, explain the rules of the game, and how to play."""


def greeting() -> None:
    """Greet the user and explain the rules of the game.

    Args:
        None
    Returns:
        None
    """
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
    from unittest import mock
    user_inputs = ['a', 'z', '1', '', ' ', 'j', 'ረ', '☭', 1]

    class SimpleTest(unittest.TestCase):
        """Test greeting()."""

        @mock.patch('__main__.input')
        def test_greeting(self, mocked):
            """Assert that greeting() returns nothing."""
            for i in user_inputs:
                mocked.return_value = i
                self.assertIsNone(greeting())

    unittest.main()
