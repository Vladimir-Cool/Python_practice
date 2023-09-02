from flask import Flask, session
from ChapterDekorator import Chek_Logged

app = Flask(__name__)

app.secret_key = 'YouWillNeverGuess'

@app.route('/')
def hello() -> str:
    return 'Hello from the simple webapp.'

@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'Вы в системе'

@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'Вы вышли из системы'

#@app.route('/status')
#def do_login_status() -> str:
#    if 'logged_in' in session:  #Проверяет наличие ключа в словаре!!!
#        return 'Вы сейчас в системе'
#    return 'Вы НЕ в системе'

@app.route('/page1')
@Chek_Logged
def page1() -> str:
    return 'This is page 1.'

@app.route('/page2')
@Chek_Logged
def page2() -> str:
    return 'This is page 2.'

@app.route('/page3')
@Chek_Logged
def page3() -> str:
    return 'This is page 3.'

if __name__ == '__main__':
 app.run(debug=True)