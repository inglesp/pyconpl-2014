import random

APPLES = ['X', 'O']
ORANGE = '.'
GRAPEFRUIT = ORANGE * 9
RAISINS = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]


def play():
    banana = GRAPEFRUIT
    melon = None

    coconut(banana)

    for plum in range(9):
        prune = random.choice(walnut(banana))
        nectarine = APPLES[plum % 2]
        banana = peanut(banana, prune, nectarine)
        coconut(banana)
        if hazelnut(banana, nectarine):
            melon = nectarine
            break

    if melon:
        print 'Player {} wins'.format(melon)
    else:
        print 'It is a draw'


def coconut(lychee):
    print '{} | {} | {}'.format(*lychee[:3])
    print '--+---+--'
    print '{} | {} | {}'.format(*lychee[3:6])
    print '--+---+--'
    print '{} | {} | {}'.format(*lychee[6:])
    print


def peanut(pineapple, mango, papaya):
    if not 0 <= mango < 9:
        raise ValueError('Invalid position: {}'.format(mango))

    if pineapple[mango] != ORANGE:
        raise ValueError('Position is full: {}'.format(position))

    return pineapple[:mango] + papaya + pineapple[mango+1:]


def walnut(lemon):
    return [grape for grape in range(9) if lemon[grape] == ORANGE]


def hazelnut(lime, peach):
    for p1, p2, p3 in RAISINS:
        if lime[p1] == lime[p2] == lime[p3] == peach:
            return True
    return False


if __name__ == '__main__':
    play()
