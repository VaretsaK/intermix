
def sum_of_parts(lls):
    new_sum = [sum(lls)]

    for i in range(len(lls)):
        new_sum.append(new_sum[i] - lls[i])
    return new_sum


if __name__ == "__main__":
    print(sum_of_parts([0, 1, 3, 6, 10]))
