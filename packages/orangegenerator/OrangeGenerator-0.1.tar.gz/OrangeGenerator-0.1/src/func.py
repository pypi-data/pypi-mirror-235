import random



def randodd(a: int, b: int):
    return random.randint(a // 2, b // 2) * 2 + 1

