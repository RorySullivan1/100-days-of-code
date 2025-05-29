import os
import random
from typing import Optional, Union

from Tools.scripts.summarize_stats import print_comparative_specialization_stats

import art

class Card:
    available_denom = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    available_suits = ["Clubs", "Spades", "Hearts", "Diamonds"]

    def __init__(self, denom: str, suit: str):
        assert denom in self.available_denom, ValueError(f"Card Denomination Invalid {denom}")
        assert suit in self.available_suits, ValueError(f"Suit Invalid {suit}")
        self.denom = denom
        self.suit = suit

    def __str__(self):
        return f'{self.denom} of {self.suit}'

class Deck:

    def __init__(self, number_of_decks: int = 1):
        self.cards = []
        for denom in Card.available_denom:
            self.cards += ([Card(denom=denom, suit=suit) for suit in Card.available_suits])
        self.cards = self.cards * number_of_decks

        for _ in range(3): # Shuffle 3x
            self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

class CardHand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        return ", ".join(f"{c}" for c in self.cards) or "Empty Hand"

    def add_card(self, card: Card):
        self.cards.append(card)

    def clear(self):
        self.cards.clear()

    def value(self):
        total, aces = 0, 0
        for card in self.cards:
            if card.denom in ["J", "Q", "K"]:
                total += 10
            elif card.denom == "A":
                total += 11
                aces += 1
            else:
                total += int(card.denom)
        while total > 21 and aces:
            total -= 10
            aces -= 1
        return total

    def is_blackjack(self):
        return self.value() == 21 and len(self.cards) == 2

    def is_bust(self):
        return self.value() > 21


class Player:
    def __init__(self, id: str, chips: Union[float, int] = 100):
        self.id = id
        self.chips = chips
        self.wager = 0
        self.hand = CardHand()

    def recieve_card(self, card: Union[Card, list[Card]]):
        if isinstance(card, Card):
            self.hand.add_card(card)
        elif isinstance(card, list):
            for c in card:
                assert isinstance(c, Card), ValueError("Card Type Expected")
                self.hand.add_card(c)

    def reset_hand(self):
        self.wager = 0
        self.hand.clear()

    def win_hand(self, multiplier: float = 2):
        self.chips += self.wager * multiplier
        print(f"Player wins {self.wager}.\nChip Count: {self.chips}")
        self.reset_hand()


    def stalemate(self):
        self.chips += self.wager
        print(f"Player Push.\nChip Count: {self.chips}")
        self.reset_hand()

    def lose_hand(self):
        print(f"Player loss.\nChip Count: {self.chips}")
        self.reset_hand()

    def show_position(self, verbose: bool = False):
        if verbose:
            print(f"{self.id}: {self.hand} (Value: {self.hand.value()})"
                  f"\nCurrent Wager: {self.wager}"
                  f"\nChips Remaining: {self.chips}\n")
        else:
            print(f"{self.id}: {self.hand} (Value: {self.hand.value()})")

class Dealer(Player):
    def show_initial(self):
        return f"\nDealer Shows: {self.hand.cards[0]}\n"

    def must_hit(self):
        return self.hand.value() < 17

class BlackJack:
    def __init__(self, deck_count: Optional[int] = 3):
        self.deck_count = deck_count
        self.deck = Deck(deck_count)
        self.dealer = Dealer("Dealer")
        self.players = self._add_players()

    @staticmethod
    def _add_players():
        players = []
        collecting_players = True
        while collecting_players:
            name = input("Add Player! Enter Name: ")
            buyin = input("Purchase how many chips?").lower()
            chips = float(1000 if not buyin else float(buyin))
            if chips == "n":
                players.append(Player(id=name))
            else:
                players.append(Player(id=name, chips=chips))
            if input("Add more Players? (Y/N)").lower() == "n":
                collecting_players = False
        return players

    def reset_game(self):
        for player in self.players:
            player.reset_hand()
        self.dealer.reset_hand()
        self.deck = Deck(self.deck_count)

    def deal_cards(self):
        for _ in range(2): # Deal 2 cards
            for player in self.players:
                player.recieve_card(self.deck.deal())
            self.dealer.recieve_card(self.deck.deal())

    def collect_bets(self):
        for player in self.players:
            print(f"Player {player.id} | Chips Remaining: {player.chips}")
            bet = float(input(f"Place your bet!").strip())
            assert bet <= player.chips, ValueError("Bet exceeds chips available")
            player.chips -= bet
            player.wager = bet

    def collect_choices(self):
        for player in self.players:
            if not player.hand:
                pass
            else:
                player.show_position(verbose=True)
                while not player.hand.is_bust():
                    player_choice = input("Hit (H) or Stand (S)?").strip().lower()
                    if player_choice == "h":
                        player.recieve_card(self.deck.deal())
                        player.show_position()
                    elif player_choice == "s":
                        break
                    else:
                        raise ValueError(f"Invalid Choice {player_choice}")

    def dealer_move(self):
        if not self.dealer.hand.is_bust():
            print("\nDealer's Turn:")
            self.dealer.show_position(verbose=False)
            while self.dealer.must_hit():
                self.dealer.recieve_card(self.deck.deal())
                self.dealer.show_position(verbose=False)

    def pay_blackjacks(self):
        for player in self.players:
            if player.hand.is_blackjack():
                print(f"Blackjack for {player.id}")
                player.win_hand(2.5)

    def assess_hand(self, player: Player):
        p_val = player.hand.value()
        d_val = self.dealer.hand.value()

        if not player.hand:
            return
        if player.hand.is_bust():
            print("Player Busts")
            player.lose_hand()
        elif self.dealer.hand.is_bust():
            print("Dealer Busts")
            player.win_hand(2)
        elif p_val > d_val:
            print("Player wins!")
            player.win_hand(2)
        elif d_val > p_val:
            print("Dealer wins!")
            player.lose_hand()
        elif d_val == p_val:
            print("Push!")

    def evaluate(self):
        for player in self.players:
            self.assess_hand(player)


    def play_round(self):
        self.reset_game()
        self.collect_bets()
        self.deal_cards()
        print(self.dealer.show_initial())
        self.pay_blackjacks()
        self.collect_choices()
        self.dealer_move()
        self.evaluate()

    @staticmethod
    def play():
        game_on = True
        print(art.logo)
        game = BlackJack()

        while game_on:
            game.play_round()
            game_on = True if input("Play Again? (Y/N)").lower() == "y" else False


if __name__ == "__main__":
    BlackJack.play()


