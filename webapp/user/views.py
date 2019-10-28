from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user

from webapp.db import db
from webapp.user.forms import LoginForm, RegistrationForm, IndexForm
from webapp.user.models import User

blueprint = Blueprint('user', __name__, url_prefix='/users')

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
                return redirect(url_for('index.index'))

    flash('Неправильное имя пользователя или пароль')
    return redirect(url_for('user.login'))

@blueprint.route('/')
def login():
    if current_user.is_authenticated:
        #return redirect(url_for('index.index'))
        title = 'Добро пожалловать в личный кабинет.'
        index_form = IndexForm()
        return render_template('user/index.html', page_title=title, form=index_form)
    title = 'Авторизация'
    login_form = LoginForm()
    return render_template('user/login.html', page_title=title, form=login_form)

@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('user.login'))

@blueprint.route('/register')
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index.index'))
    title = 'Регистрация'
    form = RegistrationForm()
    return render_template('user/registration.html', page_title=title, form=form)

@blueprint.route('/process-reg', methods=['POST'])
def process_reg():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(login=form.username.data)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Вы успешно зарегистрировались!')
        return redirect(url_for('user.login'))
    flash('Исправьте пожалуйста ошибки в форме.')
    return redirect(url_for('user.register'))
