from types import  SimpleNamespace


class Person:
    def __init__(self, name, age, hobby):
        self.hobby = hobby
        self.age = age
        self.name = name

    def __repr__(self):
        return "{0} is {1} and likes {2}".format(self.name, self.age, self.hobby)


people = [
    Person("Rodel", 25, "Working"),
    Person("June Aileen", 24, "Eating"),
    Person("Yuni Mayari", 2, "Sleeping")
]

# simple query
workers = [p for p in people if p.hobby == "Working"]
workers.sort(key=lambda p: -p.age)
print(workers)

# simple projection with anonymous types
sleepers = [SimpleNamespace(name = p.name, age = p.age, hobby = p.hobby, status = "Verified") for p in people if p.hobby == "Sleeping"]
print(sleepers)
for sleeper in sleepers:
    print(sleeper.name)