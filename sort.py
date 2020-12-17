def insertions(tosort):
    for i in range(1,len(tosort)):
        newel = tosort[i]
        h = i
        while newel < tosort[h - 1] and h > 0:
            tosort[h] = tosort[h - 1]
            h -= 1
        tosort[h] = newel
    return tosort


def bubblesort(tosort):
    n = len(tosort)
    for i in range(n-1, 0, -1):
        for el in range(i):
            if tosort[el] > tosort[el+1]:
                tosort[el], tosort[el+1] = tosort[el+1], tosort[el]
    return(tosort)
