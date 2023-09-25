def findClosest(lst, k):
    lst.sort()
    closestNum = lst[0]
    for num in lst:
        if abs(num - k) < abs (closestNum - k):
            closestNum = num
        if num > k:
            break
    return closestNum

lst = [3.64,5.2,9.42,9.35,8.5,8]
k = 9.1
print(findClosest(lst,k))