import os

from flask import Flask
from flask import render_template
from werkzeug.utils import secure_filename

from ImageForm import ImageForm
from funcs import processing_image, creation_plot

app = Flask(__name__)

# Используем CSRF-токен.
SECRET_KEY = 'secret'
app.config['SECRET_KEY'] = SECRET_KEY


# Декоратор для вывода страницы по умолчанию (главной страницы).
@app.route("/")
def index():
    return render_template('index.html')


# Декоратор для вывода страницы загрузки изображения.
@app.route('/run', methods=['GET', 'POST'])
def run_app():
    form = ImageForm()
    if form.validate_on_submit():
        filename_image = os.path.join(r'./static/images',secure_filename(form.image.data.filename))

        form.image.data.save(filename_image)

        filename_image_top_left, filename_image_top_right, filename_image_bottom_left, filename_image_bottom_right = (processing_image(filename_image))

        filename_image_plot = creation_plot(filename_image)
        filename_image_top_left_plot = creation_plot(filename_image_top_left)
        filename_image_top_right_plot = creation_plot(filename_image_top_right)
        filename_image_bottom_left_plot = creation_plot(filename_image_bottom_left)
        filename_image_bottom_right_plot = creation_plot(filename_image_bottom_right)

        return render_template('result.html',
                               filename_image=filename_image,
                               filename_image_top_left=filename_image_top_left,
                               filename_image_top_right=filename_image_top_right,
                               filename_image_bottom_left=filename_image_bottom_left,
                               filename_image_bottom_right=filename_image_bottom_right,
                               filename_image_plot=filename_image_plot,
                               filename_image_top_left_plot=filename_image_top_left_plot,
                               filename_image_top_right_plot=filename_image_top_right_plot,
                               filename_image_bottom_left_plot=filename_image_bottom_left_plot,
                               filename_image_bottom_right_plot=filename_image_bottom_right_plot
                               )
    else:
        return render_template('form.html',
                               form=form,
                               result='Загрузите файл-изображение.'
                               )


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=False)
