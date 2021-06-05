def checkUnimodal(arr, n):
    i = 1
    while (i < n and arr[i] > arr[i - 1]):
        i += 1

    while (i < n and arr[i] == arr[i - 1]):
        i += 1

    while (i < n and arr[i] < arr[i - 1]):
        i += 1

    return (i == n)

if __name__ == '__main__':
    arr = [1,0,100]
    n = len(arr)
    if (checkUnimodal(arr, n)):
        print("Yes")
    else:
        print("No")

