from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField, FloatField
from flask_wtf.file import FileField, FileRequired, FileAllowed, FileSize

class ProductForm(FlaskForm):
    name = StringField("Enter Book Name")
    author = StringField("Enter Author Name")
    price = FloatField("Enter Price")
    image = FileField("Upload Image", validators=[FileSize(1024 * 1024),
                                                  FileAllowed(["jpg", "png", "jpeg"])])
    submit = SubmitField("Create Product")