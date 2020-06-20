import time


def selection_sort(data, drawdata, timetick):
    N = len(data)
    for pos in range(0, N-1):
        for k in range(pos+1, N):
            if data[k] < data[pos]:
                data[k], data[pos] = data[pos], data[k]
                drawdata(data, ['cyan' if x == k or x ==
                                pos else 'deep sky blue' for x in range(N)])
                time.sleep(timetick)
