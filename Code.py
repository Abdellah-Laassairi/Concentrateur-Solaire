
from imgui.integrations.pygame import PygameRenderer
import imgui
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
colors = (
    (1 , 1 , 0) ,
    (2 , 1 , 0) ,
    (0 , 0 , 3) ,
    (0 , 1 , 0) ,
    (1 , 1 , 1) ,
    (0 , 1 , 1) ,
    (0 , 2 , 0) ,
    (0 , 1 , 0) ,
    (0 , 2 , 1) ,
    (1 , 0 , 0) ,
    (2 , 1 , 1) ,
    (0 , 1 , 1) ,
)


def Mirroir():
    verticies = (
        (-2 , -1 , -0.1) ,
        (2 , -1 , -0.1) ,
        (2 , -1 , 0.1) ,
        (-2 , -1 , 0.1) ,

        (2 , 1 , -0.1) ,
        (2 , 1 , 0.1) ,
        (-2 , 1 , 0.1) ,
        (-2 , 1 , -0.1)
    )
    edges = (
        (0 , 1) ,
        (0 , 3) ,
        (0 , 7) ,
        (2 , 1) ,
        (2 , 3) ,
        (2 , 5) ,
        (4 , 1) ,
        (4 , 5) ,
        (4 , 7) ,
        (6 , 7) ,
        (6 , 5) ,
        (6 , 3)
    )
    surfaces = (
        (0 , 1 , 2 , 3) ,
        (1 , 2 , 4 , 5) ,
        (5 , 4 , 7 , 6) ,
        (6 , 7 , 3 , 0) ,
        (0 , 7 , 4 , 1) ,
        (6 , 5 , 2 , 3)
    )

    glBegin (GL_QUADS)

    for surface in surfaces:
        x = 0
        for vertex in surface:
            x += 1
            glColor3fv (colors[x])
            glVertex3fv (verticies[vertex])
    glEnd ()
    glBegin (GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv (verticies[vertex])
    glEnd ()


def main():


    pygame.init ()
    display = (1000 , 700)
    display_surface = pygame.display.set_mode (display , DOUBLEBUF | OPENGLBLIT)
    pygame.display.set_caption ('solar panels')
    gluPerspective (45 , (display[0] / display[1]) , 0.1 , 50.0)
    glTranslatef (0 , 0 , -10)
    glRotatef (25 , 2 , 1 , 0)
    Mirroir()
    pygame.display.flip ()
    pygame.time.wait (10)

main ()
