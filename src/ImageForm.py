from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import FileField


class ImageForm(FlaskForm):
    image = FileField('Исходное изображение: ',
                      validators=[FileRequired(),
                                  FileAllowed(['jpg', 'jpeg', 'png'],
                                              'Только файлы изображений!')])
