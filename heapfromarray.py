def print_heap(arr):
	pass

def min_heapify(arr, i, n):
	smallest = i 
	l = i*2 + 1
	r = i*2 +2

	if l<n and arr[smallest]>arr[l]:
		smallest = l

	if r<n and arr[smallest]>arr[r]:
		smallest = r 

	if smallest!=i:
		arr[smallest], arr[i] = arr[i], arr[smallest]
		min_heapify(arr, smallest, n)


# Python3 program for implementation
# of Heap Sort
 
# To heapify a subtree rooted with
# node i which is an index in arr[].
# n is size of heap
def heapify(arr, n, i):
    smallest = i # Initialize smalles as root
    l = 2 * i + 1 # left = 2*i + 1
    r = 2 * i + 2 # right = 2*i + 2
 
    # If left child is smaller than root
    if l < n and arr[l] < arr[smallest]:
        smallest = l
 
    # If right child is smaller than
    # smallest so far
    if r < n and arr[r] < arr[smallest]:
        smallest = r
 
    # If smallest is not root
    if smallest != i:
        (arr[i],
         arr[smallest]) = (arr[smallest],
                           arr[i])
 
        # Recursively heapify the affected
        # sub-tree
        heapify(arr, n, smallest)

# main function to do heap sort
def heapSort(arr, n):
     
    # Build heap (rearrange array)
    for i in range(int(n / 2) - 1, -1, -1):
        heapify(arr, n, i)
 
    # One by one extract an element
    # from heap
    for i in range(n-1, -1, -1):
         
        # Move current root to end #
        arr[0], arr[i] = arr[i], arr[0]
 
        # call max heapify on the reduced heap
        heapify(arr, i, 0)


def max_heapify(arr, i, n):
	#n = len(arr)
	largest = i
	l = 2*i + 1
	r = 2*i + 2

	if l<n and arr[l]>arr[largest]:
		largest = l

	if r<n and arr[r]>arr[largest]:
		largest = r 

	if largest!=i:
		#print(arr, k)
		(arr[i], arr[largest]) = (arr[largest], arr[i])
		max_heapify(arr, largest, n)


def build_heap(arr):
	n = len(arr)
	start_index = n//2 - 1
	for i in range(start_index, -1, -1):
		min_heapify(arr, i, n)

	#print(arr)


def sortx(arr):
	n = len(arr)
	for i in range(n-1, -1, -1):
		arr[0], arr[i] = arr[i], arr[0]  # swap
		min_heapify(arr, 0, i)

	"""for i in range(n-1, -1, -1):
         
        # Move current root to end #
        arr[0], arr[i] = arr[i], arr[0]
 
        # call max heapify on the reduced heap
        heapify(arr, i, 0)
        """


		

arr = [0, 1, 8, 2, 3, 5, 5, 7, 4]

build_heap(arr)
print(arr)
sortx(arr)
print(arr)
heapSort(arr, 9)
print(arr)