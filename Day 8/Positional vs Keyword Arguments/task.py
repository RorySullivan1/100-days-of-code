# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")

def greet_multiple_people(people: list[str]):
    people_str = " ".join(people)
    print("Hey {}! How is it going guys!".format(people_str))

greet_multiple_people(["Me", "Myself", "I"])

def greet_person_at_location(person: str, location: str):
    print("Hey {}! I didn't know you'd be {}".format(person, location))


greet_person_at_location(person="Ryan", location="London")

