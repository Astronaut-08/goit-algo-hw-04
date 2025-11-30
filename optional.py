'''Дано k відсортованих списків цілих чисел. Ваше завдання — об'єднати
їх у один відсортований список. При виконанні завдання можете опиратися
на алгоритм сортування злиттям з конспекту. Реалізуйте функцію merge_k_lists,
яка приймає на вхід список відсортованих списків та повертає відсортований список.'''

def merge_k_lists(lists: list[list]) -> list:
    '''Merge lists'''
    sorted_lst = []

    for lst in lists:
        sorted_lst += lst # merge in main list
        # use insertion sort for each list
        for i in range(len(sorted_lst)-1):
            key = sorted_lst[i]
            j = i - 1
            while j >= 0 and key < sorted_lst[j]:
                sorted_lst[j+1] = sorted_lst[j]
                j -= 1
            sorted_lst[j+1] = key

    return sorted_lst

lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
