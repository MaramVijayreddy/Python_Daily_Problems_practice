class Solution:
    def startStation(self, gas, cost):
        #  code here
        totalgas=sum(gas)
        totalcost=sum(cost)
        if totalgas < totalcost:
            return -1
        currentgas=0
        startindex=0
        for i  in range(len(gas)):
            currentgas+=gas[i]-cost[i]

            if currentgas<0:
                startindex=i+1
                currentgas=0


        return startindex