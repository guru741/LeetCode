class Solution(object):
    def flipAndInvertImage(self, image):
        n = len(image)

        for i in range(n):
            st,end = 0,n - 1

            while st <= end:
                temp = image[i][st] ^ 1
                image[i][st] = image[i][end] ^ 1
                image[i][end] = temp

                st += 1 
                end -= 1
        return image
        