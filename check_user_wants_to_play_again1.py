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
    import unittest
    from unittest.mock import patch
    from typing import Union, List

    valid_inputs = ['y', 'n', 'Y', 'N']
    invalid_inputs: List[Union[None, int, str,
                               float]] = [None, 1, 1.5, 'a', 'yy', 'nn', 'Yy']

    class SimpleTest(unittest.TestCase):
        """Test that check_user_wants_to_play_again works."""

        @patch('__main__.input')
        def test_valid_inputs(self, mocked):
            """Test that valid_inputs are valid."""
            for i in valid_inputs:
                mocked.return_value = i
                self.assertEqual(check_user_wants_to_play_again(),
                                 i.lower() == 'y')

        @patch('__main__.input')
        def test_invalid_inputs(self, mocked):
            """Test that invalid_inputs are invalid."""
            for i in invalid_inputs:
                mocked.side_effect = i, valid_inputs[0]
                # There are only two types of valid_inputs str.lower() == 'y'
                # and str.lower() == 'n', therefore if you do an evaluation for
                # str.lower() == 'y', you replicate the functionality of the
                # function without the error checking, for testing puposes as
                # we know this is valid data
                self.assertEqual(check_user_wants_to_play_again(),
                                 valid_inputs[0].lower() == 'y')

    unittest.main()
