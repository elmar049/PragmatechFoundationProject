from flask_login.mixins import UserMixin
from run import db

class Services(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_img=db.Column(db.String(50))
    service_title=db.Column(db.String(50))
    service_content=db.Column(db.String(60))


class Products(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    product_name = db.Column(db.String(150))
    product_img = db.Column(db.String(150))



class Emails(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    mailname=db.Column(db.String(150))
    mailsurname = db.Column(db.String(150))
    mailemail = db.Column(db.String(150))
    mailnumber=db.Column(db.String(150))
    mailtext=db.Column(db.Text)


# Login
class Login(UserMixin ,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    admin_username = db.Column(db.String(50))
    admin_password = db.Column(db.String(50))
    log_bool = db.Column(db.Boolean)

