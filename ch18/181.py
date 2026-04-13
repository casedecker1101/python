class search:
    """
    Read a specified number of characters from a file.
    Args:
        filepath (str): The path to the file to read from.
        num_char (str or int): The number of characters to read from the file.
    Returns:
        str: A string containing the first num_char characters from the file.
    Raises:
        FileNotFoundError: If the file at filepath does not exist.
        OSError: If the file cannot be read due to system-level errors.
        ValueError: If num_char cannot be converted to an integer.
    """
# 18.5 creating a function to read characters from a file
    def __init__(self, filepath, num_char):
        self.filepath = filepath
        self.num_char = num_char

    def searchN(self):
        num_chars = int(self.num_char)
        with open(self.filepath, mode = "r", encoding="utf-8") as f:
            return f.read(num_chars)

cinMenu = ""
while cinMenu != 'quit':
    filepath = input("Enter file path: ")
    characters = input("Enter number of characters to read: ")

    searching = search(filepath, characters)
    try:
        print(searching.searchN())
    except ValueError:
        print("Please enter a valid whole number for characters.")
    except FileNotFoundError:
        print("File not found. Check the path and try again.")
    except OSError as err:
        print(f"Could not read file: {err}")
    cinMenu = input("Type 'quit' to exit or press Enter to continue: ")

