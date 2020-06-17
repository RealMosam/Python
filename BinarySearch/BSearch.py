print("Enter the list elements:")
arr = [int(x) for x in input().split()]
arr.sort()
print("Your list is:", arr)
pos = len(arr)-1

def BinarySearch(arr,item):
        l = 0
        u = len(arr) - 1

        while l <= u:
                mid = (l+u) // 2
                if arr[mid] == item:
                        globals() ['pos'] = mid
                        return print(item, "found at index:" ,pos+1)

                else:
                        if arr[mid] > item:
                                u = mid-1
                        else:
                                l = mid+1
        return print("Item:" ,item, "not found!")

print("Enter the item to search:")
item = int(input())

BinarySearch(arr,item)