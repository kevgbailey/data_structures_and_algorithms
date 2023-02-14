def is_sorted(lyst):
    i = 0
    while i < len(lyst) - 1:
        if lyst[i] > lyst[i+1]:
            return False
        i = i + 1 
    return True

def quicksort(lyst):
    comparisons = 0
    swaps = 0
    def partition(array, low, high):
        nonlocal comparisons
        nonlocal swaps
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            comparisons += 1
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        swaps += 1
        return i + 1
    def quicksort_param(numbers, low, high):
        if low < high:
            pivot = partition(numbers, low, high)
            quicksort_param(numbers, low, pivot - 1)
            quicksort_param(numbers, pivot + 1, high)
    quicksort_param(lyst, 0, len(lyst) - 1)
    return lyst, comparisons, swaps

def selection_sort(lyst):
    comparisons = 0
    swaps = 0
    for i in range(len(lyst)):
        j = i + 1
        lowest = i
        while j < len(lyst):
            comparisons += 1
            if lyst[j] < lyst[lowest]:
                lowest = j
            j = j + 1
        lyst[i], lyst[lowest] = lyst[lowest], lyst[i]
        swaps += 1
    return lyst, comparisons, swaps


def insertion_sort(lyst):
    comparisons = 0
    swaps = 0
    for i in range(1, len(lyst)):
        j = i
        while j > 0:
            comparisons += 1
            if lyst[j] < lyst[j-1]:
                lyst[j-1], lyst[j] = lyst[j], lyst[j-1]
                swaps += 1
            j -= 1
    return lyst, comparisons, swaps
    

    
def mergesort(lyst):
    comparisons = 0
    swaps = 0
    def merge(numbers, i, j, k):
        nonlocal comparisons
        nonlocal swaps
        merge_spot = 0
        right_spot = j+1
        left_spot = i
        temp_array = [0] * (k-i+1)
        while left_spot <= j and right_spot <= k:
            comparisons += 1
            if numbers[left_spot] < numbers[right_spot]:
                temp_array[merge_spot] = numbers[left_spot]
                swaps += 1
                merge_spot += 1
                left_spot += 1
            else:
                temp_array[merge_spot] = numbers[right_spot]
                swaps += 1
                merge_spot += 1
                right_spot += 1
        while left_spot <= j:
            temp_array[merge_spot] = numbers[left_spot]
            swaps += 1
            merge_spot += 1
            left_spot += 1
        while right_spot <= k: 
            temp_array[merge_spot] = numbers[right_spot]
            swaps += 1
            merge_spot += 1
            right_spot += 1

        for merge_spot in range(k-i+1):
            numbers[i+merge_spot] = temp_array[merge_spot]


    def mergesort_param(numbers, i, k):
        j = 0
        if(i < k):
            j = (i+k)//2
            mergesort_param(numbers, i, j)
            mergesort_param(numbers, j+1, k)
            merge(numbers, i, j, k)
    
    mergesort_param(lyst, 0, len(lyst)-1)
    return lyst, comparisons, swaps




        

def main():
    pass
    

if __name__ == "__main__":
    main()

test_array = [1,45,79,23,56,11,2,6,-8,67,90,56,7,8,45,-78,-5,8,7,9,-36,82,56,-1023,567,34,-345]
print("Before sorting:")
print(test_array)
print("After sorting:")
print(quicksort(test_array))
print(is_sorted(test_array))