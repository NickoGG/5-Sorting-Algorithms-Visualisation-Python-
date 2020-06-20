import time


def merge_sort(data, drawdata, timetick):
    merge_sort_alg(data, 0, len(data)-1, drawdata, timetick)


def merge_sort_alg(data, left, right, drawdata, timetick):
    if left < right:
        mid = (left + right) // 2
        merge_sort_alg(data, left, mid, drawdata, timetick)
        merge_sort_alg(data, mid+1, right, drawdata, timetick)
        merge(data, left, mid, right, drawdata, timetick)


def merge(data, left, mid, right, drawdata, timetick):
    drawdata(data, getcolor(len(data), left, mid, right))
    time.sleep(timetick)

    leftpart = data[left: mid+1]
    rightpart = data[mid+1: right+1]

    leftidx = rightidx = dataidx = 0

    for dataidx in range(left, right+1):
        if leftidx < len(leftpart) and rightidx < len(rightpart):
            if leftpart[leftidx] <= rightpart[rightidx]:
                data[dataidx] = leftpart[leftidx]
                leftidx += 1
            else:
                data[dataidx] = rightpart[rightidx]
                rightidx += 1

        elif leftidx < len(leftpart):
            data[dataidx] = leftpart[leftidx]
            leftidx += 1

        elif rightidx < len(rightpart):
            data[dataidx] = rightpart[rightidx]
            rightidx += 1

    drawdata(data, ['spring green' if x >= left and x <=
                    right else 'gray' for x in range(len(data))])
    time.sleep(timetick)


def getcolor(datalen, left, mid, right):
    colorlist = []

    for i in range(datalen):
        if left <= i <= right:
            if i <= mid:
                colorlist.append('deep sky blue')
            else:
                colorlist.append('salmon')
        else:
            colorlist.append('gray')
    return colorlist
