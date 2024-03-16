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
import csv                                                                        # we need to import library to read csv files
def save_to_csv(text, filename):
    words = text.split()                                                          # divides text into words and writes them to variable words
    with open(filename, 'w', newline ='', encoding ='utf-8') as csvfile:          # # open file in write mode and (with open... as..) ensur file in closed after block
        writer = csv.writer(csvfile)                                              # let us write to csv file
        writer.writerow(['Word'])                                                 # makes row header "Word"
        for word in words:                                                        # loop iterates through each word in Word column
            writer.writerow([word])                                               # writes each word as a separate row in the CSV file
text = '''Python was released in 1991 for the first time. Python 2 was
released in 2000 and introduced new features, such as list
comprehensions and a cycle-detecting garbage collection system
(in addition to reference counting). Python 3 was released in 2008
and was a major revision of the language that is not
completely backward-compatible.”
Source: Wikipedia'''
filename = "C:\\Users\\dell\\Desktop\\Testy_Excela\\python.csv"
save_to_csv(text,"C:\\Users\\dell\\Desktop\\Testy_Excela\\python.csv")
def just_digits():
    list_of_strings = []
    with open(filename, 'r') as csvfile:                                         # open file in read mode and (with open... as..) ensur file in closed after block
        reader = csv.reader(csvfile)                                             # reates a CSV reader object, allowing to read  rows from the CSV file
        for row in reader:                                                       # loop that iterates through each row in the CSV file
            for i in row:                                                        # another loop that iterates through each element in the current row
                if i.isdigit():
                    list_of_strings.append(i)
    return list_of_strings

done = just_digits()
print(done)