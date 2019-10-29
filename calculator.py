def add(*args):
    count = 0

    for each_number in args:
        count += each_number

    return count

def multiply(*args):
    count = 1

    for each_number in args:
        count *= each_number

    return count


