import re
def convert(size):
    str(size).strip()
    temp = re.compile("([0-9]+)([a-zA-Z)]+)")
    convertedTuple = temp.match(size).groups()
    if str(convertedTuple[1]).lower().strip() == "kb":
        result = float(convertedTuple[0]) * 2**10
    elif str(convertedTuple[1]).lower().strip() == "mb":
        result = float(convertedTuple[0]) * 2**20
    elif str(convertedTuple[1]).lower().strip() == "gb":
        result = float(convertedTuple[0]) * 2**30
    else:
        raise AttributeError
    return result

