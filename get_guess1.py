"""Get a letter from the user."""


def get_guess() -> str:
    """Get a letter from the user.

    Returns:
        str: Return the validated letter.
    """
    while True:
        user_input = input("Please enter a letter: ")
        if not isinstance(user_input, str):
            print("Please enter a letter between a and z")
            continue
        if len(user_input) != 1:
            print("Please enter one letter")
            continue
        if not user_input.isascii():
            print("Please enter a letter between a and z")
            continue
        return user_input.lower()


if __name__ == '__main__':
    import unittest
    from unittest.mock import patch
    from random import choice
    from typing import Union, List
    invalid_inputs: List[Union[str, None, int, float]] = [
        None, 1, 2, 10, 10.11, '☭', 'â', 'ģ', 'asdf', 'âb'
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
                self.assertEqual(get_guess(), random_valid_char)

        @patch('__main__.input')
        def test_valid_inputs(self, mocked):
            """Test that get_guess() accepts every alphabetical character."""
            for i in valid_inputs:
                mocked.return_value = i
                self.assertEqual(get_guess(), i)

    unittest.main()
