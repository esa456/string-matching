"""
This script provides unit tests for the functions main.py that work to solve
the coding test.
"""
############################################################################################
import os
import sys
import io
import unittest
from main import validate_args, validate_file, line_cleaning

############################################################################################
class TestCLIValidation(unittest.TestCase):
    """ Covers possile test cases of user input seen by 'validate_args' """

    def test_no_arguments(self):
        """ Tests for no command line arguments """

        # Call the validate_arguments function with an empty list of arguments
        args = []
        is_valid = validate_args(args)

        # Assert that the function returns False
        self.assertFalse(is_valid)

    def test_too_many_arguments(self):
        """ Tests for more than 2 command line arguments """

        # Call the validate_arguments function with a list of too many arguments
        args = ["main.py", "source.txt", "search_term"]
        is_valid = validate_args(args)

        # Assert that the function returns False
        self.assertFalse(is_valid)

    def test_argument(self):
        """ Tests for 2 command line arguments """

        # Call the validate_arguments function with a list of too many arguments
        args = ["main.py", "source.txt"]
        is_valid = validate_args(args)

        # Assert that the function returns False
        self.assertTrue(is_valid)


############################################################################################
class TestFileValidation(unittest.TestCase):
    """ Covers possible test cases of files and paths through 'validate_file' """

    def test_valid_file(self):
        """ Test for a valid file path """

        # Create a temporary file for testing
        filename = "test_file.txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write("test data")

        # Call the validate_file function with the valid file path
        is_valid = validate_file(filename)

        # Assert that the file is valid
        self.assertTrue(is_valid)

        # Delete the temporary file
        os.remove(filename)

    def test_nonexistent_file(self):
        """ Test for an invalid file path, where file doesn't exist """

        # Call the validate_file function with a nonexistent file path
        is_valid = validate_file("nonexistent_file.txt")

        # Assert that the file is invalid
        self.assertFalse(is_valid)

    def test_nonexistent_file2(self):
        """ Test for an invalid file path, where path points only to a directory """

        # Call the validate_file function with a nonexistent file path
        is_valid = validate_file(os.getcwd())

        # Assert that the file is invalid
        self.assertFalse(is_valid)

    def test_non_txt_file(self):
        """ Test if the file is in the correct format """

        # Create a temporary file with a non-txt extension for testing
        filename = "test_file.dat"
        with open(filename, "w", encoding="utf-8") as file:
            file.write("test data")

        # Call the validate_file function with the non-txt file path
        is_valid = validate_file(filename)

        # Assert that the file is invalid
        self.assertFalse(is_valid)

        # Delete the temporary file
        os.remove(filename)

    def test_invalid_encoding(self):
        """ Tests the validity of the encoding """

        # Create a temporary file with invalid encoding for testing
        filename = "test_file.txt"
        with open(filename, "w", encoding="utf-16") as file:
            file.write("test data")

        # Call the validate_file function with the invalid encoding file path
        is_valid = validate_file(filename)

        # Assert that the file is invalid
        self.assertFalse(is_valid)

        # Delete the temporary file
        os.remove(filename)

    def test_empty_file(self):
        """ Tests to see if file is empty """

        # Create a temporary file with a non-txt extension for testing
        filename = "test_file.txt"
        with open(filename, "w", encoding="utf-8"):
            pass

        # Call the validate_file function with the non-txt file path
        is_valid = validate_file(filename)

        # Assert that the file is invalid
        self.assertFalse(is_valid)

        # Delete the temporary file
        os.remove(filename)


############################################################################################
class TestFileContents(unittest.TestCase):
    """ Covers possible test cases seen by 'line_cleaning' """

    def test_line_cleaning_accents(self):
        """ Test accented characters """

        line = "@ésa_ikram"
        self.assertEqual(line_cleaning(line), "ésa ikram")

    def test_line_cleaning_whitespace(self):
        """ Test consecutive whitespaces """

        line = "    hello   sir how are  you"
        self.assertEqual(line_cleaning(line), "hello sir how are you")

    def test_line_cleaning_newline(self):
        """ Test newlines """

        line = "trees\n"
        self.assertEqual(line_cleaning(line), "trees")

    def test_line_cleaning_tabs(self):
        """ Test tabs """

        line = "   cucumbers\t"
        self.assertEqual(line_cleaning(line), "cucumbers")

    def test_line_cleaning_numbers(self):
        """ Test numbers """

        line = "143forreal I 0love eating lettuce"
        self.assertEqual(line_cleaning(line), "forreal I love eating lettuce")

    def test_line_cleaning_symbols(self):
        """ Test symbols """

        line = "trumpets need @#cleaning_every!&^six hours."
        self.assertEqual(line_cleaning(line), "trumpets need cleaning every six hours")

    def test_line_cleaning_empty(self):
        """ If first line is empty """

        line = ""
        self.assertEqual(line_cleaning(line), "")


