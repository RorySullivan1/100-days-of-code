
import random

class Blackjack:
    def __init__(self, number_of_decks: int):
        self.cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
        self.suits = ["C","S","H","D"]
        self.cards_in_play = self.cards * number_of_decks
        self.dealer = None
        self.players = []

    def shuffle(self):
        for x in range(0, 3): # Shuffle 3x
            random.shuffle(self.cards_in_play)

    def deal(self):
        for x in range(0,2): # Deal 2 cards
            for player in self.players:
                card = random.choice(self.cards_in_play)
                player.hand += card
                player.hand_value = value_card(hand_value=player.hand_value, card=card)
                print("Player: " + player.name)
                print(player.hand)
                print(player.hand_value)

            card = random.choice(self.cards_in_play)
            self.dealer.hand += card
            self.dealer.hand_value = value_card(hand_value=self.dealer.hand_value, card=card)
            print("Dealer")
            print(self.dealer.hand)
            print(self.dealer.hand_value)

    def hit(self): ...

    def stand(self): ...

    def refresh(self):
        for player in self.players:
            if player.money > 0:
                # Refresh Player Hand
                player.restart()
            else:
                # Drop Player
                self.players.pop(self.players.index(player))

    def play(self):
        all_players = False
        self.dealer = Dealer()

        # Setup Game
        while not all_players:
            player = input("Enter Player Name!")
            buyin = int(input("How much are you playing with?"))
            self.players.append(Player(name=player, buyin=buyin))
            all_players = input("Add another player? (Y/N)").lower() == "y"

        # Play Game
        game_on = True
        while game_on:
            # Deal Cards
            self.deal()

            # Payout Blackjack

            # Player Choices

            # refresh


def value_card(hand_value: int, card: str | int):
    if card in ["J", "Q", "K"]:
        return 10
    elif card == "A":
        if hand_value < 11:
            return 1
        else:
            return 11
    else:
        assert isinstance(card, int), ValueError("Card value {} - not returnable".format(card))
        return card

class Participant:
    def __init__(self):
        self.hand = ""
        self.hand_value = 0
        self.wager = 0

    def restart(self):
        return Participant.__init__(self)

class Player(Participant):
    def __init__(self, name: str, buyin: float):
        super().__init__()
        self.name = name
        self.money = buyin
        self.wager = 0

class Dealer(Participant):
    def __init__(self):
        super().__init__()





