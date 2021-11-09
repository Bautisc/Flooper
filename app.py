import MySQLdb
from flask import Flask, config, jsonify, request, session, redirect, url_for
from flask.templating import render_template
from flask_mysqldb import MySQL
from config import config

app = Flask(__name__)
mysql = MySQL(app)

#Home#


@app.route('/', methods=['GET'])
def home():
    # Output message if something goes wrong...
    msg = ''
    return render_template('index.html', msg='')


@app.route('/Flooper/<username>', methods=['GET'])
def pag_principal(username):
    if 'loggedin' in session:
        return render_template('home.html', username=session['username'])
    return redirect(url_for('/'))

# Login - Register -Logout#


@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ""
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'SELECT * FROM usuarios WHERE username = % s AND password = % s', (username, password, ))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['ID'] = account['ID']
            session['username'] = account['username']
            msg = 'Login exitoso!'
            return render_template('index.html', msg=msg)
        else:
            msg = 'Usuario o contraseña incorrectos!'
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

    #Tareas #


@app.route('/Tareas', methods=['GET'])
def Tareas():
    try:
        cursor = mysql.connection.cursor()
        sql = "SELECT id_tarea, Titulo, Estado FROM tareas"
        cursor.execute(sql)
        datos = cursor.fetchall()
        tareas = []
        for fila in datos:
            tarea = {'id_tarea': fila[0], 'Titulo': fila[1], 'Estado': fila[2]}
            tareas.append(tarea)
        return jsonify({'Tarea': tareas, 'mensaje': "Tareas listadas."})
    except Exception as ex:
        return jsonify({'mensaje': "Error"})


@app.route('/Tareas/<id_tarea>', methods=['GET'])
def leer_tareas(id_tarea):
    try:
        cursor = mysql.connection.cursor()
        sql = "SELECT id_tarea, Titulo, Estado FROM tareas WHERE id_tarea = '{0}'".format(
            id_tarea)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            tareas = {'id_tarea': datos[0],
                      'Titulo': datos[1], 'Estado': datos[2]}
            return jsonify({'Tarea': tareas, 'mensaje': "Tarea encontrada."})
        else:
            return jsonify({'mensaje': "Tarea no encontrada"})
    except Exception as ex:
        return jsonify({'mensaje': "Error"})

# Metodo POST


@app.route('/Tareas', methods=['POST'])
def registrar_Tarea():
    # print(request.json)
    try:
        cursor = mysql.connection.cursor()
        _json = request.json
        sql = """INSERT INTO tareas (id_tarea, Titulo, Estado) 
        VALUES ({0},'{1}','{2}')""".format(_json['id_tarea'], _json['Titulo'], _json['Estado'])
        cursor.execute(sql)
        mysql.connection.commit()
        return jsonify({'mensaje': "Tarea registrada."})
    except Exception as ex:
        return jsonify({'mensaje': "Error"})

    # Metodo DELETE


@app.route('/Tareas/<id_tarea>', methods=['DELETE'])  # Funcionando
def eliminar_tarea(id_tarea):
    try:
        cursor = mysql.connection.cursor()
        sql = "DELETE FROM tareas WHERE id_tarea = '{0}'".format(id_tarea)
        cursor.execute(sql)
        mysql.connection.commit()
        return jsonify({'mensaje': 'Tarea eliminada'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error'})

 # Metodo PUT


@app.route('/Tareas/<id_tarea>', methods=['PUT'])  # Funcionando
def actualizar_tarea(id_tarea):
    try:
        cursor = mysql.connection.cursor()
        _json = request.json
        sql = """UPDATE tareas SET Titulo = '{0}', Estado = '{1}' WHERE id_tarea = '{2}'""".format(
            _json['Titulo'], _json['Estado'], id_tarea)
        cursor.execute(sql)
        mysql.connection.commit()
        return jsonify({'mensaje': 'Tarea actualizada'})
    except Exception as ex:
        return jsonify({'mensaje': 'Error'})


def pagina_no_encontrada(error):
    return "<h1>La página que intentas buscar no existe...</h1>", 404


app.secret_key = "ab947a9e8c14bde1b32419e5af7abaee6b4f77c055a46d3685eba3850bcac3f2"

if __name__ == '__main__':
    app.config.from_object(config['desarrollo'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()
