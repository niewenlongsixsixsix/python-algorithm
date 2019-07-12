import math


def search_number(arr: list, item: int):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) / 2
        temp = arr[math.floor(mid)]
        if temp == item:
            return True
        elif temp > item:
            end = mid - 1
        else:
            start = mid + 1
    return False


if __name__ == '__main__':
    a = [1, 2, 3, 4, 30, 40, 60]
    print(search_number(a, 90))
