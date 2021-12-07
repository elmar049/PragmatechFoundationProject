from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__,template_folder='view')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///elmarin.db'
db=SQLAlchemy(app)
from modules.module import *

from controllers.admin.route import *
from controllers.app.route import *






  
if __name__=='__main__':
    app.run(debug=True)