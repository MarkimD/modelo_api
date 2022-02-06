from flask import Flask, request
from habilidades import Habilidades
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

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


class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = f'Desenvolvedor de ID {id} não existe.'
            response = {'Status': 'erro', 'Mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido, entre em contato com o administrador do Sistema.'
            response = {'Status': 'erro', 'Mensagem': mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'Status': 'sucesso', 'Mensagem': 'Registro excluído com sucesso.'}


class ListaDesenvolvedores(Resource):

    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]


api.add_resource(Desenvolvedor, '/dev/<int:id>')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')

if __name__ == '__main__':
    app.run(debug=True)