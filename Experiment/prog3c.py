def pyramid_pattern(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + " ".join(str(j) for j in range(1, i + 1)))

n = int(input("Enter number of times : "))
pyramid_pattern(n)
