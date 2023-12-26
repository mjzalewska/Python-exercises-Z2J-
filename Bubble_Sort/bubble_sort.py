def bubble_sort(input_list):
    sorted_list = input_list.copy()
    while True:
        ordered = False
        for i in range(len(input_list) - 1):
            if sorted_list[i] > sorted_list[i + 1]:
                sorted_list[i], sorted_list[i + 1] = sorted_list[i + 1], sorted_list[i]
                ordered = True
        if not ordered:
            break
    return sorted_list


print(bubble_sort([10, 5, 1, 3, 1]))
print(bubble_sort([2, 1, 3, 0, 1, 1, 4, 9, 3]))
print(bubble_sort([10, 1, 20, 3, 2, 1, 5, 18, 15]))
