
import random

class Deck:
    def __init__(self):
        self.card_number = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
        self.card_suits = ["C", "S", "H", "D"]
        self.cards = []
        for card in self.card_number:
            self.cards += [str(card) + suit for suit in self.card_suits]

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

def shuffle(cards: list, shuffles: int):
    for x in range(0, shuffles): # Shuffle 3x
        random.shuffle(cards)
    return cards


class Blackjack:
    def __init__(self, number_of_decks: int):
        self.cards = Deck().cards * number_of_decks
        self.dealer = Dealer()
        self.players = []

    def bet(self):
        for player in self.players:
            wager = float(input(f"{player.name}. How Much would you like to wager?"))
            if player.money < wager:
                raise ValueError("Insufficient Funds")
            else:
                player.money -= wager
                player.wager = wager


    def deal(self):
        for x in range(0, 2): # Deal 2 cards per person
            for player in self.players:
                card = self.cards.pop(0) # Deal first available cards
                player.hand += card
                player.hand_value = value_card(hand_value=player.hand_value, card=card)

                print("Player: " + player.name)
                print(player.hand)
                print(player.hand_value)

            card = random.choice(self.cards)
            self.dealer.hand += card
            self.dealer.hand_value = value_card(hand_value=self.dealer.hand_value, card=card)
        print("Dealer")
        print(self.dealer.hand[0] + "x")

    def hit(self, player: Player):
        card = self.cards.pop(0)  # Deal first available cards
        player.hand += card
        player.hand_value = value_card(hand_value=player.hand_value, card=card)

    def double(self, player: Player): ...

    def split(self, player: Player): ...

    def refresh(self):
        for player in self.players:
            if player.money > 0:
                # Refresh Player Hand
                player.restart()
            else:
                # Drop Player
                self.players.pop(self.players.index(player))

    def assess_hands(self):
        for player in self.players:
            if player.hand_value > self.dealer.hand_value:
                player.money += player.wager * 2
                print(f"Player {player.name} wins {player.wager * 2}")
            elif player.hand_value == self.dealer.hand_value:
                player.money += player.wager
                print(f"Player {player.name} pushes")
            else:
                print(f"Player {player.name} losses")

    def play(self):
        adding_players = True
        self.dealer = Dealer()

        # Setup Game
        while adding_players:
            player = input("Enter Player Name!")
            buyin = int(input("How much are you playing with?"))
            self.players.append(Player(name=player, buyin=buyin))
            adding_players = input("Add another player? (Y/N)").lower() != "n"

        # Play Game
        playing = True
        while playing:
            game_on = True
            while game_on:

                #Shuffle
                self.cards = shuffle(self.cards, 3)

                # Place Bets
                self.bet()

                # Deal Cards
                self.deal()

                # Payout Blackjack
                if self.dealer.hand_value == 21:
                    "Dealer Blackjack"
                    self.assess_hands()
                    game_on = False

                # Player Choices
                for player in self.players:
                    if player.hand_value == 21:
                        player.money += player.wager * 2.5
                        print(f"Player {player.name} Blackjack!")
                        continue
                    else:
                        choosing = True
                        while choosing:
                            print(f"Player {player.name}:\n Cards {player.hand} ({player.hand_value})")
                            choice = input(f"Hit (H), Stand (S), Split (X), Double (D)?").upper()
                            if choice == "H":
                                self.hit(player)
                            elif choice == "S":
                                choosing = False
                            elif choice == "X":
                                raise NotImplemented()
                            elif choice == "D":
                                raise NotImplemented()

                            if player.hand_value > 21:
                                print(f"Player {player.name} Busts")
                                player.wager = 0
                                choosing = False

                self.assess_hands()

            # refresh
            self.refresh()
            playing = True if input("Play Again? (Y/N)") == "Y" else False


def value_card(hand_value: int, card: str | int):
    print(card)
    if card in ["J", "Q", "K"]:
        return 10
    elif card == "A":
        if hand_value < 11:
            return 1
        else:
            return 11
    else:
        return int(card[:-1])

if __name__ == "__main__":
    game = Blackjack(3)
    game.play()


