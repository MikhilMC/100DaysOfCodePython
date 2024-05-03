with open("file1.txt") as file1:
  file1_number_strings = file1.readlines()
with open("file2.txt") as file2:
  file2_number_strings = file2.readlines()

file1_numbers = [int(num) for num in file1_number_strings]
file2_numbers = [int(num) for num in file2_number_strings]
result = [num for num in file1_numbers if num in file2_numbers]

print(result)
