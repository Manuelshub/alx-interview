#!/usr/bin/python3
""" This module contains the makeChange function
"""


def makeChange(coins, total):
    """ Returns the fewest number of coins needed to
    meet total
    """
    # Check to make sure input is valid
    if total <= 0:
        return 0
    # Sorting coins in descending order
    coins = sorted(coins, reverse=True)
    # Initializing a count
    count = 0

    # Looping through coins
    for coin in coins:
        if total == 0:
            break
        if coin <= total:
            # Getting the number of coins for each coin
            count += total // coin
            # Updating total with the remaining amount
            total = total % coin
    # If after the loop total is not 0, return -1
    # Meaning that it is impossible to meet the total
    if total > 0:
        return -1
    return count
