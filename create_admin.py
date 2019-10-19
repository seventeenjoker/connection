from getpass import getpass
import sys

from webapp import create_app
from webapp.model import User, db

app = create_app()

with app.app_context():
    login = input('Введите логин:')

    if User.query.filter(User.login == login).count():
        print('Такой пользователь уже есть.')
        sys.exit(0)
    
    password = getpass('Введите пароль:')
    password2 = getpass('Повторите пароль')

    if not password == password2:
        sys.exit(0)

    new_user = User(login=login, is_admin=True)
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()
    print(f"User with id {new_user.id} added.")