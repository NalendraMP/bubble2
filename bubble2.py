def binarysearch(arr, start, end, x):
    if end >= start:
        mid = start + (end - start) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarysearch(arr, start, mid - 1, x)
        else:
            return binarysearch(arr, mid + 1, end, x)
    else:
        return -1

def bubblesort(x):
    for i in range(len(x)-1):
        for j in range(0, len(x)-i-1):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
    return x

def recursive_bubblesort(x):
    if len(x) <= 1:
        return x
    else:
        for i in range(len(x)-1):
            if x[i] > x[i+1]:
                x[i], x[i+1] = x[i+1], x[i]
        return recursive_bubblesort(x[:-1]) + [x[-1]]

def recursive_binarysearch(arr, start, end, x):
    if end >= start:
        mid = start + (end - start) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return recursive_binarysearch(arr, start, mid - 1, x)
        else:
            return recursive_binarysearch(arr, mid + 1, end, x)
    else:
        return -1

array = [87, 54, 34, 23, 89, 15, 2, 200, 28, 31]
sorted_array = recursive_bubblesort(array)
print("Sesudah di sorting:", sorted_array)

c = int(input("Masukkan angka yang dicari: "))
result = recursive_binarysearch(sorted_array, 0, len(sorted_array)-1, c)

if result != -1:
    print(f"terdapat Angka {c} di urutan ke : {result}")
else:
    print(f"Angka {c} tidak ditemukan dalam list")
