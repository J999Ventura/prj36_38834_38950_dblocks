from flask import render_template, Flask
from forms import RegisterForm, LoginForm
app = Flask(__name__)

# Aplication key, to not allow xss, or injections on forms
app.config['SECRET_KEY'] = '22b9dac894bfa6b43fb78e8c14ef7ce058839cae87d38b31c893967343491ece'


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='BBlocks');


@app.route('/register')
def register():
    form = RegisterForm()
    return render_template('register.html', title='Register', form=form);


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('index.html', title='Login', form=form);

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)