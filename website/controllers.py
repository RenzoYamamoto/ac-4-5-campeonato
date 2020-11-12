from flask import Blueprint, render_template
from dados import PARTIDAS
from dados import EQUIPES

website_bp = Blueprint(
    'website',
    __name__,
    template_folder = 'templates'
)


@website_bp.route('/')
def home():
    for partida in PARTIDAS:

        if partida.gols_casa > partida.gols_visita:
            partida.equipe_casa.pontuacao += 3
            partida.equipe_casa.vitoria += 1
            partida.equipe_visita.derrota += 1
        elif partida.gols_casa < partida.gols_visita:
            partida.equipe_visita.pontuacao += 3
            partida.equipe_visita.vitoria += 1
            partida.equipe_casa.derrota += 1
        else:
            partida.equipe_casa.pontuacao += 1
            partida.equipe_visita.pontuacao += 1
            partida.equipe_casa.empate += 1
            partida.equipe_visita.empate += 1
    PAL = {
        "NOME": EQUIPES['PALMEIRAS'].nome,
        "VITORIAS": EQUIPES['PALMEIRAS'].vitoria,
        "DERROTAS": EQUIPES['PALMEIRAS'].derrota,
        "EMPATES": EQUIPES['PALMEIRAS'].empate,
        "PONTOS": EQUIPES['PALMEIRAS'].pontuacao,
    }
    SPT = {
        "NOME": EQUIPES['SPORT CLUB'].nome,
        "VITORIAS": EQUIPES['SPORT CLUB'].vitoria,
        "DERROTAS": EQUIPES['SPORT CLUB'].derrota,
        "EMPATES": EQUIPES['SPORT CLUB'].empate,
        "PONTOS": EQUIPES['SPORT CLUB'].pontuacao,
    }
    COR = {
        "NOME": EQUIPES['CORINTHIANS'].nome,
        "VITORIAS": EQUIPES['CORINTHIANS'].vitoria,
        "DERROTAS": EQUIPES['CORINTHIANS'].derrota,
        "EMPATES": EQUIPES['CORINTHIANS'].empate,
        "PONTOS": EQUIPES['CORINTHIANS'].pontuacao,
    }
    VAS = {
        "NOME": EQUIPES['VASCO'].nome,
        "VITORIAS": EQUIPES['VASCO'].vitoria,
        "DERROTAS": EQUIPES['VASCO'].derrota,
        "EMPATES": EQUIPES['VASCO'].empate,
        "PONTOS": EQUIPES['VASCO'].pontuacao,
    }
    SAO = {
        "NOME": EQUIPES['SÃO PAULO'].nome,
        "VITORIAS": EQUIPES['SÃO PAULO'].vitoria,
        "DERROTAS": EQUIPES['SÃO PAULO'].derrota,
        "EMPATES": EQUIPES['SÃO PAULO'].empate,
        "PONTOS": EQUIPES['SÃO PAULO'].pontuacao,
    }
    return render_template(
        'home.html',
        SAO=SAO,
        PAL=PAL,
        VAS=VAS,
        COR=COR,
        SPT=SPT
        )


@website_bp.route('/entrar')
def entrar():
    return render_template('entrar.html')


@website_bp.route('/detalhes')
def detalhes():
    return render_template('detalhes.html')