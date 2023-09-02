
def countbeatingrooks(rookcoords:list) -> int:
    def addrook(roworcol, key):
        if key not in roworcol:
            roworcol[key] = 0
        roworcol[key] += 1

    def countpairs(roworcol):
        pairs = 0
        for key in roworcol:
            pairs += roworcol[key] - 1
        return pairs

    rooksinrow = {}
    rooksincol = {}
    for row, col in rookcoords:
        addrook(rooksinrow, row)
        addrook(rooksincol, col)
    return countpairs(rooksinrow) + countpairs(rooksincol)

