def main():
    num = int(input('Insert number:'))
    output = sumOfMultiples(num)
    print(output)


def sumOfMultiples(a, b):
    sum = 0
    for i in range(1000):
        if (i % a == 0) or (i % b == 0):
            sum += i
    return sum
