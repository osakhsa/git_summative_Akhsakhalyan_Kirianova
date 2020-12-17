def insertions(tosort):
    for i in range(1,len(tosort)):
        newel = tosort[i]
        h = i
        while newel < tosort[h - 1] and h > 0:
            tosort[h] = tosort[h - 1]
            h -= 1
        tosort[h] = newel
    return tosort
