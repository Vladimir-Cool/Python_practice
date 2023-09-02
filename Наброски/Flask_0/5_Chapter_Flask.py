from flask import Flask, render_template, request, escape
from myfun import serch4letters
from DBcm import UserDataBase


app = Flask(__name__)

app.config['dbconfig'] = {'host': '127.0.0.1',
                'user': 'python',
                'password': 'python123',
                'database': 'vsearchlogDB', }

def log_request(req:'flask_request', res: str) -> None:
    with UserDataBase(app.config['dbconfig']) as cursor:
        _SQL = """insert into log 
                (phrase, letters, ip, browser_string, results) 
                values 
                (%s, %s, %s, %s, %s)"""
        cursor.execute(_SQL, (req.form['phrase'],
                          req.form['letters'],
                          req.remote_addr,
                          str(req.user_agent).split()[0],  #Отрезаю название браузера. Беру первое слово в строке
                          res,))

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                        the_title = 'Добро пожаловать в WEB!')


@app.route('/search4', methods=['POST'])
def do_search () -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    result = str(serch4letters(phrase, letters))
    #test(request)
    log_request(request, result)
    return render_template('result.html',
                           the_title = 'Ваш результат',
                           the_phrase = phrase,
                           the_letters = letters,
                           the_results = result)


@app.route('/viewlog')
def viewe_the_log() ->str:

    with UserDataBase(app.config['dbconfig']) as cursor:
        _SQL="""select phrase, letters, ip, browser_string, results from log"""
        cursor.execute(_SQL)
        contents = cursor.fetchall()
    titles = ('Select phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results')
    return render_template('log.html',
                           the_title = 'История запросов',
                           the_row_titles = titles,
                           the_data = contents)


if __name__ == '__main__':
    app.run(debug=True) #вносимые изменения будут сразу применятьс, без перезапуска сервиса.