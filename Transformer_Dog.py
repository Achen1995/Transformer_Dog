#Addison Chen
#Transformer Dog
#import basic OpenGL functionality
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from math import *
import numpy as np

window_width = 500.0
window_hight = 500.0

color = [0.0, 0.0, 1.0]

class Dog:

    def __init__(self):
        
        self.body = 0
        self.b_r_leg = -90
        self.b_l_leg = -90
        self.f_l_leg = 270
        self.f_r_leg = 270
        self.head = -200
        self.tail = -120
        
    def initGL(self):

        glClearColor (0.0, 0.0, 0.0, 0.0)
        glShadeModel (GL_FLAT)
        glOrtho(0, 500, 0, 500, 0, 500)

    def display(self):
    
        glClear (GL_COLOR_BUFFER_BIT)
        glPushMatrix()
        glTranslatef (-1.0, 0.0, 0.0)
        glRotatef (self.body, 0.0, 0.0, 1.0)
        glTranslatef (1.0, 0.0, 0.0)
        glPushMatrix()
        glScalef (4.1, 1.2, 1.0)
        glutWireCube (1.0)
        glPopMatrix()

        glPushMatrix()
        glTranslatef (1.0, 0.0, -0.2)
        glRotatef (self.b_r_leg, 0.0, 0.0, 1.0)
        glTranslatef (1.0, 0.0, 0.0)
        glPushMatrix()
        glScalef (1.0, 0.18, 0.18)
        glutWireCube (1.0)
        glPopMatrix()
        glPopMatrix()

        glPushMatrix()
        glTranslatef (1.0, 0.0, 0.2)
        glRotatef (self.b_l_leg, 0.0, 0.0, 1.0)
        glTranslatef (1.0, 0.0, 1.0)
        glPushMatrix()
        glScalef (1.0, 0.18, 0.18)
        glutWireCube (1.0)
        glPopMatrix()
        glPopMatrix() 
        
        glPushMatrix()
        glTranslatef (-1.0, 0.0, -0.2)
        glRotatef (self.f_r_leg, 0.0, 0.0, -1.0)
        glTranslatef (-1.0, 0.0, 0.0)
        glPushMatrix()
        glScalef (0.9, 0.2, 0.2)
        glutWireCube (1.0)
        glPopMatrix()
        glPopMatrix() 
        
        glPushMatrix()
        glTranslatef (-1.2, 0.0, 0.6)
        glRotatef (self.f_l_leg, 0.0, 0.0, -1.0)
        glTranslatef (-1.0, 0.0, 0.0)
        glPushMatrix()
        glScalef (0.9, 0.2, 0.2)
        glutWireCube (1.0)
        glPopMatrix()
        glPopMatrix() 
        
        glPushMatrix()
        glTranslatef (-2.5, 0.0, -0.2)
        glRotatef (self.head, 0.0, 0.0, -1.0)
        glTranslatef (0.5, -0.3, -1.0)
        glPushMatrix()
        glScalef (0.8, 0.3, 0.5)
        glutWireCube (1.6)
        glPopMatrix()
        glPopMatrix()
        
        glPushMatrix()
        glTranslatef (1.0, 0.0, 0.2)
        glRotatef (self.tail, 0.0, 0.0, 1.0)
        glTranslatef (-1.0, 0.4, 1.0)
        glPushMatrix()
        glScalef (1.5, 0.1, 0.2)
        glutWireCube (1.0)
        glPopMatrix()
        glPopMatrix() 
        
        glPopMatrix()
        glutSwapBuffers()


    def reshape (self, w, h):

        glViewport (0, 0, w,  h) # Defines a pixel rectangle in the window into which the final image is mapped.
                                 # The (x, y) parameter specifies the lower-left corner of the viewport, and width and height are the size of the viewport rectangle.
                                 # By default, the initial viewport values are (0, 0, winWidth, winHeight), where winWidth and winHeight are the size of the window.
                                 
        glMatrixMode (GL_PROJECTION)
        glLoadIdentity ()
        gluPerspective(95.0, w/h, 1, 20.0) #GLdouble fovy, GLdouble aspect, GLdouble zNear, GLdouble zFar
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef (0.0, 0.0, -5.0)


    def keyboard (self, *args):


        if (args[0] =='b'):

            self.b_r_leg = (self.b_r_leg+5) % 360
        elif (args[0] =='B'):
            self.b_r_leg = (self.b_r_leg-5) % 360


        glutPostRedisplay()
        
        if (args[0] =='b'):

            self.b_l_leg = (self.b_l_leg+5) % 360
        elif (args[0] =='B'):
            self.b_l_leg = (self.b_l_leg-5) % 360


        glutPostRedisplay()
        
        if (args[0] =='f'):

            self.f_r_leg = (self.f_r_leg+5) % 360
        elif (args[0] =='F'):
            self.f_r_leg = (self.f_r_leg-5) % 360


        glutPostRedisplay()
        
        if (args[0] =='f'):

            self.f_l_leg = (self.f_l_leg+5) % 360
        elif (args[0] =='F'):
            self.f_l_leg = (self.f_l_leg-5) % 360


        glutPostRedisplay()

        
        if (args[0] =='h'):

            self.head = (self.head+5) % 360
        elif (args[0] =='H'):
            self.head = (self.head-5) % 360


        glutPostRedisplay()
        
        if (args[0] =='t'):

            self.tail = (self.tail+5) % 360
        elif (args[0] =='T'):
            self.tail = (self.tail-5) % 360
            
            
        # The bottom code rotates the whole body

        glutPostRedisplay()
        
        if (args[0] =='d'):

            self.body = (self.body+5) % 360
        elif (args[0] =='D'):
            self.body = (self.body-5) % 360


        glutPostRedisplay()
        
        if (args[0] =='d'):

            self.b_r_leg = (self.b_r_leg+5) % 360
        elif (args[0] =='D'):
            self.b_r_leg = (self.b_r_leg+5) % 360


        glutPostRedisplay()
        
        if (args[0] =='d'):

            self.b_l_leg = (self.b_l_leg+5) % 360
        elif (args[0] =='D'):
            self.b_l_leg = (self.b_l_leg+5) % 360


        glutPostRedisplay()
        
        if (args[0] =='d'):

            self.f_r_leg = (self.f_r_leg+10) % 360
        elif (args[0] =='D'):
            self.f_r_leg = (self.f_r_leg-10) % 360


        glutPostRedisplay()
        
        if (args[0] =='d'):

            self.f_l_leg = (self.f_l_leg+10) % 360
        elif (args[0] =='D'):
            self.f_l_leg = (self.f_l_leg-10) % 360


        glutPostRedisplay()

        
        if (args[0] =='d'):

            self.head = (self.head+5) % 360
        elif (args[0] =='D'):
            self.head = (self.head-5) % 360


        glutPostRedisplay()
        
        if (args[0] =='d'):

            self.tail = (self.tail+5) % 360
        elif (args[0] =='D'):
            self.tail = (self.tail-5) % 360


        glutPostRedisplay()


    def main(self):

        glutInit(sys.argv)  #initial the system
        glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB)

        glutInitWindowSize(int(window_width), int(window_hight))#initial window size
        glutInitWindowPosition(100, 100)#initial window position

        glutCreateWindow("Transformer Dog")     #assign a title for the window

        self.initGL()

        glutDisplayFunc(self.display)
        glutReshapeFunc(self.reshape)
        glutKeyboardFunc(self.keyboard)

        glutMainLoop()  #callback function enter the GLUT event processing loop

if __name__ == "__main__":

    dog = Dog() #call the main function
    dog.main()
