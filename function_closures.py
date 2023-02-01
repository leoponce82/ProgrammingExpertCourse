def counter(start):
    count = start
    def increment(value):
        nonlocal count
        count += value
        return count
    return increment

x = counter(2)
print(x(3))