#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    choices = ["rock", "paper", "scissors"]
    possible_plays = []

    def rps_helper(result, plays_remaining):
        if plays_remaining == 0:
            possible_plays.append(result)
        else:
            for i in range(0, len(choices)):
                rps_helper(result + [choices[i]], plays_remaining - 1)
        return possible_plays

    rps_helper([], n)
    return possible_plays


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
