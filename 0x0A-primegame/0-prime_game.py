#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """
    Determines if a player can win the game
    Args:
        x: number of rounds
        nums: list of numbers
    Returns:
        The name of the player that won the most rounds
    """
    if not nums or x < 1:
        return None
    prime = [True] * (x + 1)
    prime[0] = False
    prime[1] = False
    for i in range(2, x + 1):
        if prime[i]:
            for j in range(i * 2, x + 1, i):
                prime[j] = False
    for i in nums:
        if prime[i]:
            return 'Ben'
    return 'Maria'
