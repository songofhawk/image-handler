from flask_login import LoginManager

from app import app
from app.models import User

# session(app)
login = LoginManager(app)
login.login_view = 'login'


@login.user_loader
def load_user(user_id):
    return User.get(user_id)
