def decorator (func):

    def inner(*args, **kwargs):
        print('Начало декоратора')
        func(*args, **kwargs)
        print('Конец декоратора')

    return inner

def decorator2 (func):

    def inner(*args, **kwargs):
        print('Начало 2')
        func(*args, **kwargs)
        print('Конец 2')

    return inner

@decorator2
@decorator
def say(name, surname, age):
    print('Hello' ,name, surname, age)

#say = decorator(say)
say('Vova', 'Cool', 30)