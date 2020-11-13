from flask import Blueprint, flash, redirect, render_template, request, session
from classes import Equipe, Usuario

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


@website_bp.route('/detalhes')
def detalhes():
    return render_template('detalhes.html')

@website_bp.route('/autenticar', methods=['GET', 'POST'])
def autenticar():
    form = request.form
    usuario = Usuario.autenticar(
        form.get('usuario'),
        form.get('senha')
    )
    if usuario:
        session['usuario'] = usuario.nome
        session['data'] = datetime.now().__str__()
        return redirect('/admin')
    else:
        flash('Usuário ou senha incorretos!')
        return redirect('/entrar')