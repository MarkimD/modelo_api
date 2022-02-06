from flask_restful import Resource

lista_habilidades = ['Python', 'Java', 'Kotlin', 'On Rails', 'PHP']


class Habilidades(Resource):

    def get(self):
        return lista_habilidades