def fibonacci():
    current = 0
    nxt = 1

    while True:
        print("Generating "+ str(current))
        current, nxt = nxt, current+nxt
        yield current

for n in fibonacci():
    if n> 200:
        break
    print(n, end = ', ')