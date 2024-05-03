list_of_strings = input().split(',')

list_of_numbers = [int(num) for num in list_of_strings]

result = [num for num in list_of_numbers if num % 2 == 0]

print(result)
