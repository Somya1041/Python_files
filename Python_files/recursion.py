def countdown(n):
    print(n)
    if n == 0:
        return
    else:
        countdown(n-1)
        
countdown(10)
        
        