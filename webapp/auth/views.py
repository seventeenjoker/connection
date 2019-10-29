from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user

from webapp.db import db
from webapp.auth.forms import LoginForm, RegistrationForm
from webapp.main.forms import MainForm
from webapp.auth.models import User

blueprint = Blueprint('auth', __name__, url_prefix='/auth')

@blueprint.route('/process-login', methods=['POST'])
def process_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(login=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            # flash('Вы вошли на сайт')
            if user.is_admin:
                return redirect(url_for('admin.admin'))
            else:
                return redirect(url_for('main.main'))

    flash('Неправильное имя пользователя или пароль')
    return redirect(url_for('auth.login'))

@blueprint.route('/')
def login():
    if current_user.is_authenticated:
        title = 'Добро пожаловать в личный кабинет.'
        main_form = MainForm()
        return render_template('auth/index.html', page_title=title, form=main_form)
    title = 'Авторизация'
    login_form = LoginForm()
    return render_template('auth/login.html', page_title=title, form=login_form)

@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@blueprint.route('/register')
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.main'))
    title = 'Регистрация'
    form = RegistrationForm()
    return render_template('auth/registration.html', page_title=title, form=form)

@blueprint.route('/process-reg', methods=['POST'])
def process_reg():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(login=form.username.data)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Вы успешно зарегистрировались!')
        return redirect(url_for('auth.login'))
    flash('Исправьте пожалуйста ошибки в форме.')
    return redirect(url_for('auth.register'))
