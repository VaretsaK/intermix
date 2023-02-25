

def solve(word):
    alph = "abcdefghijklmnopqrstuvwxyz"
    new_dict = {}
    parts = ""

    for i in range(len(alph)):
        new_dict[alph[i]] = i + 1

    for i in word:
        if i in "aeiou":
            parts += " "
        else:
            parts += i
    parts = parts.split(" ")

    maximum = 0
    current = 0
    for i in range(len(parts)):
        if current > maximum:
            maximum = current
        current = 0
        for j in parts[i]:
            current += new_dict[j]
    return max(maximum, current)


if __name__ == "__main__":
    print(solve("zozz"))
