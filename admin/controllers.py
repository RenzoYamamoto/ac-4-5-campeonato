from flask import Blueprint, jsonify, redirect, request, render_template
from dados import EQUIPES, PARTIDAS


admin_bp = Blueprint(
    'admin',
    __name__,
    template_folder = 'templates'
)


@admin_bp.route('/')
def home():    
    return render_template(
        'cadastro.html'
    )


@admin_bp.route('/detalhes/<equipe>')
def detalhes():
    return render_template('detalhes.html')


@admin_bp.route('equipes')
def equipes():
    return render_template('equipes.html')


@admin_bp.route('/equipes/criar')
def equipes_criar():
    return 


@admin_bp.route('/equipes/alterar')
def equipes_alterar():
    return 


@admin_bp.route('/equipes/remover')
def equipes_remover():
    return 


@admin_bp.route('/partidas')
def partidas():
    return render_template('partidas.html')


@admin_bp.route('/partidas/criar')
def partidas_criar():
    return 


@admin_bp.route('/partidas/alterar')
def partidas_alterar():
    return 


@admin_bp.route('/partidas/remover')
def partidas_remover():
    return