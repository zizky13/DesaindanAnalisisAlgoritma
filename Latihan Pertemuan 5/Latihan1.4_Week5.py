def divideAndConquer_Max(arr,ind,len):
    maximum = -1

    if (ind >= len - 2):
        if (arr[ind] > arr[ind + 1]):
            return arr[ind]
        else:
            return arr[ind+1]

    maximum = divideAndConquer_Max(arr,ind+1,len)

    if (arr[ind] > maximum):
        return arr[ind]
    else:
        return maximum

def divideAndConquer_Min(arr, ind, len):
    minimum = 0
    if (ind >= len - 2):
        if(arr[ind] < arr [ind + 1]):
            return arr[ind]
        else:
            return arr[ind + 1]

    minimum = divideAndConquer_Min(arr, ind + 1, len)

    if (arr[ind] < minimum):
        return arr[ind]
    else:
        return minimum

if __name__ == '__main__':
    minimum, maximum = 0, -1

    arr = [4,12,23,9,21,1,35,2,24]

    maximum = divideAndConquer_Max(arr, 0, 9)
    minimum = divideAndConquer_Min(arr, 0, 9)

    print("The minimum number in array is: ", minimum)
    print("The maximum number in array is: ", maximum)