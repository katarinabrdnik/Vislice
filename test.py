for n in range(1, 201):
    for d in range (2, n):
        if n % d == 0:
            break
    #ta else se izvrši, če zanka ni bila predhodno ustavljena
    else:
        print(n)