class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        letters = ['a', 'c', 'e', 'g']
        numbers = ['1', '3', '5', '7']
        letters2 = ['b', 'd', 'f', 'h']
        numbers2 = ['2', '4', '6', '8']

        if coordinates[0] in letters and coordinates[1] in numbers:
            return False

        if coordinates[0] in letters2 and coordinates[1] in numbers2:
            return False

        return True