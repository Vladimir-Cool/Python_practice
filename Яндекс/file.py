with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
    result = 0
    for line in infile:
        for letter in line.split():
            result = result + int(letter)
    outfile.write(str(result))