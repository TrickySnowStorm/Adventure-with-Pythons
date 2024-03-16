"""
In this challenge, copy the text below and save it as a CSV file.
Save it in the same folder as your Python file. Save it as
python.csv.
Write a function called just_digits that reads the text from the
CSV file and returns only digit elements from the file. Your
function should return 1991, 2, 200, 3, 2008 as a list of
strings.
“Python was released in 1991 for the first time. Python 2 was
released in 2000 and introduced new features, such as list
comprehensions and a cycle-detecting garbage collection system
(in addition to reference counting). Python 3 was released in 2008
and was a major revision of the language that is not
completely backward-compatible.”
Source: Wikipedia
"""
import csv                                          # we need to import library to read csv files
def just_digits():
    list_of_strings = []
    with open('python.csv', 'r') as file.csv:       # open file in read mode and (with open... as..) ensur file in closed after block
        reader = csv.reader(file.csv)               # reates a CSV reader object, allowing to read  rows from the CSV file.
        for row in reader:
            for i in row:
                if i.isdigit():
                    list_of_strings.append(i)
    return list_of_strings

just_digits()
