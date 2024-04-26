from random import random
from math import sin,cos

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.x=x_center
        self.y=y_center
        self.r=radius
        
    def randPoint(self) -> List[float]:
        a = random()*6.28318530718
        r = sqrt(random())*self.r
        return [self.x+r*cos(a),self.y+r*sin(a)]

# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()