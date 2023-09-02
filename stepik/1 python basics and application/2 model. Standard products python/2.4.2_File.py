
with open('dataset_24465_4.txt') as f, open('dataset_24465_4rev.txt', 'w') as w:
        lst = f.read()
        rev = lst.splitlines()[::-1]
        print(rev)
        contents = '\n'.join(rev)
        w.write(contents)
