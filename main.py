# 0 задание

def findGreaterElements(list):
    greater_elements = []
    for i in range(1, len(list)):
        if list[i] > list[i-1]:
            greater_elements.append(list[i])
    return greater_elements

list = input("Введите числовую последовательность: ").split()
list = [int(x) for x in list]
result = findGreaterElements(list)
print(result)

# 1 задание

def swapMinMax(list):
    if len(list) < 2:
        return list

    min_index = 0
    max_index = 0
    for i in range(1, len(list)):
        if list[i] < list[min_index]:
            min_index = i
        if list[i] > list[max_index]:
            max_index = i

    list[min_index], list[max_index] = list[max_index], list[min_index]
    return list

list = input("Введите числовую последовательность: ").split()
list = [int(x) for x in list]
result = swapMinMax(list)
print(result)

# 2 задание

def countCommonNumbers(list1, list2):
    common_numbers = set(list1) & set(list2)
    return len(common_numbers)

list1 = input("Введите первую числовую последовательность: ").split()
list1 = [int(x) for x in list1]
list2 = input("Введите вторую числовую последовательность: ").split()
list2 = [int(x) for x in list2]
result = countCommonNumbers(list1, list2)
print(result)

# 3 задание

def countStringOccurrences(list):
    occurrences = {}
    for string in list:
        if string in occurrences:
            occurrences[string] += 1
        else:
            occurrences[string] = 1
    return occurrences

list = input("Введите строки через пробел: ").split()
occurrences = countStringOccurrences(list)
for string, count in occurrences.items():
    print(count, end=" ")

