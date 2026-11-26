class Solution:
    def canAliceWin(self, n: int) -> bool:
        remove = 10
        alice_turn = True

        while n >= remove:
            n -= remove
            remove -= 1
            alice_turn = not alice_turn

        # Whoever's turn it is now cannot make a move and loses,
        # so the *other* player wins.
        return not alice_turn