############################################################################################
def testing_method(input_list):
    """
    This function holds logic that returns the output to console and is available
    to ensure code reuse
    """

    # Create a StringIO object to capture stdout
    output = io.StringIO()

    # Redirect stdout to the StringIO object
    sys.stdout = output

    # Call the function that will result in output whilst avoiding user input
    validate_args(input_list)

    # Get the value of the captured stdout
    stdout_value = output.getvalue()

    # Reset stdout to its original value
    sys.stdout = sys.__stdout__

    return stdout_value


class TestInputs(unittest.TestCase):
    """ Provides a number of test cases to ensure end to end tests pass """

    def test_input1(self):
        """ This will test the first provided example """

        with open("input1.txt", "w", encoding="utf-8") as file:
            file.write("cat sees me\n")
            file.write("mary likes trees\n")
            file.write("up the hill\n")
            file.write("ee\n")

        # Argument list
        input_list = ["main.py", "input1.txt"]

        # Console output
        output_value = testing_method(input_list)

        # Define the expected output as a list of strings
        expected_output = "['cat sees me']\n['mary likes trees']\n"

        # Assert that the captured stdout matches the expected output
        self.assertEqual(output_value, expected_output)

        # Deletes file
        os.remove("input1.txt")

    def test_input2(self):
        """ This will test the second provided example """

        with open("input2.txt", "w", encoding="utf-8") as file:
            file.write("Alice was beginning...\n")
            file.write("to_get9_!very\n")
            file.write("1111tired1111ofile1111sitting1111\n")
            file.write("by her_sister.\n")
            file.write("on9the bank,\n")
            file.write('and""ofile""having\n')
            file.write("nothing to do!!!\n")
            file.write("er\n")

        # Argument list
        input_list = ["main.py", "input2.txt"]

        # Console output
        output_value = testing_method(input_list)

        # Define the expected output as a list of strings
        expected_output = "['to get very']\n['by her sister']\n"

        # Assert that the captured stdout matches the expected output
        self.assertEqual(output_value, expected_output)

        # Deletes file
        os.remove("input2.txt")

    def test_input3(self):
        """ Test a file with an empty string and case sensitive search term """

        with open("input3.txt", "w", encoding="utf-8") as file:
            file.write("once upon _a time\n")
            file.write("   in a galaxy a fair few years away\n")
            file.write("\n")
            file.write("a python %*engineer was testing code in\n")
            file.write("his lair\n")
            file.write("for Tony Blair\n")
            file.write("AIR")

        # Argument list
        input_list = ["main.py", "input3.txt"]

        # Console output
        output_value = testing_method(input_list)

        # Define the expected output as a list of strings
        expected_output = (
            "['in a galaxy a fair few years away']\n"
            + "['his lair']\n['for Tony Blair']\n"
        )

        # Assert that the captured stdout matches the expected output
        self.assertEqual(output_value, expected_output)

        # Deletes file
        os.remove("input3.txt")

    def test_input4(self):
        """ Test the extended Latin alphabet (diacritics) """

        with open("input4.txt", "w", encoding="utf-8") as file:
            file.write("ésa ikram\n")
            file.write("likes Crème Brûlée\n")
            file.write("but cant stand raîsins\n")
            file.write("é  ")

        # Argument list
        input_list = ["main.py", "input4.txt"]

        # Console output
        output_value = testing_method(input_list)

        # Define the expected output as a list of strings
        expected_output = "['ésa ikram']\n['likes Crème Brûlée']\n"

        # Assert that the captured stdout matches the expected output
        self.assertEqual(output_value, expected_output)

        # Deletes file
        os.remove("input4.txt")


############################################################################################
if __name__ == "__main__":
    unittest.main()
