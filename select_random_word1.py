"""Select a random word from a list and pass on a list of used words."""
from typing import Tuple


def select_random_word(used_words: list = None) -> Tuple[str, list]:
    """Select a random word from a list and pass on a list of used words.

    Args:
        used_words (list, optional): [description]. Defaults to None.

    Returns:
        Tuple[str, list]: The random word that is selected and a list
        of the index of every random word that has been selected.
    """
