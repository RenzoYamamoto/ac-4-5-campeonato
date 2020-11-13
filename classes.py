class Usuario(object):
    __dados = []

    def __init__(self, email='', senha=''):
        self.email = email
        self.senha = senha

    def __str__(self):
        return f'{self.email}'

    @classmethod
    def criar(cls, email, senha):
        usuario = cls(email, senha,)
                    
        Usuario.__dados.append(usuario)

    @classmethod
    def autenticar(cls, email, senha):
        usuario = Usuario.obter(email)
        if usuario and usuario.senha == senha:
            return usuario

    @classmethod
    def obter(cls, email):
        for u in Usuario.__dados:
            if u.email == email:
                return u


class Equipe(object):
    __dados = []

    def __init__(self, nome='', sigla='', local=''):
        self.nome = nome
        self.sigla = sigla
        self.local = local
        self.pontuacao = 0
        self.vitoria = 0
        self.empate = 0
        self.derrota = 0

    def __str__(self):
        return f'{self.nome} ({self.sigla})'
    
    @classmethod
    def criar(cls, nome, sigla, local):
        equipe = cls(nome, sigla, local)
                    
        Equipe.__dados.append(equipe)
    
    @classmethod
    def obter(cls, sigla):
        for e in Equipe.__dados:
            if e.sigla.lower() == sigla.lower():
                return e
    
    @classmethod
    def listar(cls):
        return Equipe.__dados


class Partida(object):
    __dados = []

    def __init__(self, equipe_casa, equipe_visita, gols_casa, gols_visita):
        self.equipe_casa = equipe_casa
        self.equipe_visita = equipe_visita
        self.gols_casa = gols_casa
        self.gols_visita = gols_visita

    def __str__(self):
        return f'{self.equipe_casa.nome} ({self.gols_casa}) - {self.equipe_visita.nome} ({self.gols_visita})'
    
    @classmethod
    def criar(cls, equipe_casa, equipe_visita, gols_casa, gols_visita):
        partida = cls(equipe_casa, equipe_visita, gols_casa, gols_visita)
                    
        Partida.__dados.append(partida)

    @classmethod
    def listarPorTime(cls, sigla):
        time = []
        for p in Partida.__dados:
            if p.equipe_casa.sigla == sigla or p.equipe_visita.sigla == sigla:
                time.append(p)
        return time
        
