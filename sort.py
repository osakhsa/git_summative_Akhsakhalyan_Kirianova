def bubblesort(tosort):
    n = len(tosort)
    for i in range(n-1, 0, -1):
        for el in range(i):
            if tosort[el] > tosort[el+1]:
                tosort[el], tosort[el+1] = tosort[el+1], tosort[el]
    return(tosort)
