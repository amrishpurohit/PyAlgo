def twoNumberSum(array: list, targetSum: int) -> list:
    seen = set()
    for num in array:
        if targetSum - num not in seen:
            seen.add(num)
        else:
            return (num, targetSum - num)
    return (None, None)
        


if __name__ == "__main__":
    array = [3, 5, -4, 8, 11, 1, -1, 6]
    targetSum = 10
    print(twoNumberSum(array, targetSum))
