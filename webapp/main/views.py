import datetime
import time
from collections import Counter
from flask import Blueprint, render_template
from flask_login import current_user, login_required
from webapp.main.forms import MainForm
from webapp.auth.models import Person, User

blueprint = Blueprint('main', __name__, url_prefix='/main')

@blueprint.route('/')
@login_required
def main():
    title = 'Добро пожаловать в личный кабинет.'
    main_form = MainForm()
    return render_template('auth/index.html', page_title=title, form=main_form)

@blueprint.route('/', methods=['POST'])
def process_add_user():
    form = MainForm()
    if form.validate_on_submit():
        # Т.к. на форме дата и время разные поля, надо положить их в одну переменную для корректного применения фильтра
        date_time_form = datetime.strptime(form.datebirth.data + " " + form.timebirth.data)
        person = Person.query.filter_by(last_name=form.lastname.data, first_name=form.firstname.data, \
            datetime_of_birth=date_time_form, user_id=User.id).first()
        if not person:
            # Добавляем такого пользователя в базу
            new_person = Person(first_name=form.firstname.data, last_name=form.lastname.data, datetime_of_birth=date_time_form, \
                user_id=User.id, middle_name=form.middlename.data)
            db.session.add(new_person)
            db.session.commit()
            # Добавляем расчет в таблицу PythagoreanSquare
            person_square = pythagore_calc(date_time_form)

            flash('Вы успешно добавили пользователя!')
            return redirect(url_for('/'))
    flash('Исправьте пожалуйста ошибки при добавлении нового пользователя. Возможно он уже существует.')
    return redirect(url_for('/'))

# расчет квадрата
def pythagore_calc(date_time_birth):
    day = date_time_birth.year
    month = date_time_birth.month
    year = date_time_birth.year
    # 1. Выпишите цифры дня и месяца рождения: 1610. Сложите цифры, получится первое число: 1+6+1+0 = 8.
    # Точно также высчитайте сумму цифр года рождения: 1+9+9+1 = 20. Получили второе число.
    # Рассчитайте сумму двух первых, получившихся в результате расчёта, чисел: 8+20 = 28. Это первое рабочее число.
    summ1 = 0
    for n in str(day): 
        summ1 += int(n)
    for n in str(month):
        summ1 += int(n)
    summ2 = 0
    for n in str(year):
        summ2 += int(n)

    first_work = summ1 + summ2

    # 2. Далее найдите сумму цифр первого рабочего числа: 2+8 = 10. Это второе рабочее число.
    summ3 = 0
    for n in str(first_work):
        summ3 += n
    second_work = summ3

    # 3. Из первого рабочего числа вычитайте умноженную вдвое первую цифру даты рождения: 28-2*1 = 26. Это третье рабочее число.
    third_work = first_work - int(str(day)[:1])

    # 4. И, наконец, сложите цифры третьего рабочего числа: 2+6=8. В итоге получаем четвёртое рабочее число.
    summ4 = 0
    for n in str(third_work):
        summ4 += n
    fourth_work = summ4

    # Joining with empty separator
    numbers = "".join([day, month,year,first_work, second_work, third_work, fourth_work])
    square_calc = Counter.numbers

    return square_calc