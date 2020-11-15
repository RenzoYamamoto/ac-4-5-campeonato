from flask import Blueprint, jsonify, redirect, request, render_template, session
from dados import Equipe, Partida
from admin.decorators import login_required


admin_bp = Blueprint(
    'admin',
    __name__,
    template_folder = 'templates'
)


@admin_bp.route('/')
@login_required
def home():    
    return render_template(
        'cadastro.html'
    )

@admin_bp.route('/equipes')
@login_required
def equipes():
    return render_template('Equipe/equipes.html', equipes=Equipe.listar())

@admin_bp.route('/partidas')
@login_required
def partidas():
    return render_template('Partida/partidas.html', partidas=Partida.listar())

@admin_bp.route('/detalhes/<equipe>')
@login_required
def detalhes():
    return render_template('detalhes.html')

@admin_bp.route('/equipes/criar', methods=['GET', 'POST'])
@login_required
def equipes_criar():
    equipe = {}
    erros = []
    
    if request.method == "POST":
        equipe = request.form
        erros = Equipe.criar(
            equipe.get('nome'),
            equipe.get('sigla'),
            equipe.get('local')
        )

        if len(erros) == 0:
            return redirect('/admin/equipes')

    return render_template('Equipe/nova_equipe.html', erros=erros)

@admin_bp.route('/partidas/criar', methods=['GET', 'POST'])
@login_required
def partidas_criar():
    partida = {}
    erros = []
    
    if request.method == "POST":
        alteracao = request.form
        erros = Partida.criar(Equipe.obter(alteracao.get("timeCasa")), 
                Equipe.obter(alteracao.get("timeVisita")),
                alteracao.get("golsCasa"),                 
                alteracao.get("golsVisita"))

        if len(erros) == 0:
            return redirect('/admin/partidas')

    return render_template('Partida/nova_partida.html', erros=erros, equipes=Equipe.listar())

@admin_bp.route('/equipes/alterar/<equipe>', methods=['GET', 'POST'])
@login_required
def equipes_alterar(equipe):
    erros = []

    if request.method == "POST":
        alteracao = request.form
        erros = Equipe.alterar(equipe, 
                alteracao.get("nome"), 
                alteracao.get("sigla"), 
                alteracao.get("local"))

        if len(erros) == 0:
            return redirect('/admin/equipes')

    return render_template(
        'Equipe/alterar_equipe.html',
        equipe=Equipe.obter(equipe),
        erros=erros
    )

@admin_bp.route('/partidas/alterar/<partida>', methods=['GET', 'POST'])
@login_required
def partidas_alterar(partida):
    erros = []

    if request.method == "POST":
        alteracao = request.form
        erros = Partida.alterar(partida, 
                alteracao.get("timeCasa"), 
                alteracao.get("golCasa"), 
                alteracao.get("timeVisita"),
                alteracao.get("golVisita"))

        if len(erros) == 0:
            return redirect('/admin/partidas')

    return render_template(
        'Partida/alterar_partida.html',
        partida=Partida.obter(partida),
        erros=erros
    )

@admin_bp.route('/equipes/deletar/<equipe>', methods=['GET', 'POST'])
@login_required
def equipes_remover(equipe):
    Equipe.remover(equipe)
    return redirect('/admin/equipes')

@admin_bp.route('/partidas/deletar/<partida>', methods=['GET', 'POST'])
@login_required
def partidas_remover(partida):
    Partida.remover(partida)
    return redirect('/admin/partidas')