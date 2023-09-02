
def groupwords(words:list) -> list:
    def keybyword(word:str) -> str:
        symcount = {}
        for sym in word:
            if sym not in symcount:
                symcount[sym] = 0
            symcount[sym] += 1
        lst = []
        for sym in sorted(symcount.keys()):
            lst.append(sym)
            lst.append(str(symcount[sym]))
        return ''.join(lst)

    groups = {}
    for word in words:
        sortedword = keybyword(word)
        if sortedword not in groups:
            groups[sortedword] = []
        groups[sortedword].append(word)
    ans = []
    for sortedword in groups:
        ans.append(groups[sortedword])
    return ans


A = ["eat", "tea", "tan", "ate", "nat", "bat", "rarte", "22a00", "022a0", "0a022"]

print(groupwords(A))


