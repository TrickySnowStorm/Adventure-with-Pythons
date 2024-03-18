"""
Write a function called check_pangram that takes a string
and checks if it is a pangram. A pangram is a sentence that
contains all the letters of the alphabet. If it is a pangram,
the function should return True, otherwise, return False. The
following sentence is a pangram so it should return True:
'the quick brown fox jumps over a lazy dog'
"""
import string                                   # contains useful ascii_lowercase, which includes all lowercase letters of the English alphabet

def check_pangram(tekst):
    alphabet = set(string.ascii_lowercase)      # creates a set containing all lowercase letters of the English alphabet
    return set(tekst.lower()) >= alphabet       # checks if the set of unique lowercase letters in the text 
                                                # is greater than or equal to the alphabet set

tekst = str(input('Your tekst: '))
print(check_pangram(tekst))