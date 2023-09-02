
# f = open('test1.txt', 'w')
# line = ['Line1', 'Line2', 'Line3']
# contents = '\n'.join(line)
# f.write(contents)
# f.close()



with open('test1.txt') as f, open('testcopi.txt', 'w') as w:
    for line in f:
        w.write(line)
