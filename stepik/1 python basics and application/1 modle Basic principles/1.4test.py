import collections


def bfs(graph, root):
    visited, queue = set(), collections.deque([root])
    visited.add(root)
    while queue:
        vertex = queue.popleft()
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


testfinde = {'global':  {'parent': None, 'variables' : [],
                        'foo': {'parent': 'global', 'variables': []},
                        'new': {'parent': 'global', 'variables': [],
                                'new2': {'parent': 'new', 'variables': []}}}}

finddict = dict()
#def findespace(desired, ):

print(testfinde['global']['foo'])
print(testfinde['global']['new'])
