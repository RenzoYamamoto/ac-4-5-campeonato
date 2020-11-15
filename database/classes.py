class Usuario(object):
    
    __dados = []

    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

    def __str__(self):
        return self.email

    @classmethod
    def criar(cls, email, senha):
        usuario = cls(email, senha,)
                    
        Usuario.__dados.append(usuario)

    @classmethod
    def autenticar(cls, email, senha):
        email = Usuario.obter(email)
        if email and email.senha == senha:
            return email

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
    
        erros = Equipe.__validar(equipe, True)
        if len(erros) == 0:
            Equipe.__dados.append(equipe)

        return erros
    
    @classmethod
    def obter(cls, sigla):
        for e in Equipe.__dados:
            if e.sigla.lower() == sigla.lower():
                return e
    
    @classmethod
    def listar(cls):
        return Equipe.__dados

    @classmethod
    def alterar(cls, siglaAntiga, nome, sigla, local):
        equipe = cls(nome, sigla, local)
        erros = Equipe.__validar(equipe, True)

        if len(erros) == 0:
            original = Equipe.obter(siglaAntiga)
            original.nome = equipe.nome
            original.sigla = equipe.sigla
            original.local = equipe.local

        return erros

    @classmethod
    def __validar(cls, equipe, alteracao=False):
        erros = []
        if not equipe.nome:
            erros.append('Nome da equipe é obrigatório!')

        if not equipe.sigla:
            erros.append('Sigla da equipe é obrigatória!')
        elif not alteracao and Equipe.obter(equipe.sigla):
            erros.append(f'A sigla {equipe.sigla} já está sendo utilizada!')

        if not equipe.local:
            erros.append('Local da equipe é obrigatório!')

        return erros

    @classmethod
    def remover(cls, sigla):
        equipe = Equipe.obter(sigla)
        if equipe:
            Equipe.__dados.remove(equipe)


class Partida(object):
    __dados = []
    __idPartida = 0

    def __init__(self, equipe_casa, equipe_visita, gols_casa, gols_visita):
        self.equipe_casa = equipe_casa
        self.equipe_visita = equipe_visita
        self.gols_casa = gols_casa
        self.gols_visita = gols_visita
        self.idPartida = Partida.__idPartida
        Partida.__idPartida += 1   

    def __str__(self):
        return f'{self.equipe_casa.nome} ({self.gols_casa}) - {self.equipe_visita.nome} ({self.gols_visita})'
    
    @classmethod
    def criar(cls, equipe_casa, equipe_visita, gols_casa, gols_visita):
        partida = cls(equipe_casa, equipe_visita, gols_casa, gols_visita)
    
        erros = Partida.__validar(partida, True)
        if len(erros) == 0:
            Partida.__dados.append(partida)

        return erros

    @classmethod
    def listarPorTime(cls, sigla):
        time = []
        for p in Partida.__dados:
            if p.equipe_casa.sigla == sigla or p.equipe_visita.sigla == sigla:
                time.append(p)
        return time

    @classmethod
    def listar(cls):
        return Partida.__dados

    @classmethod
    def obter(cls, id):
        for p in Partida.__dados:
            if p.idPartida == int(id):
                return p

    @classmethod
    def alterar(cls, idAntigo, timeCasa, golCasa, timeVisita, golVisita):
        partida = cls(Equipe.obter(timeCasa), Equipe.obter(timeVisita), golCasa, golVisita)
        erros = Partida.__validar(partida, True)

        if len(erros) == 0:
            original = Partida.obter(idAntigo)
            original.equipe_casa = partida.equipe_casa
            original.equipe_visita = partida.equipe_visita
            original.gols_casa = partida.gols_casa
            original.gols_visita = partida.gols_visita

        return erros

    @classmethod
    def __validar(cls, partida, alteracao=False):
        erros = []
        if not partida.equipe_casa:
            erros.append('Equipe casa é obrigatório!')

        if not partida.equipe_visita:
            erros.append('Equipe visita é obrigatório!')

        if not partida.gols_casa:
            erros.append('Gols visita é obrigatório!')

        if not partida.gols_visita:
            erros.append('Gols visita é obrigatório!')

        return erros

    @classmethod
    def remover(cls, sigla):
        partida = Partida.obter(sigla)
        if partida:
            Partida.__dados.remove(partida)
        
