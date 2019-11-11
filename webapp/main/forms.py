from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField, DateField, TimeField
from wtforms.validators import DataRequired, EqualTo

class MainForm(FlaskForm):
        lastname = StringField('Фамилия', validators=[DataRequired()], render_kw={"class":"form-control"})
        firstname = StringField('Имя', validators=[DataRequired()], render_kw={"class":"form-control"})
        middlename = StringField('Отчество', render_kw={"class":"form-control"})
        datebirth = DateField('Дата', validators=[DataRequired()], render_kw={"class":"form-control", "type":"date", "min":"1900-01-01", "max":"2100-12-31"})
        timebirth = TimeField('Время', validators=[DataRequired()], render_kw={"class":"form-control", "type":"time", "class":"form-control", "min":"00:00", "max":"23:59"})
        submit = SubmitField('Добавить расчет', render_kw={"class":"btn btn-primary"})
