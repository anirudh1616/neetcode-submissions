class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Calculate the distance between a given point and the origin.
        # After all the distances have been calculated, sort them in ascending order
        # Pick the first k points in that ascending order to be returned.
        # important caveat, you have to store the distance in a way that it relates to the points.

        # making helper function to calculate distance:
        def dist(point: List[int]):
            origin = (0, 0)
            x2 = origin[0]
            y2 = origin[1]

            x1 = point[0]
            y1 = point[1]

            return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        distances = []
        for i in range(len(points)):
            point = points[i]
            distance = dist(point)
            distances.append((distance, point))
        
        distances.sort()
        result = [item[1] for item in distances[:k]]
        return result
