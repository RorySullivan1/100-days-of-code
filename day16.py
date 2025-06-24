from operator import truediv

menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

class CoffeeMachine:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100
        }
        self.choice = ""
        self.balance = 0

    def make_coffee(self):
        print(f"Making: {self.choice}", "\n", menu[self.choice]["ingredients"])
        self.remove_resources()
        return

    def check_resources(self):
        resources_required = menu[self.choice]["ingredients"]
        for item in resources_required:
            if self.resources[item] < resources_required[item]:
                print(f"Not enough {item}.\nNeed {resources_required[item]}")
                return False
        return True

    def remove_resources(self):
        resources_required = menu[self.choice]["ingredients"]
        for item in resources_required:
            self.resources[item] -= resources_required[item]

    def request_selection(self):
        self.choice = input(f"Please select coffee type: {list(menu.keys())}\n").lower()
        assert self.choice in menu, ValueError(f"Incorrect Choice {self.choice}")

    def request_money(self):
        return float(input(f"Please insert ${menu[self.choice]["cost"] - self.balance} for 1 {self.choice}\n"))

    def run(self):
        running = True
        while running:
            self.request_selection()
            if not self.check_resources():
                running = False
            else:
                self.balance = self.request_money()
                while self.balance < menu[self.choice]["cost"]:
                    self.balance += self.request_money()
                self.make_coffee()
                print(f"Successfully made {self.choice}")
                if self.balance > menu[self.choice]["cost"]:
                    print(f"Refunding ${self.balance - menu[self.choice]["cost"]:}")
                print("-" * 10)
                print("Resources Remaining:")
                print(self.resources)
            self.balance = 0


def main():
    machine = CoffeeMachine()
    machine.run()

main()


