'''
Write a function called unique_numbers that takes a list of
numbers as an argument. Your function is going to find all the
unique numbers in the list. It will then sum up the unique
numbers. You will calculate the difference between the sum of
all the numbers in the original list and the sum of unique
numbers in the list. If the difference is an even number, your
function should return the original list. If the difference is an
odd number, your function should return a list with unique
numbers only. For example [1, 2, 4, 5, 6, 7, 8, 8] should
return [1, 2, 4, 5, 6, 7, 8, 8].
'''

def unique_numbers(numbers_list):

    unique_list = list(set(numbers_list))       # creating a list of unique numbers
                                                # set automatically removes duplicate elements
    unique_sum = sum(unique_list)
    numbers_sum = sum(numbers_list)
    if (numbers_sum - unique_sum)  % 2 == 0:    # () allows to maintain the order of operations
        return numbers_list
    else:
        return unique_list


numbers_list = [1, 2, 4, 5, 6, 7, 8, 8]
result = unique_numbers(numbers_list)
print(result)
