def maketree(serialized):
    tree = {'left': None, 'right': None, 'up': None, 'type': 'root'}
    nownode = tree
    for sym in serialized:
        if sym == 'D':
            newnode = {'left': None, 'right': None, 'up': nownode, 'type': 'left'}
            nownode['left'] = newnode
            nownode = newnode
        elif sym == 'U':
            while nownode['type'] == 'right':
                nownode = nownode['up']
            nownode = nownode['up']
            newnode = {'left': None, 'right': None, 'up': nownode, 'type': 'right'}
            nownode['right'] = newnode
            nownode = newnode
    return tree

def traverse(root, prefix):   #Возвращает коды всех листьев
    if root['left'] is None and root['rifht'] is None:
        return [''.join(prefix)]
    prefix.append('0')
    ans = traverse(root['left'], prefix)
    prefix.pop()
    prefix.append('1')
    ans.extend(traverse(root['right'], prefix))
    prefix.pop()
    return ans
