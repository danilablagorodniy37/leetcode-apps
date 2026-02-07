class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        res = 0               # Counter for how many jewels we found
        for s in stones:      # Loop through each character (stone) in stones
            if s in jewels:   # Check if this stone type is listed in jewels
                res += 1      # If yes, increase the counter
        return res            # Return the total count
