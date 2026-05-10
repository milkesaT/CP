class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for arr in image:
            left = 0
            right = len(arr) - 1
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]

                left += 1
                right -= 1

        for i in range(len(image)):
            for j in range(len(image[i])):
                if image[i][j] == 0:
                    image[i][j] = 1
                else:
                    image[i][j] = 0
        return image