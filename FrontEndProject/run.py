from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate


app=Flask(__name__)

UPLOAD_FOLDER = 'static/uploads/'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///final.db'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app.routes import *
from admin.routes import *




if __name__=='__main__':

    app.run(debug=True)