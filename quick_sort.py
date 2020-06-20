import time


def partition(data, head, tail, drawdata, timetick):
    border = head
    pivot = data[tail]

    drawdata(data, getcolor(len(data), head, tail, border, border))
    time.sleep(timetick)

    for j in range(head, tail):
        if data[j] < pivot:
            drawdata(data, getcolor(len(data), head, tail, border, j, True))
            time.sleep(timetick)

            data[border], data[j] = data[j], data[border]
            border += 1

        drawdata(data, getcolor(len(data), head, tail, border, j))
        time.sleep(timetick)

    drawdata(data, getcolor(len(data), head, tail, border, tail, True))
    time.sleep(timetick)

    data[border], data[tail] = data[tail], data[border]
    return border


def quick_sort(data, head, tail, drawdata, timetick):
    if head < tail:
        partitionidx = partition(data, head, tail, drawdata, timetick)

        quick_sort(data, head, partitionidx-1, drawdata, timetick)
        quick_sort(data, partitionidx+1, tail, drawdata, timetick)


def getcolor(datalen, head, tail, border, curridx, isswaping=False):
    colorlist = []
    for i in range(datalen):
        # base coloring
        if head <= i <= tail:
            colorlist.append('deep sky blue')
        else:
            colorlist.append('gray')

        if i == border:
            colorlist[i] = 'red'
        elif i == tail:
            colorlist[i] = 'blue'
        elif i == curridx:
            colorlist[i] = 'orange'

        if isswaping:
            if i == border or i == curridx:
                colorlist[i] = 'spring green'
    return colorlist
