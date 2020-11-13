from flask import Blueprint, flash, redirect, render_template, request, session
from classes import Equipe, Usuario, Partida

website_bp = Blueprint(
    'website',
    __name__,
    template_folder = 'templates'
)


@website_bp.route('/')
def home():    
    return render_template(
        'home.html',
        equipes=Equipe.listar()
        )

@website_bp.route('/detalhes/<equipe>')
def detalhes(equipe):
    return render_template(
        'detalhes.html', 
        partidas=Partida.listarPorTime(equipe), 
        nome=Equipe.obter(equipe).nome)

@website_bp.route('/entrar', methods=['GET', 'POST'])
def entrar():
    if request.method == 'POST':
        form = request.form
        usuario = Usuario.autenticar(
            form.get('email'),
            form.get('senha')
        )
        if usuario:
            
            return redirect('/admin')
        else:
            flash('Email ou senha incorretos!')
            return redirect('/entrar')
    else:
        return render_template('entrar.html')