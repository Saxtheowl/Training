import sys, pyperclip

# add bullet star at the begining of each line

text = pyperclip.paste()
new_text = text.split('\n')

for i in range(len(new_text)):
    new_text[i] = '* ' + new_text[i]

#print('old:' + str(new_text))
text = '\n'.join(new_text)
pyperclip.copy(text)
