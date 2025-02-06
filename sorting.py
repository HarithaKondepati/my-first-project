"#sorting Algo Visualizer" 
def bubble_sort(arr):
	n = len(arr)
	for i in range(n):
		swapped = False
		for j in range(n-i-1):
			if arr[j] > arr[j + 1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swapped = True
				print(f"Step {i+1} - {j+1}: {arr}")
		if not swapped:
			break

arr = [64, 25, 12, 22, 11]
print(f"Original Array: {arr}")
bubble_sort(arr)
print(f"Sorted Array: {arr}")
