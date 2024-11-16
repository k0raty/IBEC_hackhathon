def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

def find_pair(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == 10:
                return (lst[i], lst[j])
    return None