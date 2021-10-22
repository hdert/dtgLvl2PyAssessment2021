"""Get the user's name for further use in the game."""


def get_name():
    """Get the user's name for further use in the game."""
    while True:
        name = input("""
        What is your name: """)
        if name and not name.isspace():
            return name


if __name__ == '__main__':
    import unittest
    from unittest import mock
    valid_user_inputs = [
        "John", "John Doe", 1, 9, 999, "1297498", "☭", "J", "Joe D'Angelo",
        "Wade McMcFace"
    ]
    invalid_user_inputs = [
        None, '', ' ', '     ', '​', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
        ' ', '⠀', ' '
    ]

    def shadow_input(return_value):
        """Return return value, whilst."""

    class SimpleTest(unittest.TestCase):
        """Test that all names are valid, apart from spaces."""

        @mock.patch('__main__.input')
        def test_valid_inputs(self, mocked):
            """Test that all valid names are returned."""
            for i in valid_user_inputs:
                mocked.return_value = i
                self.assertIs(get_name, i)

        @mock.patch('__main__.input')
        def test_invalid_inputs(self, mocked):
            """Test that all types of space are invalid inputs"""
            for i in invalid_user_inputs:
                mocked.return_value = i
