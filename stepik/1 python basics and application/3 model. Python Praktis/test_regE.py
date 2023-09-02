import re, sys

pattern = r"cat"

for line in sys.stdin:
    line = line.rstrip()
    print(re.match(pattern, line))
    print(re.search(pattern, line))
    print(re.findall(pattern, line))
    print(re.sub(pattern, '0', line))