from OpenGL.GL import *
import numpy as np

from collections import namedtuple
from view.utilities import *


def init_gl_widget(gl_widget, model):
    gl_widget.initializeGL()
    gl_widget.paintGL = lambda: paint_gl(model, gl_widget)
    gl_widget.initializeGL = lambda: glClearColor(0.8, 0.8, 0.8, 1)
    gl_widget.resizeGL = lambda w, h: glViewport(*gl_widget.geometry().getRect())


def paint_gl(model, gl_widget):
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    if model.iter_num > -1:
        glClear(GL_COLOR_BUFFER_BIT)
        draw_levi(model.iter_num)


Triangle = namedtuple('Triangle', ['a', 'b', 'c'])
Point = namedtuple('Point', ['y', 'x'])
Color = namedtuple('Color', ['r', 'g', 'b'])


def draw_triangle(triangle, color):
    glBegin(GL_TRIANGLES)
    glColor(*color)
    glVertex2f(*triangle.a)
    glVertex2f(*triangle.b)
    glVertex2f(*triangle.c)
    glEnd()


def rotate2d_points(prop, angle_in_degrees, points):
    angle_in_radians = np.radians(angle_in_degrees)

    rotation_matrix = np.array([[np.cos(angle_in_radians), -np.sin(angle_in_radians)],
                      [np.sin(angle_in_radians), np.cos(angle_in_radians)]])

    new_points = []
    for point in points:
        vector = np.array([point.x - prop.x, point.y - prop.y])
        rotated = rotation_matrix @ vector
        new_points += [Point(rotated[0] + prop.x, rotated[1] + prop.y)]

    return new_points


def scale2d_points(prop, scale_factor, points):
    scale_matrix = np.array([[scale_factor, 0],
                             [0, scale_factor]])

    new_points = []
    for point in points:
        vector = np.array([point.x - prop.x, point.y - prop.y])
        rotated = scale_matrix @ vector
        new_points += [Point(rotated[0] + prop.x, rotated[1] + prop.y)]

    return new_points


LEVI_SCALE_FACTOR = np.sqrt(2) / 2


def draw_levi(n):
    gray_triangles = []
    black_triangles = [Triangle(Point(-0.4, 0.0), Point(0.0, 0.4), Point(0.4, 0.0))]

    for i in range(n):
        gray_triangles = black_triangles
        black_triangles = []

        for gray_triangle in gray_triangles:
            left_triangle = Triangle(*rotate2d_points(gray_triangle[0], -45, gray_triangle[:]))
            left_triangle = Triangle(*scale2d_points(left_triangle[0], LEVI_SCALE_FACTOR, left_triangle[:]))

            right_triangle = Triangle(*rotate2d_points(gray_triangle[2], 45, gray_triangle[:]))
            right_triangle = Triangle(*scale2d_points(right_triangle[2], LEVI_SCALE_FACTOR, right_triangle[:]))

            black_triangles += [left_triangle, right_triangle]

    for triangle in gray_triangles:
        draw_triangle(triangle, Color(1, 0, 0))

    for triangle in black_triangles:
        draw_triangle(triangle, Color(0, 0, 1))
