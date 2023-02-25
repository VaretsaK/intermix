

def diamond(a):
    if a < 1 or a % 2 == 0:
        return
    b = a // 2
    c = 0
    cc = 0
    r = []
    for i in range(1, a * 2 + 1):
        if i % 2 == 0:
            continue
        if i < a:
            r.append(" " * (b - c))
            r.append("*" * i)
            r.append("\n")
            c += 1
        elif i == a:
            r.append("*" * a)
            r.append("\n")
        else:
            c -= 1
            cc += 1
            r.append(" " * (b - c))
            r.append("*" * (a - 2 * cc))
            r.append("\n")

    new = ''.join(r)
    return new


if __name__ == "__main__":
    print(diamond(9))
