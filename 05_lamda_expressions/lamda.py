
def get_numbers(limit, predicate):
    for n in range(0, limit):
        if predicate(n):
            yield n


result = list(get_numbers(50, lambda n: n % 11 == 0))
print(result)
