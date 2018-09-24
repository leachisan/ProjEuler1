def main():
    num = int(input('Insert number:'))
    output = sumOfMultiples(num)
    print(output)


def sumOfMultiples(a, b):
    sum = 0
    for i in range(1000):
        if (i % 3 == 0) or (i % 5 == 0):
            sum += i
    return sum
