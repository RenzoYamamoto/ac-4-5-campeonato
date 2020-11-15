import json
import os

from database.classes import Equipe, Partida, Usuario


def carregar_dados(base_dir):
    with open(os.path.join(base_dir, 'dados.json')) as json_arq:
        dados = json.load(json_arq)
        carregar_equipes(dados['equipe'])
        carregar_partidas(dados['partida'])
        carregar_usuarios(dados['usuarios'])


def carregar_equipes(equipes):
    for equipe in equipes:
        Equipe.criar(
            equipe['nome'],
            equipe['sigla'],
            equipe['local']
        )
    print(f'Carregados {len(equipes)} equipes com sucesso!')


def carregar_partidas(partidas):
    for partida in partidas:
        Partida.criar(
            Equipe.obter(partida['equipe_casa']),
            Equipe.obter(partida['equipe_visita']),
            partida['gols_casa'],
            partida['gols_visita']
        )
    print(f'Carregados {len(partidas)} partidas com sucesso!')


def carregar_usuarios(usuarios):
    for usuario in usuarios:
        Usuario.criar(
            usuario['email'],
            usuario['senha']
        )
    print(f'Carregados {len(usuarios)} usuários com sucesso!')


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    carregar_dados(base_dir)