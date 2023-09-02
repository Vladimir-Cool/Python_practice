
def wordsindict(dictionary:list, text:list) -> list:
    goodwords = set(dictionary)
    for word in dictionary:
        for delpos in range(len(word)):
            goodwords.add(word[:delpos] + word[delpos+1:])
    ans = []
    for word in text:
        ans.append(word in goodwords)
    return ans

A = ['abc', 'acb', 'cab']
Word = ['ab', 'fg', 'acb', 'ddd']

print(wordsindict(A, Word))