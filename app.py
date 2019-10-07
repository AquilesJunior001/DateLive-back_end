from flask import Flask
from flask_cors import CORS
import pymysql

db = pymysql.connect("localhost", "root", "1234", "datalive")
app = Flask(__name__)
CORS(app)

@app.route('/select', methods=['GET', 'POST'])
def select():
    try:
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

    except Exception as e:
        print(e)

    finally:
        cursor.close()

@app.route('/update/<num>/<pont>', methods=['PUT'])
def update(num,pont):
    try:
        nume = num
        pontu = pont
        cursor = db.cursor()
        query = "UPDATE datalive.usuario SET pontuacao = pontuacao + %s WHERE id = %s"
        data = (pontu,nume)
        cursor.execute(query,data)
        db.commit()
        return 'Alterado com Sucesso'

    except Exception as e:
        print(e)

    finally:
        cursor.close()

@app.route('/insert/<nom>/<senh>', methods=['POST'])
def insert(nom,senh):
    try:
        nome = nom
        senha = senh
        cursor = db.cursor()
        query = "INSERT INTO datalive.usuario (nome,senha) VALUES (%s,%s)"
        data = (nome, senha)
        cursor.execute(query, data)
        db.commit()
        return 'Inserido com Sucesso'

    except Exception as e:
        print(e)

    finally:
        cursor.close()

@app.route('/delete/<num>', methods=['DELETE'])
def delete(num):
    try:
        nume = num
        cursor = db.cursor()
        query = "DELETE FROM datalive.usuario WHERE id = %s"
        data = (nume)
        cursor.execute(query, data)
        db.commit()
        return 'Morte Matada'

    except Exception as e:
        print(e)

    finally:
        cursor.close()

if __name__ == '__main__':
    app.run()