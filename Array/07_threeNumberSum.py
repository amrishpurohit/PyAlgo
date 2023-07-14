def threeNumberSum(array, targetSum):
    array.sort()
    result= []
    for first in range(len(array) - 3):
        second = first + 1
        third = len(array)-1
        while second < third:
            currentSum = array[first] + array[second] + array[third]
            print(currentSum)
            if currentSum == targetSum:
                result.append([array[first], array[second], array[third]])
                second += 1
                third -= 1
            elif currentSum < targetSum:
                second += 1
            else:
                third -= 1
    return result


if __name__ == '__main__':
    array = [12, 3, 1, 2, -6, 5, -8, 6]
    targetSum = 0
    print(threeNumberSum(array, targetSum))
