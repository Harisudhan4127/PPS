n = int(input("Enter the n value : "))

def fibonacci_series(n):
    series = [0,1]
    for i in range(2,n):
        series.append(series[-1] + series[-2])
    return series[:n]
print("Fibonacci Series : ", fibonacci_series(n))
