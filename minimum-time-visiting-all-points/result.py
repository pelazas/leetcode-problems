class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        initial_x, initial_y = points.pop(0)
        result = 0
        while len(points) > 0:
            target_x, target_y = points.pop(0)

            x_move = abs(target_x -initial_x)
            y_move = abs(target_y - initial_y)
            result += max(x_move, y_move)

            initial_x,initial_y = target_x, target_y

        return result
        