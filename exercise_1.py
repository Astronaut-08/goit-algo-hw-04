'''Порівняйте три алгоритми сортування: злиттям, вставками
та Timsort за часом виконання. Аналіз повинен бути
підтверджений емпіричними даними, отриманими шляхом
тестування алгоритмів на різних наборах даних. Емпірично
перевірте теоретичні оцінки складності алгоритмів, наприклад,
сортуванням на великих масивах.'''

import timeit
import random

############################################### Functions merge_sort from conspect
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
############################################### Function insertion from conspect
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst
###############################################

num_test_short = 100000
num_test_long = 1000

print('-'*20, 'Короткі масиви', '-'*20)
mrg = timeit.timeit(
    stmt='merge_sort([random.randrange(100) for _ in range(10)])',
    setup='from __main__ import merge_sort, random',
    number=num_test_short

)

insrt = timeit.timeit(
    stmt='insertion_sort([random.randrange(100) for _ in range(10)])',
    setup='from __main__ import insertion_sort, random',
    number=num_test_short

)

timsort = timeit.timeit(
    stmt='sorted([random.randrange(100) for _ in range(10)])',
    setup='from __main__ import random',
    number=num_test_short

)

print(f'Час виконання сортування злиттям: {mrg:.3f} секунд.')
print(f'Час виконання сортування вставками: {insrt:.3f} секунд.')
print(f'Час виконання сортування timsort: {timsort:.3f} секунд.')


print('\n','-'*20, 'Довгі масиви', '-'*20)
mrg = timeit.timeit(
    stmt='merge_sort([random.randrange(100) for _ in range(1000)])',
    setup='from __main__ import merge_sort, random',
    number=num_test_long

)

insrt = timeit.timeit(
    stmt='insertion_sort([random.randrange(100) for _ in range(1000)])',
    setup='from __main__ import insertion_sort, random',
    number=num_test_long

)

timsort = timeit.timeit(
    stmt='sorted([random.randrange(100) for _ in range(1000)])',
    setup='from __main__ import random',
    number=num_test_long

)

print(f'Час виконання сортування злиттям: {mrg:.3f} секунд.')
print(f'Час виконання сортування вставками: {insrt:.3f} секунд.')
print(f'Час виконання сортування timsort: {timsort:.3f} секунд.')
