from logging import debug
from flask import Flask, redirect,request, render_template

app=Flask(__name__)


from routes.admin.route import *
from routes.app.route import *




    



if __name__=='__main__':
    app.run(debug=True) 