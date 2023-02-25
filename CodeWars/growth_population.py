
def popul(a, b, c, d):
    counter = 0
    while a < d:
        a = a + (a * b / 100) + c
        counter += 1
    return counter


if __name__ == "__main__":
    print(popul(1500000, 0.5, 1000, 2000000))
