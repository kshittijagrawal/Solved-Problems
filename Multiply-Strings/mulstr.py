class Solution:
    def multiply(self, num1, num2):
        c1, ind, numo = len(num1)-1, 0, 0
        while c1>=0:
            numo += (ord(num1[ind])-48) * (10**c1)
            c1 -= 1
            ind += 1
        c2, ind, numt = len(num2)-1, 0, 0
        while c2>=0:
            numt += (ord(num2[ind])-48) * (10**c2)
            c2 -= 1
            ind += 1
        return str(numo*numt)