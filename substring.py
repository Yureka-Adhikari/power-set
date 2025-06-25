def subsets_bitwise(s):
    n = len(s)
    subsets = []
    for i in range(1 << n):
        subset = ""
        for j in range(n):
            if i & (1 << j):
                subset += s[j]
        subsets.append(subset)
    return subsets

if __name__ == "__main__":
    inp = input("Enter a string: ")
    result = subsets_bitwise(inp)
    print("All subsets:")
    for sub in result:
        print(sub)