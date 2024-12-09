import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import *
from random import *
from time import *

angle=0.0
speed = 90.0 
rotation_direction = 1  
speed_change_rate = 30.0  
direction_change_interval = 5.0  
last_time = time()
direction_change_time = time() + direction_change_interval

def init():
    glClearColor(0.302, 0.851, 0.929, 1.0)

def rotation():
    global angle, speed, last_time, rotation_direction
    current_time = time()
    elapsed_time = current_time - last_time
    angle += speed * rotation_direction * elapsed_time
    angle %= 360
    last_time = current_time

def circle(a,b,r):
    glColor4f(1.0, 0.9333, 0.3608, 1.0)
    glBegin(GL_POLYGON)
    for i in range(36):
        theta=(2.0*pi*i) / 36.0
        x=a + r * cos(theta)
        y=b + r * sin(theta)
        glVertex3f(x,y,0.0)
    glEnd()

def hills():
    glColor4f(0,0.5,0,1.0)
    glBegin(GL_TRIANGLES)
    glVertex3f(-8,-7,0)
    glVertex3f(0,-2,0)
    glVertex3f(8,-7,0)
    glEnd()

    glColor4f(0,0.6,0,1.0)
    glBegin(GL_TRIANGLES)
    glVertex3f(-15.5,-7,0)
    glVertex3f(-6.5,0.5,0)
    glVertex3f(3,-7,0)
    glEnd()

    glColor4f(0.2,0.8,0,1.0)
    glBegin(GL_TRIANGLES)
    glVertex3f(-4,-7,0)
    glVertex3f(5.5,-0.5,0)
    glVertex3f(14,-7,0)
    glEnd()


def blades(x,y):
    global angle

    glPushMatrix()
    glTranslatef(x,y,0)
    glRotatef(angle,0,0,1)
    glTranslatef(-x,-y,0)

    for i in range(4):
        glPushMatrix()
        glTranslatef(x,y,0)
        glRotatef(i * 90 , 0.0, 0.0, 1.0)
        glTranslatef(-x,-y,0)
        glColor4f(0.9451, 0.9451, 0.9451, 1.0)
        glBegin(GL_TRIANGLES)
        glVertex3f(x,y,0)
        glVertex3f(x+1,y+1,0)
        glVertex3f(x+0.6,y+0.87,0)
        glEnd()
        glPopMatrix()

    glPopMatrix()

def windmill(x,y):
    glColor4f(0.7569, 0.7569, 0.7569, 1.0)
    glBegin(GL_POLYGON)
    glVertex3f(x,y,0)
    glVertex3f(x+0.4,y,0)
    glVertex3f(x+0.33,y+1.5,0)
    glVertex3f(x+0.25,y+3,0)
    glVertex3f(x+0.15,y+3,0)
    glVertex3f(x+0.07,y+1.5,0)
    glEnd()

    blades(x+0.2,y+3)

def main():
    global speed, rotation_direction, direction_change_time
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(80, (display[0]/display[1]),0.1,50.0)
    glTranslate(0,0,-7)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        current_time = time()
        if current_time >= direction_change_time:
            rotation_direction *= -1
            direction_change_time = current_time + direction_change_interval  # Schedule next change

       
        speed += speed_change_rate * rotation_direction
        if speed < 200: 
            speed = 500
        if speed > 500: 
            speed = 500
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        init()
        circle(4.5,4,0.5)


        
        windmill(-6,-0.5)
        windmill(-3.3,-2.5)
        windmill(0,-2.5)
        windmill(3.3,-2)
        windmill(6.3,-1.5)

        hills()        
        
        rotation()
        
        pygame.display.flip()
        pygame.time.wait(10)

main()
