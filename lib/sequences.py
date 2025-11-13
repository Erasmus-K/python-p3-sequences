#!/usr/bin/env python3

def print_fibonacci(n):
    if n <= 0:
        print([])
        return
    
    fib_seq = [0]
    
    if n > 1:
        fib_seq.append(1)
    
    while len(fib_seq) < n:
        next_value = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(next_value)
    
    print(fib_seq)

# Example usage:
print_fibonacci(9)
# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21]
