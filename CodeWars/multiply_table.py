

def multiply(a):
    result = []
    for i in range(1, a + 1):
        result.append([])
        for j in range(1, a + 1):
            result[i - 1].append(i * j)
    return result


if __name__ == "__main__":
    print(multiply(4))
