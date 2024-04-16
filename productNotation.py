def productNotation(function, lowerBound, Upperbound):
    y = 0
    for i in range(lowerBound, Upperbound):
        y *= function(i)
    return y
