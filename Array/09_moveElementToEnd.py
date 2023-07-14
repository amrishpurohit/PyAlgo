def moveElementToEnd(array, toMove):
    for right in range(len(array)-1, -1, -1):
        if array[right] != toMove:
            break
    left=0
    while left < right:
        if array[left] == toMove:
            array[left] = array[right]
            array[right] = toMove
            right -= 1
        else:
            left += 1
    return array


if __name__ == '__main__':
    array = [2, 1, 2, 2, 2, 3, 4, 2]
    toMove = 2
    print(moveElementToEnd(array, toMove))
