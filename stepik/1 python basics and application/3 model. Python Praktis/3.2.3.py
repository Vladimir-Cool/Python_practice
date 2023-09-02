import re, sys

pattern = r".*z.{3}z.*"

for line in sys.stdin:
    line = line.rstrip()
    result = re.match(pattern, line)
    if (result):
        print(line)