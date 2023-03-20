def getTrappedWater(heights) -> int:
    p1:int = 0
    p2:int = len(heights)-1
    trappedWater:int = 0
    maxLHeight:int = 0
    maxRHeight:int = 0
    while p1<p2:
        if heights[p1] < heights[p2]:
            if heights[p1] < maxLHeight:
                trappedWater += maxLHeight - heights[p1]
            else:
                maxLHeight = heights[p1]
            p1 += 1
        else:
            if heights[p2] < maxRHeight:
                trappedWater += maxRHeight - heights[p2]
            else:
                maxRHeight = heights[p2]
            p2 -= 1
    return trappedWater
