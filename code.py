obj1= {'a':{'b':{'c':'d'}}}
obj2= {'x':{'y':{'z':'a'}}}
def get_value(object):
    for key, value in object.items():
        if type(value) is dict:
            yield from get_value(value)
        else:
            yield (key, value)

for key, value in get_value(obj1):
    print(value)
