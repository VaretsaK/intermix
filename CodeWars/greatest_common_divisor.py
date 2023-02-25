

def mygcd(x, y):
    a = max(x, y)
    b = min(x, y)
    while True:
        r = a - b * (a // b)
        if r == 0:
            return b
        a = b
        b = r


if __name__ == "__main__":
    print(mygcd(444, 444))
