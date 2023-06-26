def fibonacci(n):
    sequence = []
    if n >= 1:
        sequence.append(0)
    if n >= 2:
        sequence.append(1)

    for i in range(2, n):
        fib_num = sequence[i-1] + sequence[i-2]
        sequence.append(fib_num)

    return sequence

# For example
n = int(input("Enter the number of Fibonacci numbers to generate: "))
fibonacci_sequence = fibonacci(n)
print("Fibonacci Sequence:", fibonacci_sequence)
