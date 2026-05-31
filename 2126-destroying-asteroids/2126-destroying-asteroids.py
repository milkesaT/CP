class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        n=mass
        for i in asteroids:
            if n<i:
                return False
            n+=i
        return True
