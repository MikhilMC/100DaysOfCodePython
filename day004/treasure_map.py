line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure?") 

'''
row_index = 0
col_index = 0

if position[0].upper() == "A":
    pass
elif position[0].upper() == "B":
    col_index = 1
else:
    col_index = 2

row_index = int(position[1]) - 1
map[row_index][col_index] = "X"
'''
letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
nummber_index = int(position[1]) - 1
map[nummber_index][letter_index] = "X"

print(f"{line1}\n{line2}\n{line3}")