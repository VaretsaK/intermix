

def find_missing(s):
    step = (s[-1] - s[0]) / ((s.index(s[-1]) + 2) - 1)
    for i in range(len(s)):
        if s[i + 1] != s[i] + step:
            return int(s[i] + step)


if __name__ == "__main__":
    print(find_missing([1, 3, 7, 9]))
