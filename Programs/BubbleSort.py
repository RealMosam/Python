print("Enter the list elements:")

arr = [int(x) for x in input().split()]

def BubbleSort(arr):
        counter = 0
        for i in range(len(arr)-1,0,-1):
                for j in range(i):
                        if arr[j]>arr[j+1]:
                                 temp = arr[j]
                                 arr[j] = arr[j+1]
                                 arr[j+1] = temp
                print("Iterations No.",-(i-len(arr)+1)+(1))
                print(arr)



print("Your list before Bubble Sort:", arr)

BubbleSort(arr)

print("Your list after Bubble Sort:", arr)
