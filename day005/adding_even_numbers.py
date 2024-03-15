target = int(input("Enter a number between 0 and 1000 : "))

even_sum = 0
for num in range(0, target + 1, 2):
    even_sum += num

print(f"Sum of even numbers upto {target} = {even_sum}")