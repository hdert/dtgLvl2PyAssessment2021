"""Select a random word from a list and pass on a list of used words."""
from typing import Tuple, Optional, List
from random import randint, sample


def select_random_word(
        used_words: List[int]) -> Tuple[Optional[str], List[int]]:
    """Select a random word from a list and pass on a list of used words.

    Args:
        used_words (list): A list of the indexes of every already used word.

    Returns:
        Tuple[Optional[str], list]: The random word that is selected and a list
        of the index of every random word that has been selected.
    """
    list_of_words: List[str] = [
        "hangman", "kanban", "evidence", "problem", "decomposed", "components",
        "developed", "trialled", "assembled", "tested", "create", "final",
        "working", "outcome"
    ]
    if len(used_words) == len(list_of_words):
        # if len(used_words) == len(list_of_words), when line 26 and 27
        # run, it will just delete every word from list_of_words, so we
        # save the computational energy, and another if statement to check
        # if list_of_words_without_used_words is empty, and just return
        # None as the word, thus signalling to the caller, that the word
        # list is empty.
        return None, used_words
    list_of_words_without_used_words: List[str] = list_of_words.copy()
    for i in sorted(used_words, reverse=True):
        # used_words is looped through in reverse for this as, when in
        # reverse, the 'popping' of an list item at index 'i' will
        # never effect a higher index list item, as that higher index
        # list item has already been popped.
        list_of_words_without_used_words.pop(i)
    # len(list_of_words_without_used_words) - 1 because, lists start
    # at index 0.
    random_number: int = randint(0, len(list_of_words_without_used_words) - 1)
    word = list_of_words_without_used_words[random_number]
    # because random_number picks a word from a popped version of
    # list_of_words, we can't directly translate the index of the word in
    # list_of_words_without_used_words to the index of the word in
    # list_of_words, therefore, we have to use the list.index()
    # function to find the index of the word in the full list.
    used_words.append(list_of_words.index(word))
    return word, used_words


if __name__ == "__main__":
    import unittest

    testing_list_of_words: List[str] = [
        "hangman", "kanban", "evidence", "problem", "decomposed", "components",
        "developed", "trialled", "assembled", "tested", "create", "final",
        "working", "outcome"
    ]

    class SimpleTest(unittest.TestCase):
        """Test that the word is in the list of words."""

        def test_word_in_list(self):
            """Test that the word is in the list of words."""
            word: Optional[str]
            word, _ = select_random_word([])
            self.assertIn(word, testing_list_of_words)

        def test_index_of_word(self):
            """Test that the index of the word is correct."""
            word: Optional[str]
            index_of_word: List[int]
            word, index_of_word = select_random_word([])
            self.assertEqual(word, testing_list_of_words[index_of_word[-1]])

        def test_index_is_correct(self):
            """Check that the indexes given are returned properly."""
            index_of_word: List[int]
            false_indexes: List[int]
            false_indexes = sample(range(0, len(testing_list_of_words)), 5)
            _, index_of_word = select_random_word(false_indexes)
            for i in false_indexes:
                self.assertIn(i, index_of_word)

        def test_check_lists_are_equal(self):
            """Check that the test list and actual lists are the same."""
            used_words: List[int] = []
            words: List[str] = []
            while True:
                word: str
                word, used_words = select_random_word(used_words)
                if word is None:
                    break
                words.append(word)
            self.assertEqual(sorted(testing_list_of_words), sorted(words))

    unittest.main()
