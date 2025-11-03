def quick_sort(numbers):
    lenght = len(numbers)
    if lenght <= 1:
        return numbers

    pivot = numbers.pop()
    high, low = [], []
    for number in numbers:
        if number > pivot:
            high.append(number)
        else:
            low.append(number)
    return quick_sort(low) + [pivot] + quick_sort(high)

number_list = [10,5,12,1,9,7]
print(quick_sort(number_list))
