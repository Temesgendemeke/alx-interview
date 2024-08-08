#!/usr/bin/python3
""" Prime Game"""


def isWinner(x, nums):
    """ Prime Game"""
    def sieve(n):
        """ Prime Game"""
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        return [p for p in range(2, n + 1) if is_prime[p]]

    max_n = max(nums)
    primes = sieve(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        available = set(range(1, n + 1))
        turn = 0  # 0 for Maria, 1 for Ben

        while True:
            move_made = False
            for prime in primes:
                if prime in available:
                    move_made = True
                    multiples = set(range(prime, n + 1, prime))
                    available -= multiples
                    break

            if not move_made:
                if turn == 0:
                    ben_wins += 1
                else:
                    maria_wins += 1
                break

            turn = 1 - turn

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
