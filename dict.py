print('................................. DICTIONARY ....................................')
dict = {000:'Mr./Mrs.'}
dict[100] = 'subrata'
dict[200] = 'moumita'
dict[300] = 'sun'
dict[400] = 'moon'
print(dict)

my_dict = {'name':'Subrata Das', 'age':28, 'address':'Kolkata', 'position':'Developer'}
print(my_dict)
print(my_dict['name'])
print(my_dict.get('age'))
print(my_dict.get('location')) # return none value
# print(my_dict['location']) # return keyerror
my_dict['age'] = 29 # update the value
print(my_dict)
my_dict['pin'] = 700001 # add new item
print(my_dict)


print('\n..................................... POP() ..........................................')
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares.pop(4))
print(squares)

print('\n................................... POPITEM() ........................................')
print(squares.popitem())
print(squares)


print('\n.................................... CLEAR() .........................................')
squares.clear()
print(squares)

print('\n.................................... del .........................................')
del squares
# print(squares) # Throws error

print('\n.................................... COPY() .........................................')
original_marks = {'Physics':67, 'Maths':87}
copied_marks = original_marks.copy() #dict.copy()
print('Original Marks:', original_marks)
print('Copied Marks:', copied_marks)

original = {1:'one', 2:'two'}
new = original.copy()
new.clear()
print('new: ', new)
print('original: ', original)


print('\n.................................... = OPERATOR .........................................')
original = {1:'one', 2:'two'}
new = original
new.clear()
print('new: ', new)
print('original: ', original)
