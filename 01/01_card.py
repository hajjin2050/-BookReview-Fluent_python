from random import choice
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
        # deck[0] 은 첫번째 카드를 , deck[-1]은 마지막 카드를 가져온다 => 이때 기능을 __getitem_에서 수행해줌


# 자신이 갖고 있는 카드의 수를 반환
deck = FrenchDeck()
print(len(deck))


# 무작위로 골라내는 메서드를 사용
print(choice(deck))

# __getitem__() 특별 메서드를 구현함으로써 deck 반복
for card in deck:  # doctest : +ELLIPSIS
    print(card)

# 컬렉션에 __contatins__() 메서드가 없다면 in 연산자는 차례대로 검색 -> iterable Class 라면 가능
print(Card('Q', 'hearts') in deck)  # True

# 정렬 -> 숫자로 순위를 정하고 숫자가 같은 경우 스페이드 >하트>다이아몬드>클로버 순으로 정함

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(deck, key=spades_high):  # doctest: +ELLIPSIS
    print(card)
    # Frenchdeck 이 압묵적으로 object 를 상속받지만 상속 대신 데이터 모델과 구성을 이요용해서 기능을 가져온다.
    # __len__() 과 __getitem__() 특별 메서드를 구현함으로써 self._cards 에 떠넘길 수 있음


# 추후 카드셔플링은 11_shuffle.py 에 __setitem__() 이라는 메서드를 추가하여 해결
