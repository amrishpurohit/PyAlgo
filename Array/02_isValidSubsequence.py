def isValidSubsequence(array, sequence) -> bool:
    if not sequence:
        return False
    sequenceIndex = 0
    for element in array:
        if element == sequence[sequenceIndex]:
            sequenceIndex += 1
            if sequenceIndex == len(sequence):
                return True
    return False


if __name__ == "__main__":
    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [1, 6, -1, 10]
    print(isValidSubsequence(array, sequence))
