with open("./Input/Names/invited_names.txt") as invited_names:
    names = invited_names.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    content = letter.read()
    for name in names:
        sender_name = name.strip("\n")
        edited_name = sender_name + ",\n"
        with open(f"./Output/ReadyToSend/letter_for_{sender_name}.txt", mode="w") as invitation_letter:
            invitation_letter.write(content.replace("[name],\n", edited_name))
