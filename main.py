"""
This is a program that takes a single command-line argument that species a
file path which points to a file specifying some source text anda search term.

It then searches the source text for matches of the search term, and outputs all
the matches in a specified format
"""
############################################################################################
import re
import sys
import os

############################################################################################
def validate_args(arguments):
    """ Validate the number of arguments from user input """

    # Check number of arguments
    if len(arguments) != 2:
        print("Invalid number of arguments, Please enter the file path")
        return False

    # Valid number of arguments
    file_path = arguments[1]
    validate_file(file_path)
    return True


############################################################################################
def validate_file(file_path):
    """ Validates that the given file exists and is a valid text file """

    # Check if the file exists and is a file (not a directory)
    if not os.path.isfile(file_path):
        print(f"Error: {file_path} is not a valid file.")
        return False

    # Check if the file is in the correct format (e.g., a txt file)
    if not file_path.endswith(".txt"):
        print(f"Error: {file_path} is not a txt file.")
        return False

    # Check if file is empty
    if os.path.getsize(file_path) == 0:
        print(f'The file "{file_path}" is empty.')
        return False

    # Process the file
    try:
        # The encoding type accounts for accented characters
        with open(file_path, "r", encoding="utf-8") as file:
            lines = list(file.readlines())

        main(lines)
        return True

    except UnicodeDecodeError:
        print(
            f'Error: File "{file_path}" could not be read as text, please check the encoding'
        )
        return False


############################################################################################
def line_cleaning(line):
    """ Removes all consecutive whitespaces, newlines and non alphabetic characters """

    # This regex expression accounts for the Latin alphabet with diacritics
    clean_line = re.sub(
        r"[^a-zA-Zéèêëîïôöùûüçàáâäåæñøœß]+", " ", line, flags=re.UNICODE
    ).strip()

    # Remove any consecutive spaces
    cleaned_line = re.sub(r"\s+", " ", clean_line)

    return cleaned_line


############################################################################################
def main(lines):
    """ Overall objective is computed here """

    # Gives us a clean search term
    search_term = line_cleaning(lines[-1])

    # Loop through each line apart from the last
    for line in lines[:-1]:

        # Gives us a clean line to search
        cleaned_line = line_cleaning(line)

        # Match the line with any capitalisation
        pattern = re.compile(search_term, re.IGNORECASE)

        # If there's a match
        match = pattern.search(cleaned_line)
        if match:

            # Format output
            new_list = [cleaned_line]
            print(new_list)


############################################################################################
def run():
    """ End to end run """

    arguments = sys.argv
    validate_args(arguments)

    return True


if __name__ == "__main__":
    run()
