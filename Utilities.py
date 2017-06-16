from Constants import *


def change_register_group(input):
    input = input.lower()

    indexesUP = set([0, 1])
    indexesDwn = set([2, 3])

    if input == BAD_GROUP:
        output = REPAIR_BAD_GROUP
    else:
        output = ''.join(c.upper() if i in indexesUP else c.lower() if i in indexesDwn else c for i, c in enumerate(input))

    return output
