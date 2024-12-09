placeholder = '[name]'

with open('./input/names/invited_names.txt') as name_list:
    names = name_list.readlines()
with open('./input/letters/starting_letter.txt') as iletter:
    letter = iletter.read()
    for i in names:
        stripped_name = i.strip()
        separate_invite = letter.replace(placeholder,stripped_name)
        with open(f"./output/readytosend/letter_for_{stripped_name}.docx", mode = 'w') as final_invitation:
            final_invitation.write(separate_invite)