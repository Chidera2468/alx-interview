#!/usr/bin/python3
<<<<<<< HEAD
"""0. Prime Game - Maria and Ben are playing a game"""


def isWinner(x, nums):
    """x - rounds
    nums - numbers list
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    ben = 0
    maria = 0

    a = [1 for x in range(sorted(nums)[-1] + 1)]
    a[0], a[1] = 0, 0
    for i in range(2, len(a)):
        rm_multiples(a, i)

    for i in nums:
        if sum(a[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def rm_multiples(ls, x):
    """removes multiple
    of primes
    """
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break
=======
"""
Define isWineer function, a solution to the Prime Game problem
"""


def primes(n):
    """Return list of prime numbers between 1 and n inclusive
      Args:
       n (int): upper boundary of range. lower boundary is always 1
     """
      prime = []
      sieve = [True] * (n + 1)
      for p in range(2, n + 1):
          if (sieve[p]):
          prime.append(p)
          for i in range(p, n + 1, p):
              sieve[i] = False
      return prime



  def isWinner(x, nums):
      """
      Determines winner of Prime Game
      Args:
        x (int): no. of rounds of game
        nums (int): upper limit of range for each round
      Return:
        Name of winner (Maria or Ben) or None if winner cannot be found
        """
        if x is None or nums is None or x == 0 or nums == []:
            return None
        Maria = Ben = 0
        for i in range(x):
            prime = primes(nums[i])
            if len(prime) % 2 == 0:
                Ben += 1
            else:
                Maria += 1
        if Maria > Ben:
             return 'Maria'
         elif Ben > Maria:
              return 'Ben'
          return None

>>>>>>> 31c35b492ad02a95fa2e707fb422cceff86291d3
