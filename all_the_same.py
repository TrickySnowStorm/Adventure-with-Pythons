'''
Create a function called all_the_same that takes one
argument, a string, a list, or a tuple and checks if all the
elements are the same. If the elements are the same, the function
should return True. If not, it should return False. For example,
[‘Mary’, ‘Mary’, ‘Mary’] should return True.

'''

def all_the_same(data):
                                                                # Sprawdzenie czy wszystkie elementy na liście lub krotce są takie same
    if isinstance(data, (list, tuple)):                         # isinstance porównuje czy data to lista lub tupla,
        return all(element == data[0] for element in data)      # jeśli tak, True - idzie dalej, jeśli nie False
    elif isinstance(data, str):
        return all(char == data[0] for char in data)
    else:
        return False                                            # Obsługa przypadku, gdy data nie jest ani listą, ani tuplą, ani stringiem

                                                                # Testowanie funkcji, można wprowadzić własne parametry
print(all_the_same(['Mary', 'Mary', 'Mary']))  
print(all_the_same(('apple', 'apple', 'apple')))  
print(all_the_same('aaa'))  
print(all_the_same([1, 2, 3]))  