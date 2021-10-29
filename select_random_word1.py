"""Select a random word from a list and pass on a list of used words."""
from typing import Tuple, Optional, List


def select_random_word(
        used_words: List[int] = None) -> Tuple[Optional[str], List[int]]:
    """Select a random word from a list and pass on a list of used words.

    Args:
        used_words (list, optional): [description]. Defaults to None.

    Returns:
        Tuple[str, list]: The random word that is selected and a list
        of the index of every random word that has been selected.
    """
    if used_words is None:
        used_words = [0]
    return "hangman", used_words


if __name__ == "__main__":
    import unittest
    from random import sample

    list_of_words: List[str] = []

    class SimpleTest(unittest.TestCase):
        """Test that the word is in the list of words."""

        def check_word_in_list(self):
            word, _ = select_random_word()
            self.assertIn(word, list_of_words)

        def check_index_of_word(self):
            word, index_of_word = select_random_word()
            self.assertEqual(word, list_of_words[index_of_word])

        def check_index_is_correct(self):
            false_indexes = sample(range(0, len(list_of_words)), 5)
            _, index_of_word = select_random_word(false_indexes)
            for i in false_indexes:
                self.assertIn(i, index_of_word)

        def self_check_lists_are_equal(self):
            used_words = []
            words = []
            while True:
                word, used_words = select_random_word(used_words)
                if word is None:
                    break
                words.append(word)
            self.assertEqual(list_of_words.sort(), words.sort())
