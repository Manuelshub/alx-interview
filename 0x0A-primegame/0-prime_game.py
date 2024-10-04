#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """ Determines the winner of a prime game after x rounds.

    Args:
        x (int): Number of rounds.
        nums (list): List of integers representing the maximum number in each round.

    Returns:
        str or None: The name of the player with the most wins ("Maria" or "Ben"),
                     or None if they have the same number of wins.
    """
    if x < 1 or not nums:
        return None
    
    # Precompute primes up to the maximum value in nums
    max_n = max(nums)
    prime = [True] * (max_n + 1)
    prime[0] = prime[1] = False
    
    for i in range(2, int(max_n**0.5) + 1):
        if prime[i]:
            for j in range(i * i, max_n + 1, i):
                prime[j] = False

    # Calculate results for each round and keep track of wins
    maria_wins, ben_wins = 0, 0

    for n in nums:
        primes_count = sum(prime[:n + 1])  # Count primes up to n
        # If primes_count is odd, Maria wins; if even, Ben wins
        if primes_count % 2 != 0:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
