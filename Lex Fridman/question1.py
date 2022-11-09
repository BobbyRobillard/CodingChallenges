def tuple_slice(startIndex, endIndex, tup):
    return ",".join(map(str, tup[startIndex:endIndex]))

if __name__ == "__main__":
    print(tuple_slice(1, 4, (76, 34, 13, 64, 12)))