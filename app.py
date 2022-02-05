from flask import Flask, jsonify, request
import json

app = Flask(__name__)

desenvolvedores = [
    {
        'id': 0,
        'Nome': 'Marcus Daniel',
        'Habilidades': ['Python', 'Machine Learning', 'Deep Learning']
    },

    {
        'id': 1,
        'Nome': 'Clelson Sales',
        'Habilidades': ['Java', 'SQL', 'Gestão']
    },
    {
        'id': 2,
        'Nome': 'Filipe Bogalho',
        'Habilidades': ['React js', 'HTML 5', 'CSS']

    }
]


# Devolve um desenvolvedor pelo ID e também Altera e Deleta o registro
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = f'Desenvolvedor de ID {id} não existe.'
            response = {'Status': 'erro', 'Mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido, entre em contato com o administrador do Sistema.'
            response = {'Status': 'erro', 'Mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'Status': 'sucesso', 'Mensagem': 'Registro excluído com sucesso.'})


# lista registro de Desenvolvedores e inclui e registra um novo desenvolvedor
@app.route('/dev', methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)






if __name__ == '__main__':
    app.run(debug=True)