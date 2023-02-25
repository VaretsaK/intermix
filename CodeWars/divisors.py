

def divisors(i):
    new = []
    b = i - 1
    while b != 1:
        if i % b == 0:
            new.append(b)
        b -= 1
    if len(new) == 0:
        return f"{i} is prime"
    new.reverse()
    return new


if __name__ == "__main__":
    print(divisors(13))
