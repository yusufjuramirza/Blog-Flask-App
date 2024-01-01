from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Length
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# TODO: Create a RegisterForm to register new users
class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(message='Email is required')])
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(message='Password is required'),
            Length(max=12, message="Too long"), Length(min=6, message='Too short')
        ]
    )
    name = StringField('Name', validators=[DataRequired(message='Name is required'), Length(min=2, message='Too short name')])
    register = SubmitField('Sign me up!')


# TODO: Create a LoginForm to login existing users
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(message='Email is required')])
    password = PasswordField('Password', validators=[DataRequired(message='Password is required')])
    login = SubmitField('Let me in!')


# TODO: Create a CommentForm so users can leave comments below posts
class CommentForm(FlaskForm):
    comment_text = CKEditorField('Comment', validators=[DataRequired()])
    comment = SubmitField('Submit Comment')
