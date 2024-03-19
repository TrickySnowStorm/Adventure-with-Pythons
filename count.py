"""
Write a function called count that takes one argument a string,
and returns a dictionary of how many times each element
appears in the string. For example, ‘hello’ should return:
{‘h’:1,’e’: 1,’l’:2, ‘o’:1}
"""

def count(tekst):
    how_many ={}
    for char in tekst:
        how_many[char] = how_many.get(char, 0) + 1  # In square brackets ([]), there is an index that refers to a specific element in a dictionary
                                                    # It might be confusing because square brackets are often associated with lists,
                                                    # but in the context of dictionaries in Python, when used with a key,
                                                    # they serve to reference a specific element in the dictionary.
                                                    # The numbers_occurrences.get(character, 0) checks whether a given char is already in the numbers_occurrences dictionary.
                                                    # If it is, it returns the number of its occurrences. If not, it returns the default value 0
                                                    # Then, we add 1 to the result of this operation to increase the count of occurrences of the particular character by one.
                                                    # This value is assigned to the corresponding key (character) in the dictionary.
    return how_many

tekst = 'łubudubu, niech nam żyje prezes naszego klubu'
print(count(tekst))