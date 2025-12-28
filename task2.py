def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    iterations = 0
    upper_bound = None

    while low <= high:
        iterations += 1
        mid = (low + high) // 2

        if arr[mid] < x:
            low = mid + 1
        else:
            upper_bound = arr[mid]
            
            high = mid - 1

    return iterations, upper_bound

sorted_array = [0.1, 0.5, 1.3, 1.8, 2.4, 3.7, 5.5]

# Test Case 1: Value exists exactly
target1 = 2.4
result1 = binary_search(sorted_array, target1)
print(f"Target: {target1}, Result: {result1}") 
# Expected: (iterations, 2.4) because 2.4 >= 2.4

# Test Case 2: Value does not exist, find next largest
target2 = 2.0
result2 = binary_search(sorted_array, target2)
print(f"Target: {target2}, Result: {result2}") 
# Expected: (iterations, 2.4) because 2.4 is the smallest number >= 2.0

# Test Case 3: Value larger than any element in array
target3 = 10.0
result3 = binary_search(sorted_array, target3)
print(f"Target: {target3}, Result: {result3}") 
# Expected: (iterations, None) because no element is >= 10.0
