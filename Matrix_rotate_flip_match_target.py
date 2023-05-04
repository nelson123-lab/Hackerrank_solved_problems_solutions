class Solution:
    def rotate(self, matrix):
        return [list(reversed(col)) for col in zip(*matrix)]

    def flip(self, matrix):
        return [list(reversed(rows) for rows in matrix)]

    def findRotation(self, mat, target):
        for i in range(4):
            if mat == target:
                return True
            mat = self.rotate(mat)
        for i in range(4):
            if mat == target:
                return True
            mat = self.flip(mat)
        return False