"""Calculate the user's final score."""
from typing import List


def calculate_score(secret_word: str, wrong_guesses: List[str]) -> int:
    """Calculate the user's final score.

    Args:
        secret_word (str): The secret word.
        wrong_guesses (List[str]): The list of wrong guesses

    Returns:
        int: The score for the game.
    """
    # We need to round the final value, as we use division and want to return
    # an integer. We add to the length of wrong_guesses, as if the user has
    # no wrong guesses, we get a divide by zero error. This approach was chosen
    # instead of rounding zero up to one, as that would give a player who made
    # one mistake, the same final score as a player who made zero mistakes.
    # We then multiply the result by 1000 to give an arcady feel.
    return round((len(secret_word) / (len(wrong_guesses) + 1)) * 1000)


if __name__ == '__main__':
    import unittest

    class SimpleTest(unittest.TestCase):
        """Test that calculate_score() works."""

        def test_calculate_score(self):
            """Test that calculate_score() works."""
            list_of_wrong_guesses = []
            for length_of_word in range(10):
                for _ in range(10):
                    self.assertEqual(
                        calculate_score('*' * length_of_word,
                                        list_of_wrong_guesses),
                        round(length_of_word /
                              (len(list_of_wrong_guesses) + 1) * 1000))
                    # append afterwards to test if an empty list works.
                    list_of_wrong_guesses.append(None)

    unittest.main()
