# 选择排序
# 时间复杂度 O(n^2)

# 从小到大排序

def findSmallItem(arr):
    min_item = arr[0]
    min_item_index = 0
    for i in range(1, len(arr)):
        if arr[i] < min_item:
            min_item = arr[i]
            min_item_index = i
    return min_item_index


def selectionSort(arr):
    new_array = []
    for i in range(len(arr)):
        small_index = findSmallItem(arr)
        new_array.append(arr.pop(small_index))
    return new_array


if __name__ == '__main__':
    arr = [2, 20, 39, 6, 19]

    array = selectionSort(arr)

    print(array)
