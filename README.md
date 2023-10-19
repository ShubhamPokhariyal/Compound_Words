# Compound_Words
Solution for Impledge Fresher Problem

Execution Steps:
1.   Open the compound_word.py file in an editor
2.   Update the file path at line 13
3.   Execute the script

Approach:
Read the input file and store the words in a list and sort it according to the length, so the words which form the compound word can be addded to the WordSet (python set) beforehand.
The approach I used is a recursive approach which splits the current word into a suffix and prefix while recursively solving the prefix.
If the word being processed is found to be a compound word it is then compared to the longest compound word and the second longest compound word.

