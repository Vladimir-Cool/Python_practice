import re, sys

pattern = r"\bcat\b"

for line in sys.stdin:
    line = line.rstrip()
    result = re.search(pattern, line)
    if (result):
        print(line)
