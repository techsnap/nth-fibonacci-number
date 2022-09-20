def fib_recursive(n):
    if n < 2:
    	return n
    
    return fib_recursive(n-1) + fib_recursive(n-2)


n = int(input("Enter n: "))

print()
print("Using fib_recursive")
print(f"F({n}) = Number of calls = {fib_recursive(n)}")