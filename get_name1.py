"""Get the user's name for further use in the game."""


def get_name() -> str:
    """Get the user's name for further use in the game.

    Args:
        None
    Returns:
        str: The name the player has entered.
    """
    while True:
        name = str(input("""
What is your name: """))
        if name and not name.isspace():
            return name
        print("""
Name cannot be a space.""")


if __name__ == '__main__':
    import unittest
    from unittest import mock
    from random import choice
    valid_user_inputs = [
        "John", "John Doe", 1, 9, 999, "1297498", "☭", "J", "Joe D'Angelo",
        "Wade McMcFace",
        "Adolph Blaine Charles David Earl Frederick Gerald Hubert Irvin John"
        "Kenneth Lloyd Martin Nero Oliver Paul Quincy Randolph Sherman Thomas"
        "Uncas Victor William Xerxes Yancy Zeus Wolfeschlegel­steinhausen­berg"
        "erdorff­welche­vor­altern­waren­gewissenhaft­schafers­wessen­schafe­w"
        "aren­wohl­gepflege­und­sorgfaltigkeit­beschutzen­vor­angreifen­durch­"
        "ihr­raubgierig­feinde­welche­vor­altern­zwolfhundert­tausend­jahres­v"
        "oran­die­erscheinen­von­der­erste­erdemensch­der­raumschiff­genacht­m"
        "it­tungstein­und­sieben­iridium­elektrisch­motors­gebrauch­licht­als­"
        "sein­ursprung­von­kraft­gestart­sein­lange­fahrt­hinzwischen­sternart"
        "ig­raum­auf­der­suchen­nachbarschaft­der­stern­welche­gehabt­bewohnba"
        "r­planeten­kreise­drehen­sich­und­wohin­der­neue­rasse­von­verstandig"
        "­menschlichkeit­konnte­fortpflanzen­und­sich­erfreuen­an­lebenslangli"
        "ch­freude­und­ruhe­mit­nicht­ein­furcht­vor­angreifen­vor­anderer­int"
        "elligent­geschopfs­von­hinzwischen­sternartig­raum Sr."
    ]
    invalid_user_inputs = [
        '', ' ', '     ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
        '     '
    ]

    class SimpleTest(unittest.TestCase):
        """Test that all names are valid, apart from spaces."""

        @mock.patch('__main__.input')
        def test_valid_inputs(self, mocked):
            """Test that all valid names are returned."""
            for i in valid_user_inputs:
                mocked.return_value = i
                self.assertEqual(get_name(), str(i))

        @mock.patch('__main__.input')
        def test_invalid_inputs(self, mocked):
            """Test that all types of space are invalid inputs."""
            for i in invalid_user_inputs:
                valid_input = choice(valid_user_inputs)
                mocked.side_effect = [i, valid_input]
                self.assertEqual(get_name(), str(valid_input))

    unittest.main()
