
def greet():
    print("Some Greeting")
    print("You know how it be")
    print("You will see this when it runs")

def greet_name(name: str):
    print("Hey {}! Welcome!".format(name))

greet()
greet_name("Ryan")