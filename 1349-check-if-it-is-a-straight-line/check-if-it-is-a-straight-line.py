class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        try:
            slope = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0]) 
        except ZeroDivisionError:
            slope = 0
        last_point = coordinates[1]
        for i in range(2,len(coordinates)):
            try:
                if (coordinates[i][1] - last_point[1]) / (coordinates[i][0] - last_point[0]) != slope:
                    return False
            except ZeroDivisionError:
                if 0 != slope:
                    return False
        return True
        