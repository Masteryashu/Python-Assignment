def rotate_array(arr, N):
    rotations = N % len(arr)
    # rotate the array using a loop
    for i in range(rotations):
        arr.insert(0, arr.pop())
    return arr

arr = [3,1,2,5,7]
N = 2
result = rotate_array(arr, N)
print(result)
