## Creating a python dictionary
def one():
    # empty dictionary
    my_dict = {}

    # dictionary with integer keys
    my_dict = {1: 'apple', 2: 'ball'}

    # dictionary with mixed keys
    my_dict = {'name': 'John', 1: [2, 4, 3]}

    # using dict()
    my_dict = dict({1:'apple', 2:'ball'})

    # from sequence having each item as a pair
    my_dict = dict([(1,'apple'), (2,'ball')])

#Accessing Elements from Dictionary
def two():
    # get vs [] for retrieving elements
    my_dict = {'name': 'Jack', 'age': 26}

    # Output: Jack
    print(my_dict['name'])

    # Output: 26
    print(my_dict.get('age'))

    # Trying to access keys which doesn't exist throws error
    # Output None
    print(my_dict.get('address'))

    # KeyError
    print(my_dict['address'])

# Changing and Adding Dictionary elements
def three():
    # Changing and adding Dictionary Elements
    my_dict = {'name': 'Jack', 'age': 26}

    # update value
    my_dict['age'] = 27

    #Output: {'age': 27, 'name': 'Jack'}
    print(my_dict)

    # add item
    my_dict['address'] = 'Downtown'

    # Output: {'address': 'Downtown', 'age': 27, 'name': 'Jack'}
    print(my_dict)

#Removing elements from Dictionary
def four():
    # Removing elements from a dictionary

    # create a dictionary
    squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

    # remove a particular item, returns its value
    # Output: 16
    print(squares.pop(4))

    # Output: {1: 1, 2: 4, 3: 9, 5: 25}
    print(squares)

    # remove an arbitrary item, return (key,value)
    # Output: (5, 25)
    print(squares.popitem())

    # Output: {1: 1, 2: 4, 3: 9}
    print(squares)

    # remove all items
    squares.clear()

    # Output: {}
    print(squares)

    # delete the dictionary itself
    del squares

    # Throws Error
    print(squares)

#Python Dictionary Comprehension
def five():
    '''
    Dictionary comprehension is an elegant and concise way to create a new dictionary
    from an iterable in Python.

    Dictionary comprehension consists of an expression pair (key: value)
    followed by a for statement inside curly braces {}.
    '''
    # Dictionary Comprehension
    squares = {x: x*x for x in range(6)}

    print(squares)

one()
two()
three()
four()
five()
