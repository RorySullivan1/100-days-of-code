# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

def add_bid(bids: dict):
    name = input("What is your Name?")
    bid = float(input("What is your bid?"))
    bids[name] = bid

def get_highest_bidder(bids: dict):
    highest_bidder = None
    highest_bid = 0
    for name, bid in bids.items():
        if bid > highest_bid:
            highest_bid = bid
            highest_bidder = name
    return highest_bidder, highest_bid

def clear_terminal():
    print("\n" * 20)

def run_auction():
    bids = {}
    active = True

    print("Lets Start The Bidding!")
    while active:
        add_bid(bids)
        if input("Anymore bids? (Y/N)").lower() == "n":
            highest_bidder, highest_bid = get_highest_bidder(bids)
            print(f"{highest_bidder} wins with a bid of {highest_bid}!")
            active = False
        else:
            clear_terminal()
            continue

run_auction()

