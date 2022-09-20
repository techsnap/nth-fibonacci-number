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


n = int(input("Enter n(>= 0): "))

print()
print("Using fib_recursive")
print(f"F({n}) = Number of calls = {fib_recursive(n)}")

print()
print("Using fib_memoized")
print(f"F({n}) = {fib_memoized(n, d)}")
print(f"Number of calls = {calls}")