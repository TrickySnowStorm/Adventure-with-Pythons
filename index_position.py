'''
Write a function called index_position. This function takes a
string as a parameter and returns the positions or indexes of all
lower letters in the string. For example, ‘LovE’ should return
[1,2].
'''

def index_position(word):

    index_list = []

    for index in range(len(word)):                  # Iterating over the indices within the range of the word's length.
        letter = word[index]
        if letter.islower():
            index_list.append(index)

    return index_list

word = str(input('Please, enter your word mixed with lowercase and uppercase letter: '))
indexes = index_position(word)
print(indexes)