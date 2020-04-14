
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


def Mirroir(a,b):
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
    glRotate (-a , 0 , 1, 0)
    glRotate (-b , 1 ,0 , 0)

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

def support():
    verticies1 = (
        (-0.1 , -3 , -0.1) ,
        (-0.1 , -3 , 0.1) ,
        (0.1 , -3 , 0.1) ,
        (0.1 , -3 , -0.1),
        (-0.1 , 0 , -0.1) ,
        (-0.1 , 0 , 0.1) ,
        (0.1 , 0 , 0.1) ,
        (0.1 , 0 , -0.1) ,


    )
    edges1 = (
        (0 , 1) ,
        (0 , 3) ,
        (0 , 4) ,
        (2 , 1) ,
        (2 , 3) ,
        (2 , 6) ,
        (4 , 0) ,
        (4 , 5) ,
        (4 , 7) ,
        (6 , 2) ,
        (6 , 7) ,
        (6 , 5)
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
            glVertex3fv (verticies1[vertex])
    glEnd ()
    glBegin (GL_LINES)
    for edge1 in edges1:
        for vertex in edge1:
            glVertex3fv (verticies1[vertex])
    glEnd ()


def main():


    pygame.init ()
    display = (1000 , 700)
    display_surface = pygame.display.set_mode (display , DOUBLEBUF | OPENGLBLIT)
    pygame.display.set_caption ('solar panels')
    gluPerspective (45 , (display[0] / display[1]) , 0.1 , 50.0)

    glTranslatef (0 , 0 , -10)

    glRotatef (25 , 2 , 1 , 0)

    KLEFT = False
    KRIGHT = False
    KUP = False
    KDOWN = False
    b=0
    a=0
    # Infinite while loop
    while True:
        # Event Handling loop
        for event in pygame.event.get ():
            if event.type == pygame.QUIT:
                pygame.quit ()
                quit ()
            # Kill Window

            # KEYEVENT KEYDOWN HANDLING
            if event.type == pygame.KEYDOWN:
                # TRANSLATE
                if event.key == pygame.K_LEFT:
                    KLEFT = True
                if event.key == pygame.K_RIGHT:
                    KRIGHT = True
                if event.key == pygame.K_UP:
                    KUP = True
                if event.key == pygame.K_DOWN:
                    KDOWN = True



            # KEYEVENT KEYUP HANDLING
            if event.type == pygame.KEYUP:
                # TRANSLATE
                if event.key == pygame.K_LEFT:
                    KLEFT = False
                if event.key == pygame.K_RIGHT:
                    KRIGHT = False
                if event.key == pygame.K_UP:
                    KUP = False
                if event.key == pygame.K_DOWN:
                    KDOWN = False
                if event.key == pygame.K_j:
                    KJ = False
                if event.key == pygame.K_l:
                    KL = False
        if KRIGHT == True:
            a += 5

        if KLEFT == True:
            a -= 5
        if KUP == True:
            b += 5

        if KDOWN == True:
            b -= 5

        glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix ()
        Mirroir(a,b)
        glPopMatrix ()
        support()
        pygame.display.flip ()
        pygame.time.wait (10)

main ()
