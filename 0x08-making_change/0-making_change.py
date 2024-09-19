#!/usr/bin/python3
""" This module contains the makeChange function
"""


def makeChange(coins, total):
    """ Returns the fewest number of coins needed to
    meet total
    """
    if total <= 0:
        return 0
    coins = sorted(coins, reverse=True)
    count = 0

    for coin in coins:
        if total == 0:
            break
        if coin <= total:
            count += total // coin
            total = total % coin

    if total > 0:
        return -1
    return count
