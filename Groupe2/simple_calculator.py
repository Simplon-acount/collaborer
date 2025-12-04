def add(a,b):
    return a+b
def subtract(a, b):
    return a-b
def multiply(a, b):
    """Multiply using repeated addition"""
    result = 0
    negative = False
    if b < 0:
        b = -b
        negative = True

    for _ in range(int(b)):
        result = add(result, a)


    if negative:
        result = -result




