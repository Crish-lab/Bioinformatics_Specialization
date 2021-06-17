'''SOLVE THE CHANGE PROBLEM
The DPChange pseudocode is reproduced below for your convenience.

Input: An integer money and an array Coins = (coin1, ..., coind).
Output: The minimum number of coins with denominations Coins that changes money.
   DPChange(money, Coins)
      MinNumCoins(0) ← 0
      for m ← 1 to money
         MinNumCoins(m) ← ∞
         for i ← 0 to |Coins| - 1
            if m ≥ coini
               if MinNumCoins(m - coini) + 1 < MinNumCoins(m)
                  MinNumCoins(m) ← MinNumCoins(m - coini) + 1
      output MinNumCoins(money)

Sample Input:
40
50,25,20,10,5,1
Sample Output:
2
'''
import sys

def RECchange(money, coins):

    if money == 0:
        return 0

    MinNumCoins = float("inf")

    for i in range(len(coins)):
        if money >= coins[i]:
            NumCoins = RECchange(money - coins[i], coins)
            if NumCoins + 1 < MinNumCoins:
                MinNumCoins = NumCoins + 1

    return MinNumCoins


def DPchange(money, coins):

    MinNumCoins = [0 for i in range(money + 1)]

    for m in range(1, money + 1):
        MinNumCoins[m] = float("inf")
        for i in range(len(coins)):
            if m >= coins[i]:
                NumCoins = MinNumCoins[m - coins[i]] + 1
                if NumCoins < MinNumCoins[m]:
                    MinNumCoins[m] = NumCoins

    return MinNumCoins[money]



if __name__ == "__main__":

    money = int(input())
    denominations = [2, 3]

    print(DPchange(money, denominations))