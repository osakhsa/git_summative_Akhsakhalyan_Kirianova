def bubblesort(tosort):
    n = len(tosort)
    for i in range(n-1, 0, -1):
        for el in range(i):
            if tosort[i] > tosort[i+1]:
                tosort[i], tosort[i+1] = tosort[i+1], tosort[i]
    return(tosort)
