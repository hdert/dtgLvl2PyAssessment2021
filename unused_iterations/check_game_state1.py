"""Check if there are any _ left in the word or if hangman_state >= 9."""


def check_game_state(current_word: str, hangman_state: int) -> bool:
    """Check if there are any _ left in the word or if hangman_state >= 9.

    Args:
        current_word (str): The current state of the word that the user sees.
        hangman_state (int): The state of the hangman.

    Returns:
        bool: True if the game may continue, False if the game is over.
    """
    if hangman_state >= 9:
        return False
    for i in current_word:
        if i == '_':
            return True
    return False


if __name__ == '__main__':
    import unittest
    from typing import List, Optional

    valid_current_words: List[str] = [
        '_', 'asdf_', '_asdf', 'asdf_asdf', '____', '☭_☭'
    ]
    valid_hangman_states: List[int] = [0, 1, 2, 3, 5, 6, 7, 8]

    invalid_current_words: List[Optional[str]] = [
        '', None, "hangman", "kanban", "evidence", "problem", "decomposed",
        "components", "developed", "trialled", "assembled", "tested", "create",
        "final", "working", "outcome"
    ]

    invalid_hangman_states: List[int] = [9, 10, 123987, 65535, 65536]

    class SimpleTest(unittest.TestCase):
        """Test check_game_state()."""

        def test_check_game_state_passes(self):
            """Check that the function returns True when expected."""
            for current_word in valid_current_words:
                for hangman_state in valid_hangman_states:
                    self.assertEqual(
                        check_game_state(current_word, hangman_state), True)

        def test_check_game_state_fails(self):
            """Check that the function returns False when expected."""
            for current_word in invalid_current_words:
                for hangman_state in invalid_hangman_states:
                    self.assertEqual(
                        check_game_state(current_word, hangman_state), False)

    unittest.main()
