memo = {}

def fibonnaci(n):
    if n < 2:
        return n

    if n not in memo:
        memo[n] = fibonnaci(n-1) + fibonnaci(n-2)
    
    return memo[n]

print(fibonnaci(14))