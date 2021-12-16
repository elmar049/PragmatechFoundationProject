### APP - ROUTES

from flask import Flask, render_template, redirect,request
from run import app
from models import *


@app.route("/")
def portfolio():
    from models import Products
    from models import Services
    from models import Emails

    mails=Emails.query.all()
    products=Products.query.all()
    services = Services.query.all()
    return render_template("app/index.html", services=services, products=products, mails=mails)

