import copy
import random

def findSequence(t, n):
    tOrigin = t.copy()
    tOrigin = tOrigin[:n]
    tSort = tOrigin.copy()
    tSort = list(set(tSort))
    tSort.sort()
    nBis = len(tSort)
    tRange = []
    rangeStart = tSort[0]

    for i in range(1, nBis):
        if tSort[i] != tSort[i - 1] + 1:
            tRange.append(range(rangeStart, tSort[i - 1] + 1))
            rangeStart = tSort[i]
    tRange.append(range(rangeStart, tSort[i] + 1))

    seqBeg = 0
    seqEnd = 0

    for r in tRange:
        tSelected = [None] * n
        for i in range(len(tOrigin)):
            if tOrigin[i] in r:
                tSelected[i] = tOrigin[i]
        anchorBeg = 0
        anchorEnd = 0
        wasOnNone = True

        for i in range(len(tSelected)):
            if tSelected[i] == None:
                wasOnNone = True
            else:
                if wasOnNone == True:
                    anchorBeg = i
                else:
                    anchorEnd = i + 1
                    if anchorEnd - anchorBeg > seqEnd - seqBeg:
                        seqBeg = anchorBeg
                        seqEnd = anchorEnd
                wasOnNone = False

    return tOrigin[seqBeg:seqEnd], seqEnd - seqBeg

def main():
    for n in range(10):
        t = []
        for i in range(random.randint(4, 20)):
            t.append(random.randint(0, 20))
        print("\norigin :", t)
        print("sequence :", findSequence(t, len(t)))

main()
