class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        length = len(image) - 1
        for i in range(length + 1):
            for j in range((length + 2) // 2):
                image[i][j], image[i][length - j] =  int(not image[i][length - j]), int(not image[i][j])
        
        return image