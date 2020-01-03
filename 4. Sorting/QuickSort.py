def quickSort(arr):
    _quickSort(arr, 0, len(arr) - 1)
    return arr

def _quickSort(arr, lo, hi):
    if lo >= hi:
        return
    pivot = partition(arr, lo, hi)
    _quickSort(arr, lo, pivot - 1)
    _quickSort(arr, pivot + 1, hi)

def partition(arr, lo, hi):
    pivot = arr[lo]
    swap_index = lo + 1
    for i in range(lo + 1, hi + 1):
        if arr[i] < pivot:
            arr[i], arr[swap_index] = arr[swap_index], arr[i]
            swap_index += 1
    arr[lo], arr[swap_index - 1] = arr[swap_index - 1], arr[lo]
    return swap_index - 1


