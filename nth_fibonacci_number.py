def fib_recursive(n):
    if n < 2:
    	return n
    
    return fib_recursive(n-1) + fib_recursive(n-2)


calls = 0
d = {0:0, 1:1}
def fib_memoized(n, d):
    global calls
    calls += 1

    if n in d:
        return d[n]
    else:
        d[n] = fib_memoized(n-1, d) + fib_memoized(n-2, d)
        return d[n]


def fib_iterative(n):
    if n < 2:
    	return n
    
    a, b = 1, 2
    for i in range(3, n):
        c = a + b
        a = b
        b = c

    return c

n = int(input("Enter n(>= 0): "))

print()
print("Using fib_recursive")
print(f"F({n}) = Number of calls = {fib_recursive(n)}")

print()
print("Using fib_memoized")
print(f"F({n}) = {fib_memoized(n, d)}")
print(f"Number of calls = {calls}")

print()
print("Using fib_iterative")
print(f"F({n}) = {fib_iterative(n)}")