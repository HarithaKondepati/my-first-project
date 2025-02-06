# Sorting Algorithm Visualizer

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                print(f"Bubble Sort Step {i+1}-{j+1}: {arr}")
        if not swapped:
            break
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f"Insertion Sort Step {i}: {arr}")
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

# Taking user input
arr = list(map(int, input("Enter numbers separated by space: ").split()))

print("\nChoose Sorting Algorithm:")
print("1. Bubble Sort")
print("2. Insertion Sort")
print("3. Quick Sort")
print("4. Merge Sort")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    print(f"\nOriginal Array: {arr}")
    bubble_sort(arr)
    print(f"Sorted Array (Bubble Sort): {arr}")

elif choice == 2:
    print(f"\nOriginal Array: {arr}")
    insertion_sort(arr)
    print(f"Sorted Array (Insertion Sort): {arr}")

elif choice == 3:
    print(f"\nOriginal Array: {arr}")
    sorted_arr = quick_sort(arr)
    print(f"Sorted Array (Quick Sort): {sorted_arr}")

elif choice == 4:
    print(f"\nOriginal Array: {arr}")
    merge_sort(arr)
    print(f"Sorted Array (Merge Sort): {arr}")

else:
    print("Invalid choice! Please run the program again.")
