from flask import Flask
import pymysql

db = pymysql.connect("localhost", "root", "1234", "datalive")
app = Flask(__name__)


@app.route('/cadastro', methods=['GET', 'POST'])
def novo1():
    usuarios = {}
    lista = []
    cursor = db.cursor()
    cursor.execute("SELECT * FROM datalive.usuario")
    results = cursor.fetchall()
    for linha in results:
        aux = {'id':linha[0],'nome':linha[1],'senha':linha[2],'pontuacao':linha[3],'tipo':linha[4]}
        lista.append(aux)
        usuarios.update(usuario=lista)

    return usuarios

if __name__ == '__main__':
    app.run()