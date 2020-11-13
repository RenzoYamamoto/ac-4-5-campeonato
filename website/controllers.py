from flask import Blueprint, render_template
from classes import Equipe

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