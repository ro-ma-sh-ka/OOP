def mygenerator(start, end):
    "My first Generator"
    while start < end:
        yield start
        start += 1


for item in mygenerator(1, 10):
    print(item)