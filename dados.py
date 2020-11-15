from database.classes import Equipe, Partida, Usuario

EQUIPES = {
    'PALMEIRAS': Equipe('PALMEIRAS', 'PAL', 'São Paulo-SP'),
    'SPORT CLUB': Equipe('SPORT CLUB', 'SPT', 'Recife - PE'),
    'SANTOS': Equipe('SANTOS', 'SAT', 'São Paulo-SP'),
    'CORINTHIANS': Equipe('CORINTHIANS', 'COR', 'São Paulo-SP'),
    'VASCO': Equipe('VASCO', 'VAS', 'Rio de Janeiro-RJ')
}

PARTIDAS = [
    Partida(EQUIPES['PALMEIRAS'], EQUIPES['SPORT CLUB'], 1, 0),
    Partida(EQUIPES['SPORT CLUB'], EQUIPES['PALMEIRAS'], 2, 5),
    Partida(EQUIPES['PALMEIRAS'], EQUIPES['SANTOS'], 1, 3),
    Partida(EQUIPES['SANTOS'], EQUIPES['PALMEIRAS'], 5, 3),
    Partida(EQUIPES['PALMEIRAS'], EQUIPES['CORINTHIANS'], 5, 2),
    Partida(EQUIPES['CORINTHIANS'], EQUIPES['PALMEIRAS'], 5, 3),
    Partida(EQUIPES['PALMEIRAS'], EQUIPES['VASCO'], 3, 5),
    Partida(EQUIPES['VASCO'], EQUIPES['PALMEIRAS'], 3, 1),
    Partida(EQUIPES['SPORT CLUB'], EQUIPES['SANTOS'], 3, 2),
    Partida(EQUIPES['SANTOS'], EQUIPES['SPORT CLUB'], 4, 3),
    Partida(EQUIPES['SPORT CLUB'], EQUIPES['CORINTHIANS'], 4, 1),
    Partida(EQUIPES['CORINTHIANS'], EQUIPES['SPORT CLUB'], 2, 3),
    Partida(EQUIPES['SPORT CLUB'], EQUIPES['VASCO'], 0, 1),
    Partida(EQUIPES['VASCO'], EQUIPES['SPORT CLUB'], 0, 0),
    Partida(EQUIPES['SANTOS'], EQUIPES['CORINTHIANS'], 1, 0),
    Partida(EQUIPES['CORINTHIANS'], EQUIPES['SANTOS'], 2, 1),
    Partida(EQUIPES['SANTOS'], EQUIPES['VASCO'], 3, 1),
    Partida(EQUIPES['VASCO'], EQUIPES['SANTOS'], 0, 3),
    Partida(EQUIPES['CORINTHIANS'], EQUIPES['VASCO'], 2, 2),
    Partida(EQUIPES['VASCO'], EQUIPES['CORINTHIANS'], 1, 5)
]

USUARIOS = [
    Usuario('admin@admin.com', 'admin123*')
]