import time
from collections import Counter
from datetime import datetime
from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required
from webapp.main.forms import MainForm
from webapp.auth.models import Person, PythagoreanSquare, User
from webapp.db import db

blueprint = Blueprint('main', __name__, url_prefix='/main')

@blueprint.route('/')
@login_required
def main():
    title = 'Добро пожаловать в личный кабинет.'
    main_form = MainForm()
    return render_template('auth/index.html', page_title=title, form=main_form)

@blueprint.route('/', methods=['POST'])
def process_add_person():
    form = MainForm()
    if form.validate_on_submit():
        # Т.к. на форме дата и время разные поля, надо положить их в одну переменную для корректного применения фильтра
        date_time_form = datetime.strptime(str(form.datebirth.data) + " " + str(form.timebirth.data), '%Y-%m-%d %H:%M:%S')
        person = Person.query.filter_by(last_name=form.lastname.data, first_name=form.firstname.data, \
            datetime_of_birth=date_time_form, user_id=current_user.id).first()
        if not person:
            # Добавляем такого пользователя в базу
            new_person = Person(first_name=form.firstname.data, last_name=form.lastname.data, datetime_of_birth=date_time_form, \
                user_id=current_user.id, middle_name=form.middlename.data)
            db.session.add(new_person)
            db.session.commit()
            # Добавляем расчет в таблицу PythagoreanSquare
            person_square = pythagore_calc(date_time_form)
            new_square = PythagoreanSquare(person_id=new_person.user_id, first=person_square.get('1', 0), second=person_square.get('2', 0), \
                third=person_square.get('3', 0), fourth=person_square.get('4', 0), fifth=person_square.get('5', 0), sixth=person_square.get('6', 0), \
                seventh=person_square.get('7', 0), eighth=person_square.get('8', 0), ninth=person_square.get('9', 0))
            db.session.add(new_square)
            db.session.commit()
            # flash('Вы успешно добавили пользователя!')
            return redirect(url_for('main.main'))
    # flash('Исправьте пожалуйста ошибки при добавлении нового пользователя. Возможно он уже существует.')
    return redirect(url_for('main.main'))

def pythagore_calc(date_time_birth):
    """ расчет квадрата """
    day = date_time_birth.year
    month = date_time_birth.month
    year = date_time_birth.year
    # 1. Выпишите цифры дня и месяца рождения: 1610. Сложите цифры, получится первое число: 1+6+1+0 = 8.
    # Точно также высчитайте сумму цифр года рождения: 1+9+9+1 = 20. Получили второе число.
    # Рассчитайте сумму двух первых, получившихся в результате расчёта, чисел: 8+20 = 28. Это первое рабочее число.
    
    summ1 = sum(map(lambda x: int(x), list(str(day)) + list(str(month))))
    summ2 = sum(map(lambda x: int(x), list(str(year))))

    first_work = summ1 + summ2

    # 2. Далее найдите сумму цифр первого рабочего числа: 2+8 = 10. Это второе рабочее число.
    second_work = sum(map(lambda x: int(x), list(str(first_work))))

    # 3. Из первого рабочего числа вычитайте умноженную вдвое первую цифру даты рождения: 28-2*1 = 26. Это третье рабочее число.
    third_work = first_work - int(str(day)[:1]*2)

    # 4. И, наконец, сложите цифры третьего рабочего числа: 2+6=8. В итоге получаем четвёртое рабочее число.
    fourth_work = sum(map(lambda x: int(x), list(str(third_work))))

    # Joining with empty separator
    numbers = (str(day) + str(month) + str(year) + str(first_work) + str(second_work) + str(third_work)+ str(fourth_work))
    square_calc = Counter(numbers)

    return square_calc