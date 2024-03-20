import timeit
import random
from collections import defaultdict
import matplotlib.pyplot as plt

def generate_list(n):
    return list(random.sample(range(0, 99999), n))

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def execute_time(sort, list):
    starttime = timeit.default_timer()
    sort(list)
    return timeit.default_timer() - starttime

def main():
    data = []
    for i in range(1, 4):
        data.append(generate_list(5 * (10 ** i)))
    
    res = defaultdict(list)

    for list_ in data:
        insertion_time = execute_time(insertion_sort,list_)
        merge_time = execute_time(merge_sort,list_)
        sorted_time = execute_time(sorted,list_)
        res['Insertion'].append(insertion_time)
        res['Merge'].append(merge_time)
        res['Timsort'].append(sorted_time)
        
        print(f"For list of size {len(list_)}:")
        print(f"\tInsertion - {insertion_time}")
        print(f"\tMerge - {merge_time}")
        print(f"\tTimsort - {sorted_time}")
    
    fig, ax = plt.subplots()
    colors = ['tab:red', 'tab:green', 'tab:blue']

    for i, (key, values) in enumerate(res.items()):
        ax.scatter([key] * len(values), values, color=colors[i])

    plt.show()

if __name__ == "__main__":
    main()