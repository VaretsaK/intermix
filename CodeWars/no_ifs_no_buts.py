

def no_ifs_no_buts(a, b):
    while a > b:
        return f"{max(a, b)} is greater than {min(a, b)}"
    while a < b:
        return f"{min(a, b)} is smaller than {max(a, b)}"
    while a == b:
        return f"{a} is equal to {b}"


if __name__ == "__main__":
    print(no_ifs_no_buts(-4, -7))
