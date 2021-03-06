"""Contains various ascii art used in the program."""
hangman = [
    """








              """,
    """








==============""",
    """
|
|
|
|
|
|
|
|
+=============""",
    """
|
|
|
|
|
|
|\\
| \\
+=============""",
    """
|
| /
|/
|
|
|
|\\
| \\
+=============""",
    """
+—————————————
| /
|/
|
|
|
|\\
| \\
+=============""",
    """
+—————————————
| /          |
|/
|
|
|
|\\
| \\
+=============""",
    """
+—————————————
| /          |
|/          (_)
|
|
|
|\\
| \\
+=============""",
    """
+—————————————
| /          |
|/          (_)
|            |
|            |
|
|\\
| \\
+=============""",
    """
+—————————————
| /          |
|/          (_)
|            |
|           /|\\
|            |
|\\
| \\
+=============""",
    """
+—————————————
| /          |
|/          (_)
|            |
|           /|\\
|            |
|\\          / \\
| \\
+=============""",
]

if __name__ == "__main__":
    from time import sleep
    for i in hangman:
        print(i)
        sleep(0.5)
