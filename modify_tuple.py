# Add a certain value into a tuple at a certain position
def insert_item(my_tuple, new_value, index):
    # The first step is to slice the tuple. It isn't as easy as using a list
    new_tuple = my_tuple[:index] + (new_value,) + my_tuple[index:]    
    return new_tuple

sports = ('football', 'basketball', 'cricket', 'hockey', 'tennis', 'volleyball')
new_value = 'baseball'
index1 = 2

numbers = (7, 17, 13, 19, 5)
new_value2 = 11
index2 = 3

result1 = insert_item(sports, new_value, index1)
print(result1)
result2 = insert_item(numbers, new_value2, index2)
print (result2)