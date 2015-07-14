#!/usr/bin/env python

import sys

game = [None] * 9
turn = 1
WIN_COMBOS = [
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [0,4,8],
    [2,4,6]
]

def repr_square(game, i):
    if game[i] == 1:
        return 'X'
    elif game[i] == 0:
        return 'O'
    else:
        return ' '


def print_game(game):
    for i in range(0,3):
        row = i * 3
        line = ""
        line += repr_square(game, row + 0)
        line += "|"
        line += repr_square(game, row + 1)
        line += "|"
        line += repr_square(game, row + 2)
        print line


# scores for all squares
# sort those
# the best one
#
def count_losses(game, our_i, depth=0):
    depth += 1
    if depth == 6:
        return 0

    new_game = list(game)
    new_game[our_i] = 0

    if is_winner(game, 0):
        return 0
    else:
        losses = 0
        # do their move
        for i in range(0,9):
            if game[i] is None:
                new_game = list(game)
                new_game[i] = 1
                if is_winner(new_game, 1):
                     losses += 1
                else:
                    for i in range(0, 9):
                        if new_game[i] is None:
                            losses += count_losses(new_game, i, depth)
        return losses

#      for all the remaining squares:
#         pick their move
#         if is a win for them
#            return 1
#         else:
#            return count_losses(new_new_game, i)


def find_highest_idx(ary):
    maximum_idx = None
    maximum = None
    for i in range(0, len(ary)):
        if ary[i] is not None:
            if maximum_idx == None or ary[i] > maximum:
                maximum_idx = i
                maximum = ary[i]
    return maximum_idx


def our_move(game):
    ret = None
    squares_to_losses = [None] * 9
    for our_i in range(0,9):
        if game[our_i] is None:
            squares_to_losses[our_i] = count_losses(game, our_i)
            print squares_to_losses

    return find_highest_idx(squares_to_losses)


def get_move():
    print "-------"
    print "1|2|3"
    print "4|5|6"
    print "7|8|9"
    move = input("Enter your move: ")
    return move


def end_game():
    print "THE END"
    sys.exit(0)


def is_winner(game, player):
    for combo in WIN_COMBOS:
        score = 0
        for index in combo:
            if game[index] == player:
                score += 1
        if score == 3:
            return True
    return False


def is_full(game):
    total = 0
    for index in game:
        if index is not None:
            total += 1
    return total == 9


while True:
    if turn == 0:
        our_move_idx = our_move(game)
        game[our_move_idx] = 0
        print "Here's my move!"
        print_game(game)
    elif turn == 1:
        move = get_move()
        # if legal...
        game[move - 1] = 1
    else:
        raise "CANNOT HAPPEN"

    if is_winner(game, 1):
        print "you won"
        end_game()
    elif is_winner(game, 0):
        print "i won, despite trying to lose"
        end_game()
    elif is_full(game):
        print "nobody won"
        end_game()
    else:
        # game is not over
        pass

    turn ^= 1




# represent the game



# output the game state

# take input

# define winning

# enumerate possibilities
# pick the move whereby the other user wins more of the time


