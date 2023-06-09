from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, \
    TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, \
    Length
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    fullname_me = StringField('Full Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Request Password Reset')


class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    fullname_me = TextAreaField('Full Name', validators=[Length(min=0, max=140)])
    email_me = TextAreaField('Email', validators=[Length(min=0, max=140)])
    phonenumber_me = TextAreaField('Phone Number', validators=[Length(min=0, max=140)])
    city_me = TextAreaField('City', validators=[Length(min=0, max=140)])
    jobtitle_me = TextAreaField('Job Title', validators=[Length(min=0, max=140)])
    company_me = TextAreaField('Company', validators=[Length(min=0, max=140)])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')
    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.')


class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')


class PostForm(FlaskForm):
    post = TextAreaField('Say something', validators=[DataRequired()])
    submit = SubmitField('Submit')

class CreateEvent(FlaskForm):
    eventname = StringField('Event Name', validators=[DataRequired()])
    eventadress = TextAreaField('Event Adress', validators=[Length(min=0, max=140)])
    eventdate = TextAreaField('Event Date', validators=[Length(min=0, max=140)])
    eventtime = TextAreaField('Event Time', validators=[Length(min=0, max=140)])
    eventhost = TextAreaField('Event Host', validators=[Length(min=0, max=140)])
    eventcontact = TextAreaField('Event Contact', validators=[Length(min=0, max=140)])
    eventdetails = TextAreaField('Event Details', validators=[Length(min=0, max=140)])

    def __repr__(self):
        return f'<Event {self.eventname}>'
