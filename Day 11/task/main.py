
import random

class Deck:
    def __init__(self):
        self.card_number = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
        self.card_suits = ["C", "S", "H", "D"]
        self.cards = []
        for card in self.card_number:
            self.cards += [str(card) + suit for suit in self.card_suits]

class Blackjack:
    def __init__(self, number_of_decks: int):
        self.cards = Deck().cards * number_of_decks
        self.dealer = Dealer()
        self.players = []

    def shuffle(self, shuffles: int):
        for x in range(0, shuffles): # Shuffle 3x
            random.shuffle(self.cards)

    def deal(self, number_of_cards: int):
        for x in range(0, number_of_cards): # Deal 2 cards
            for player in self.players:

                card = self.cards[0] # Deal first available cards
                player.hand += card
                player.hand_value = value_card(hand_value=player.hand_value, card=card)

                print("Player: " + player.name)
                print(player.hand)
                print(player.hand_value)

            card = random.choice(self.cards)
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





