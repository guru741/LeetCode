class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        sum_bottles = numBottles
        empty = 0
        while numBottles >= numExchange:
            new = numBottles // numExchange
            empty = numBottles % numExchange
            sum_bottles += new
            numBottles = new + empty
        return sum_bottles
        