


def sum_of_evens(number):
    total = 0

    for number1 in range(0,number + 1):
        if number1 % 2 == 0:
            total = total + number1

    return total



print(sum_of_evens(4))
