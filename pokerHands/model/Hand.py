from pokerHands.model.Rank import Rank

__author__ = 'Cyrus'


class Hand(object):
    def __init__(self, card1, card2, card3, card4, card5):

        cards = [card1, card2, card3, card4, card5]
        sorted_cards = sorted(cards, key=lambda card: card.rank.value)
        self.cards = sorted_cards
        value_counts = self.__create_value_count()
        self.__count_value_dictionary = self.__create_count_value_dictionary(value_counts)

    def high_card(self):
        return self.cards[4]

    def get_pairs(self):
        if 2 in self.__count_value_dictionary:
            return sorted(self.__count_value_dictionary[2], key=lambda card_rank: card_rank.value)
        else:
            return []

    def get_four_of_a_kind(self):
        if 4 in self.__count_value_dictionary:
            return self.__count_value_dictionary[4][0]
        else:
            return Rank.NULL

    def get_three_of_a_kind(self):
        if 3 in self.__count_value_dictionary:
            return self.__count_value_dictionary[3][0]
        else:
            return Rank.NULL

    def is_a_straight(self):
        previous_value = self.cards[0].rank.value - 1
        for card in self.cards:
            if card.rank.value == previous_value + 1:
                previous_value = card.rank.value
            else:
                return False
        return True

    def is_a_flush(self):
        previous_suit = self.cards[0].suit
        for card in self.cards:
            if card.suit != previous_suit:
                return False
        return True

    def get_kicker(self):
        possible_kickers = sorted(self.__count_value_dictionary[1], key=lambda card_rank: card_rank.value)
        return possible_kickers[len(possible_kickers) - 1]

    def __create_value_count(self):
        value_count = dict()
        for card in self.cards:

            if card.rank in value_count:
                count = value_count[card.rank]
                count += 1
                value_count[card.rank] = count
            else:
                value_count[card.rank] = 1
        return value_count

    @staticmethod
    def __create_count_value_dictionary(value_counts):
        key_value_pairs = value_counts.items()
        count_value_dictionary = dict()
        for pair in key_value_pairs:
            if pair[1] in count_value_dictionary:
                value_list = count_value_dictionary[pair[1]]
                value_list.append(pair[0])
                count_value_dictionary[pair[1]] = value_list
            else:
                count_value_dictionary[pair[1]] = [pair[0]]
        return count_value_dictionary

