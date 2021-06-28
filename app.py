import connexion
from ma import ma
from db import db

#Create the application instance
connex_app = connexion.App("__name__",specification_dir='./')
#read the swagger to configure the endpoints
connex_app.add_api('swagger.yml')

app = connex_app.app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True


@app.before_first_request
def create_tables():
    db.create_all()


if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    app.run(port=5000, debug=True)