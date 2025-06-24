from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField, DateField, RadioField, SelectField, EmailField, FloatField
from wtforms.validators import DataRequired, length, equal_to, ValidationError
from flask_wtf.file import FileField, FileRequired, FileAllowed, FileSize
from string import ascii_uppercase, ascii_lowercase, digits, punctuation


class LoginForm(FlaskForm):
    username = StringField("Enter Username...", validators=[DataRequired()])
    password = PasswordField("Enter Password...", validators=[DataRequired()])
    login = SubmitField("Log In")


class RegisterForm(FlaskForm):
    username = StringField("Enter Username...",
                           validators=[DataRequired()])

    email = EmailField("Enter Email...",
                       validators=[DataRequired()])

    password = PasswordField("Enter Password...",
                             validators=[DataRequired(), length(min=8, max=20)])

    repeat_password = PasswordField("Confirm Password...",
                                    validators=[DataRequired("განმეორებითი პაროლის ველი სავალდებულოა"),
                                                equal_to("password",
                                                         message="პაროლი და განმეორებითი პაროლი არ ემთხვევა")])

    birthday = DateField("Enter Birthday...",
                         validators=[DataRequired()])

    gender = RadioField("Choose Gender", choices=[(0, "Male"), (1, "Female")],
                        validators=[DataRequired()])

    country = SelectField("Choose Country", choices=["Georgia", "USA", "Spain"],
                          validators=[DataRequired()])

    profile_image = FileField("Upload Profile Image",
                              validators=[FileSize(1024 * 1024),
                                          FileAllowed(["jpg", "jpeg", "png"])])
    submit = SubmitField("Registration")

    def validate_password(self, field):
        contains_uppercase = False
        contains_lowercase = False
        contains_digits = False
        contains_symbols = False

        for char in field.data:
            if char in ascii_uppercase:
                contains_uppercase = True

            if char in ascii_lowercase:
                contains_lowercase = True

            if char in digits:
                contains_digits = True

            if char in punctuation:
                contains_symbols = True

        if not contains_uppercase:
            raise ValidationError("პაროლი უნდა შეიცავდეს დიდ ასოებს")

        if not contains_lowercase:
            raise ValidationError("პაროლი უნდა შეიცავდეს პატარა ასოებს")

        if not contains_digits:
            raise ValidationError("პაროლი უნდა შეიცავდეს ციფრებს")

        if not contains_symbols:
            raise ValidationError("პაროლი უნდა შეიცავდეს სიმბოლოებს")