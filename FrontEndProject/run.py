from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
from flask_mail import Mail, Message


app=Flask(__name__)


UPLOAD_FOLDER = 'static/uploads/'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///final.db'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587   
app.config['MAIL_USERNAME'] = "sabuhiq0@gmail.com"
app.config['MAIL_PASSWORD'] = "Sabuhi07123"
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)


db = SQLAlchemy(app)

from models import *
migrate = Migrate(app, db)



from app.routes import *
from admin.routes import *





if __name__=='__main__':
    app.run(debug=True)