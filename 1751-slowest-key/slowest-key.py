from typing import List

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        maxi = releaseTimes[0]  # The duration of the first key press
        lar = keysPressed[0]  # The first key itself
        n = len(releaseTimes)  # The total number of key presses
        
        for i in range(1, n):
            diff = releaseTimes[i] - releaseTimes[i - 1]  # The duration of the current key press
            if diff > maxi or (diff == maxi and keysPressed[i] > lar):
                maxi = diff  # Update the maximum duration
                lar = keysPressed[i]  # Update the slowest key

        return lar  # Return the slowest key