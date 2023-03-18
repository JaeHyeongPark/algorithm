import sys
N = int(sys.stdin.readline())
array_N = sorted(list(map(int, sys.stdin.readline().split(" "))))
M = int(sys.stdin.readline())
array_M = list(map(int, sys.stdin.readline().split(" ")))

# def binary_search(array, search):
#     n = len(array)
#     if n == 1:
#         if array[0] == search:
#             return True
#         else:
#             return False
#     if n == 0:
#         return False
    
#     mid = n // 2

#     if array[mid] == search:
#         return True
#     elif array[mid] > search:
#         return binary_search(array[:mid], search)
#     else:
#         return binary_search(array[mid+1:], search)

def binary_search(start, end, arr, num):
    while start <= end:
        mid = (start + end)//2
        if arr[mid] == num:
            return True
        elif arr[mid] > num:
            end = mid-1
        else:
            start = mid+1

for elem in array_M:
    if binary_search(0, N-1, array_N, elem):
        print(1)
    else:
        print(0)
