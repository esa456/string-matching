*************************************** PREREQUISITES **************************************
This solution will be developed in python and so you will need to have the following things installed:

python 3.9
os
unittest
re
sys
io

Note: Please ensure the files are in the same directory when running

*************************************** ASSUMPTIONS **************************************


ASSUMPTION 1:

'No numbers or symbols will be found in the middle of the words'

numbers or symbols embedded within the words would disrupt the word boundaries and make it difficult to distinguish the vocabulary for this task.


ASSUMPTION 2:

'The solution only supports characters found in the Latin alphabet and the Latin alphabet with diacritics'

This allows for any of the following characters to be processed and tested éèêëîïôöùûüçàáâäåæñøœß as well as the normal characters found in the english alphabet.


ASSUMPTION 3:

'The solution does not support large files'

For purposes of runtime the solution does not support large files, the portion of the code that checks if the file is empty therefore loads the whole file into memory and checks it's size.


ASSUMPTION 4:

'The input file must be a '.txt' format

I have decided to define a scope otherwise a vast number of file type would need to be accounted for


ASSUMPTION 5:

'The input must have 'utf-8' encoding'

So to allow for the logic to process the diacritic characters of the Latin alphabet


ASSUMPTION 6:

'The search term is not case sensitive'

Letter Casing is extremely common and so should be accounted for