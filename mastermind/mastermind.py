import itertools
import random

N = 4
PEGS = 'abcdef'


def score(pattern, guess):
    n_black = len([ix for ix in range(N) if pattern[ix] == guess[ix]])

    pattern_mismatches = [pattern[ix] for ix in range(N) if pattern[ix] != guess[ix]]
    guess_mismatches = [guess[ix] for ix in range(N) if pattern[ix] != guess[ix]]

    n_white = 0

    for x in guess_mismatches:
        if x in pattern_mismatches:
            n_white +=1
            pattern_mismatches.remove(x)

    return n_black, n_white


def all_patterns():
    return list(itertools.product(*[PEGS for _ in range(N)]))


def possible_patterns(patterns, guess, n_black, n_white):
    return [p for p in patterns if score(p, guess) == (n_black, n_white)]


def play():
    patterns = all_patterns()

    while True:
        guess = random.choice(patterns)

        print 'I guess', guess
        n_black = int(raw_input('How many black pegs? '))
        n_white = int(raw_input('How many white pegs? '))

        patterns = possible_patterns(patterns, guess, n_black, n_white)

        if len(patterns) == 0:
            print
            print 'You must have made a mistake'
            break
        elif len(patterns) == 1:
            print
            print 'Your pattern is', patterns[0]
            break


if __name__ == '__main__':
    play()
