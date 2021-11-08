"""Get a letter from the user."""
from string import ascii_letters
from typing import List, Union


def get_guess(current_word: str, wrong_guesses: List[str]) -> str:
    """Get a letter from the user.

    Args:
        current_word (str): The current state of the word.
        wrong_guesses (List[str]): The wrong guesses that the user has made.

    Returns:
        str: Return the validated letter.
    """
    while True:
        user_input = input("Please enter a letter: ")
        # Check that user_input is a string, as the next checks will
        # throw and exception if user_input isn't a string.
        if not isinstance(user_input, str):
            print("Please enter a letter between a and z")
            continue
        # Comparing the length of user input helps condense the empty
        # and too many characters checks into one check.
        if len(user_input) != 1:
            print("Please enter one letter")
            continue
        # Test if user input is alphabetical, and is ascii, in one go.
        if user_input not in ascii_letters:
            print("Please enter a letter between a and z")
            continue
        # Test if the user has entered the guess before.
        if user_input in current_word or user_input in wrong_guesses:
            print("Please enter a letter you haven't used")
            continue
        # We return user_input as lower case as everything in the program
        # is lower case.
        return user_input.lower()


if __name__ == '__main__':
    import unittest
    from unittest.mock import patch
    from random import choice, sample

    invalid_inputs: List[Union[str, None, int, float]] = [
        None, 1, 2, 10, 10.11, '☭', 'â', 'ģ', 'asdf', 'âb', '_', ' ', ''
    ]
    valid_inputs: List[str] = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]

    class SimpleTest(unittest.TestCase):
        """Test that get_guess() only accepts single alphabetic characters."""

        @patch('__main__.input')
        def test_invalid_inputs(self, mocked):
            """Test that get_guess() doesn't accept invalid characters."""
            for i in invalid_inputs:
                random_valid_char = choice(valid_inputs)
                mocked.side_effect = i, random_valid_char
                self.assertEqual(get_guess('', []), random_valid_char)

        @patch('__main__.input')
        def test_valid_inputs(self, mocked):
            """Test that get_guess() accepts every alphabetical character."""
            for i in valid_inputs:
                mocked.return_value = i
                self.assertEqual(get_guess('', []), i)

        @patch('__main__.input')
        def test_repeated_inputs(self, mocked):
            """Test that get_guess() doesn't accept repeated characters."""
            secret_word = ''.join(sample(valid_inputs, 6))
            wrong_guesses = sample(valid_inputs, 6)
            while True:
                valid_character = choice(valid_inputs)
                if (valid_character not in secret_word and
                        valid_character not in wrong_guesses):
                    break
            for character in secret_word:
                mocked.side_effect = character, valid_character
                self.assertEqual(get_guess(secret_word, wrong_guesses),
                                 valid_character)
            for character in wrong_guesses:
                mocked.side_effect = character, valid_character
                self.assertEqual(get_guess(secret_word, wrong_guesses),
                                 valid_character)

    unittest.main()
