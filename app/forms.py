from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, validators

class LoginForm(Form):
    openid = StringField('openid', validators=[validators.DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
