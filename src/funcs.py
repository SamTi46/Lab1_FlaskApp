import os
import cv2
import matplotlib.pyplot as plt
import numpy as np


# Функция обработки изображения.
def processing_image(filename_image):
    image = cv2.imread(filename_image, cv2.IMREAD_COLOR)

    height, width, _ = image.shape

    half_width = width // 2
    half_height = height // 2

    image_top_left = image[:half_height, :half_width]
    image_top_right = image[:half_height, half_width:]
    image_bottom_left = image[half_height:, :half_width]
    image_bottom_right = image[half_height:, half_width:]

    filename, file_extension = os.path.splitext(filename_image)
    filename_image_top_left = filename + '_top_left' + file_extension
    filename_image_top_right = filename + '_top_right' + file_extension
    filename_image_bottom_left = filename + '_bottom_left' + file_extension
    filename_image_bottom_right = filename + '_bottom_right' + file_extension

    cv2.imwrite(filename_image_top_left, image_top_left)
    cv2.imwrite(filename_image_top_right, image_top_right)
    cv2.imwrite(filename_image_bottom_left, image_bottom_left)
    cv2.imwrite(filename_image_bottom_right, image_bottom_right)

    return filename_image_top_left, filename_image_top_right, filename_image_bottom_left, filename_image_bottom_right


# Функция построения графика распределения цветов.
def creation_plot(filename_image):
    # Чтение изображения.
    image = cv2.imread(filename_image, cv2.IMREAD_COLOR)

    # Разбиение имени файла.
    filename, file_extension = os.path.splitext(filename_image)
    filename_plot = filename_image + '_plot' + file_extension

    image_lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

    y, x, z = image_lab.shape
    flat_lab = np.reshape(image_lab, [y * x, z])

    colors = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    colors = np.reshape(colors, [y * x, z]) / 255.

    # Построение графика распределения цветов.
    figure = plt.figure()
    ax = figure.add_subplot(111, projection='3d')
    ax.scatter(xs=flat_lab[:, 2], ys=flat_lab[:, 1], zs=flat_lab[:, 0], s=10, c=colors, lw=0)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    figure.savefig(filename_plot)

    return filename_plot
