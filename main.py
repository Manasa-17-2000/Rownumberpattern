N = int(input("Enter The Number : "))
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if j == i:
            print(j, end="")
        else:
            print(" ", end="")
    print()


