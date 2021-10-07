import random


def generate_random(power: int) -> list:
    """
    Generate list with 2 ** power random elemnts.
    """
    array = [random.random() for i in range(2 ** power)]
    return array

def generate_increasing(power: int) -> list:
    array = [random.random() for i in range(2 ** power)]
    array.sort()
    return array

def generate_decreasing(power: int) -> list:
    array = [random.random() for i in range(2 ** power)]
    array.sort(reverse=True)
    return array

def generate_from_set(power: int) -> list:
    array = [random.choice([1, 2, 3]) for i in range(2**power)]
    return array