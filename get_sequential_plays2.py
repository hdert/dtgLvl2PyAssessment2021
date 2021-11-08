"""Get the sequential number of times the player wants to play."""


def get_sequential_plays() -> int:
    """Get the sequential number of times the player wants to play.

    Returns:
        An integer between and including 1 to 10.
    """
    while True:
        try:
            plays = float(
                input("""
How many times would you like to play [1-10]: """))
        except ValueError:
            print("""
You must enter a number, e.g. 1, 5, 8, 9.""")
            continue
        if plays % 1 != 0:
            print("""
You must enter a whole number, e.g. 1, 5, 8, 9.""")
            continue
        plays = int(plays)
        if 1 <= plays <= 10:
            return plays
        print("""
The number must between from 0 and 11, e.g. 1, 5, 8, 9""")


if __name__ == '__main__':
    import unittest
    from unittest import mock
    from random import choice
    valid_user_inputs = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, '1', '2', '3', '4', '5', '6', '7', '8',
        '9', '10'
    ]
    invalid_user_inputs = [
        0, '0', 11, '11', -8, -0, -11, '-8', '-0', '-11', '☭', 'â', -0.11,
        1.123124, 2.3145, 11.134516, '-0.11', '1.123124', '2.3145',
        '11.134516', 12, 83216508, '12', '83216508', '', ' ', '   ', 1.5, 1.6,
        '1.5', '1.6'
    ]

    class SimpleTest(unittest.TestCase):
        """Test that numbers between 0 and 11 are valid, and nothing else."""

        @mock.patch('__main__.input')
        def test_valid_inputs(self, mocked):
            """Test that the list of valid inputs, is valid."""
            for i in valid_user_inputs:
                mocked.return_value = i
                self.assertEqual(get_sequential_plays(), int(i))

        @mock.patch('__main__.input')
        def test_invalid_inputs(self, mocked):
            """Test that the list of invalid inputs, is invalid."""
            for i in invalid_user_inputs:
                valid_input = choice(valid_user_inputs)
                mocked.side_effect = i, valid_input
                self.assertEqual(get_sequential_plays(), int(valid_input))

    unittest.main()
