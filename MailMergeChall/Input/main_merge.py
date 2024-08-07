with open("Input/Names/names.txt") as file_name:
    name_list = file_name.readlines()

invited_names = []

for name in name_list:
    mod_name = name.strip("\n")
    invited_names.append(mod_name)

with open("Input/Letters/base_letter.txt", mode="r") as base_letter:
    base_letter_txt = base_letter.read()

for name in invited_names:
    with open(f"Output/ReadyEmails/{name}_invite.txt", mode="w") as new_letter:
        invite_letter = base_letter_txt.replace("{name}", name)
        new_letter.write(invite_letter)
    


