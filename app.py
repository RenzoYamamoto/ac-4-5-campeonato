import os
from flask import Flask
from website.controllers import website_bp
from admin.controllers import admin_bp
from database.carregador import carregar_dados


app = Flask(__name__)
app.register_blueprint(website_bp)
app.register_blueprint(admin_bp, url_prefix='/admin')

carregar_dados(
    os.path.join(
        os.path.dirname(
            os.path.abspath(__file__)
        ),
        'database'
    )
)
if __name__ == "__main__":
    app.run(
        debug=True
    )
