import re
import MySQLdb
from flask import Flask, config, jsonify, request, session, redirect, url_for
from flask.templating import render_template
from flask_mysqldb import MySQL
from config import config

app = Flask(__name__)
mysql = MySQL(app)

#Home#


@app.route('/', methods=['GET'])
def index():
    # Output message if something goes wrong...
    msg = ''
    return render_template('index.html', msg='')


@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/flooper/<username>', methods=['GET'])
def pag_principal(username):
    print(username)
    if 'loggedin' in session:
        print("entro al if del login")
        return redirect(url_for('login', username=session['username']))
    return render_template('home.html')

# Login - Register -Logout#


@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ""
    print("printed")
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)  #
        cursor.execute(
            'SELECT * FROM usuarios WHERE username = % s AND password = % s', (username, password))
        account = cursor.fetchone()
        print(username)
        print(password)
        if account:
            session['loggedin'] = True
            session['ID'] = account['ID']
            session['username'] = account['username']
            msg = 'Login exitoso!'
            print(msg)
            return "Login completado con exito"
        else:
            msg = 'Usuario o contraseña incorrectos!'
            print(msg)
    return render_template('login.html', msg=msg)


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('ID', None)
    session.pop('username', None)
    return redirect(url_for('/'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['Email']
        cursor = mysql.connection.cursor()  # MySQLdb.cursors.DictCursor
        cursor.execute(
            'SELECT * FROM usuarios WHERE username = %s', (username,))
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            msg = 'Nombre de usuario ocupado.'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Ingrese una dirrecion email valida.'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'El nombre de usuario solo puede contener letras y números'
        elif not username or not password or not email:
            msg = 'Porfavor completa todos los campos del formulario'
        else:
            cursor.execute(
                'INSERT INTO usuarios (username, password, Email) VALUES(%s, %s, %s)', (username, password, email))
        mysql.connection.commit()
        cursor.close()
        return "Registro completado con exito."
    return render_template('register.html', msg=msg)


def pagina_no_encontrada(error):
    return "<h1>La página que intentas buscar no existe...</h1>", 404


app.secret_key = "ab947a9e8c14bde1b32419e5af7abaee6b4f77c055a46d3685eba3850bcac3f2"

if __name__ == '__main__':
    app.config.from_object(config['desarrollo'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()
