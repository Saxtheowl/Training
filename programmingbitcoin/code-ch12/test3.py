import fileinput

filename = "test4.py"
text_to_search = ">>> "
replacement_text = ""

with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace(text_to_search, replacement_text), end='')
