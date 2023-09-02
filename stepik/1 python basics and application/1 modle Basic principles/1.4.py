
'''Создание нового пространства "namespace" внутри "parent"'''
def create(namespace, parent, context = 'scope'):
    if parent in context:
        context[parent].setdefault(namespace, {'parent': parent})
    else:
        for space in context:
            create(namespace, parent, space)


def add(namespace, var):
    pass


def get(namespace, var):
    pass


testfinde = {'global':  {'parent': None,
                        'foo': {'parent': 'global'},
                        'new': {'parent': 'global',
                                'new2': {'parent': 'new'}}}}


finddict = dict()
def findespace(desired, ):
    for spase in contex.keys():
        if spase != parent:
            pathtospace = spase
        return pathtospace
    else:
        for space in contex:
            contex[space]
        return 'ошибка'


scope = {'global' : {'parent': None,}}

print(testfinde['global'])
print(testfinde['global']['foo'])
print(findespace('foo'))


#create('foo', 'global')
#create('new', 'foo')
#print(scope)




