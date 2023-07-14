def maxSubsetSumNoAdjacent(array: list):
    track = [-1] * len(array)
    sumArray = [i for i  in array]
    maxSum = max(array[0], array[1])

    if maxSum != array[1]:
        sumArray[1] = maxSum
        track[1] = 0
    for index in range(2, len(array)):
        if array[index] + sumArray[index-2] > sumArray[index-1]:
            sumArray[index] = array[index] + sumArray[index-2]
            track[index] = index - 2
        else:
            sumArray[index] = sumArray[index-1]
            track[index] = index - 1
    
    index = len(array) -1
    while index != -1:
        if sumArray[index] != sumArray[track[index]]:
            print(array[index])
        index = track[index]
    print(array)
    print(sumArray)

if __name__ == '__main__':
    array = [75, 105, 120, 75, 90, 135]
    array = [4, 3, 5, 200, 5, 3]
    maxSubsetSumNoAdjacent(array)