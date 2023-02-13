def search(arr,item):
        for i in range(len(arr)):
                if arr[i] == item:
                        return print("Element found at Index:", i+1)
        return print("Element not found.")


print("Enter the list values:")

arr = [str(x) for x in input().split()]

print("Your list is:", arr)

item = str(input("Enter the value to be searched:"))

search(arr,item)

