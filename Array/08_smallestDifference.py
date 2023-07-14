def _smallestDifference(smaller, bigger):
    smaller.sort()
    bigger.sort()
    smallestDiff = abs(smaller[0] - bigger[0])
    oneSmall = smaller[0]
    twoSmall = bigger[0]
    smallIndex = 1
    biggerIndex = 1
    while smallIndex < len(smaller) and biggerIndex < len(bigger):
        currendDiff = abs(smaller[smallIndex] - bigger[biggerIndex])
        if currendDiff < smallestDiff:
            smallestDiff = currendDiff
            oneSmall = smaller[smallIndex]
            twoSmall = bigger[biggerIndex]
        if smaller[smallIndex] == bigger[biggerIndex]:
            return [oneSmall, twoSmall]
        if smaller[smallIndex] < bigger[biggerIndex]:
            smallIndex += 1
        else:
            biggerIndex += 1
    return [oneSmall, twoSmall]


def smallestDifference(arrayOne, arrayTwo):
    if len(arrayOne) < len(arrayTwo):
        return _smallestDifference(arrayOne, arrayTwo)
    return _smallestDifference(arrayTwo, arrayOne)


if __name__ == "__main__":
    arrayOne = [-1, 5, 10, 20, 28, 3]
    arrayTwo = [26, 134, 135, 15, 17]
    print(smallestDifference(arrayOne, arrayTwo))
