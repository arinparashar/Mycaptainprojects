def print_positive_numbers(numbers):
    positive_numbers = [num for num in numbers if num > 0]
    print("Output:", ", ".join(str(num) for num in positive_numbers))


# For example
list1 = [12, -7, 5, 64, -14]
print("Input:", list1)
print_positive_numbers(list1)

list2 = [12, 14, -95, 3]
print("Input:", list2)
print_positive_numbers(list2)
