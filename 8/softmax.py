import math

input = [1, 4, 5, 2]


def softmax(vector):
    num = []
    output = []

    for i in vector:
        num.append(math.exp(i))

    den = sum(num)

    for j in num:
        output.append(j / den)

    return output


print(softmax(input))