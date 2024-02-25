'''
Write a function called middle_figure that takes two
parameters a, and b. The two parameters are strings. The
function joins the two strings and finds the middle element.
If the combined string has a middle element, the function should
return the element, otherwise, return ‘no middle figure’. Use
‘make love’ as an argument for a and ‘not wars’ as an
argument for b. Your function should return ‘e’ as the middle
element. Whitespaces should be removed
'''


def middle_figure(a, b):
    combined_string = (a + b).replace(" ", "")      # Joining two strings and removing whitespaces

    if len(combined_string) % 2 == 0:               # Checking if the length of the combined string is even
        return 'no middle figure'                   # If there is no middle element, return 'no middle figure'
    else:
        middle_index = len(combined_string) // 2    # Return the middle element
        return combined_string[middle_index]

result = middle_figure("huba bub", "not wars")
print(result)
