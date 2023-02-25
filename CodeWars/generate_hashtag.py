

def generate_hashtag(a):

    new = "#" + "".join([x.capitalize() for x in a.strip().split(" ")])
    if 0 < len(new) < 141:
        return new


if __name__ == "__main__":
    print(generate_hashtag(" Hello there thanks for trying my Kata"))
