from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from app.models import User

class RegisterForm(FlaskForm):

    username = StringField('用户名', validators=[DataRequired(), Length(min=6, max=20)])
    email=StringField('邮箱', validators=[DataRequired(), Email()])
    password = PasswordField('密码', validators=[DataRequired(), Length(min=6, max=20)])
    confirm = PasswordField('确认密码',validators=[DataRequired(), EqualTo('password')])

    #recaptcha = RecaptchaField()
    submit = SubmitField('注册')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('用户名已被使用，请您使用其他用户名！')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('邮箱已被使用，请您使用其他邮箱！')

class LoginForm(FlaskForm):

    username = StringField('用户名', validators=[DataRequired(), Length(min=6, max=20)])
    password = PasswordField('密码', validators=[DataRequired(), Length(min=6, max=20)])
    remember = BooleanField('记住密码')
    submit = SubmitField('登录')

class PasswordResetRequestForm(FlaskForm):

    email = StringField('邮箱', validators=[DataRequired(), Email()])
    submit = SubmitField('发送')
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if not user:
            raise ValidationError('邮箱不存在！')

class GetDataForm(FlaskForm):

    search = StringField('搜索内容', validators=[DataRequired()])
    filename=StringField('文件名', validators=[DataRequired()])
    submit = SubmitField('提交')

class CleanForm(FlaskForm):

    clean_filename = StringField('文件名', validators=[DataRequired()])
    submit = SubmitField('提交')

class CloudWordForm(FlaskForm):

    cloudwordname = StringField('文件名', validators=[DataRequired()])
    submit = SubmitField('提交')

class Td_IdfForm(FlaskForm):

    td_idfname = StringField('文件名', validators=[DataRequired()])
    submit = SubmitField('提交')

class MoodForm(FlaskForm):

    moodname = StringField('文件名', validators=[DataRequired()])
    submit = SubmitField('提交')

class K_meansForm(FlaskForm):

    filename = StringField('文件名', validators=[DataRequired()])
    k=StringField('k值', validators=[DataRequired()])
    submit = SubmitField('提交')

class ResetPasswordForm(FlaskForm):

    password = PasswordField('密码', validators=[DataRequired(), Length(min=6, max=20)])
    confirm = PasswordField('确认密码',validators=[DataRequired(), EqualTo('password')])


    submit = SubmitField('修改密码')