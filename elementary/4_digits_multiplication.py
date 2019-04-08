
def checkio(number: int) -> int:
    multi = 1
    string = str(number)
    for num in string:
        if int(num) != 0:
            multi *= int(num)
    return multi


if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
