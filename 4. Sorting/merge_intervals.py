
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    output = []
    if not intervals:
        return []
    arr = sorted(intervals, key = lambda x:x[0])
    print(arr)
    for i in arr:
        if not output or output[-1][1] < i[0]:
            output.append(i)
        else:
            output[-1][1] = max(i[1],output[-1][1])

    return output
