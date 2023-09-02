
def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')



'''Проверка метода .user_agent.browser'''
def test(req: 'flask_request'):
    with open('vsearch.log', 'a') as log:
        print(str(req.user_agent).split()[0], file=log)

'''Функция для проверки доступных методов для flask запроса'''
def Test_metod(req:'flask_request', res:str) -> None:
    with open('vsearch.log', 'a') as log:
        print(str(dir(req)), res, file=log)