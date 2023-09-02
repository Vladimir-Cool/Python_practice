phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
new_phrase = plist[1:3] + plist[5:3:-1] + plist[7:5:-1]

print(new_phrase)
print(''.join(new_phrase))  # Как это работает???