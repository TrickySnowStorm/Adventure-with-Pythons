'''
Write a function called repeated_name that finds the most
repeated name in the following list.
name = ["John", "Peter", "John", "Peter", "Jones", "Peter"]
'''


def repeted_name(names):
    counted_names = {}
    for name in names:
        if name in counted_names:
            counted_names[name] +=1
        else:
            counted_names[name] =1
    most_popular_name = max(counted_names, key=counted_names.get)
    return most_popular_name

names = ["John", "Peter", "John", "Peter", "Jones", "Peter"]
print(repeted_name(names))