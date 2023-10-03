from glapp.PyOGLApp import *
from glapp.Utils import *
from glapp.Mesh import *

import os

print(os.getcwd())
print(os.listdir("shaders"))

class MyFirstShaderToyPort(PyOGLApp):
    def __init__(self):
        super().__init__(0, 0, 700, 700, "MyFirstShaderToyPort")
        self.screen_plane = None

    def initialize(self):
        self.program_id = create_program(open("shaders/vert.vs").read(), open("shaders/frag_fractal_v1.vs").read())
        self.screen_plane = Mesh(self.program_id)

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(self.program_id)

        res_id = glGetUniformLocation(self.program_id, "iResolution")
        glUniform2f(res_id, self.screen_width, self.screen_height)
        self.screen_plane.draw()

MyFirstShaderToyPort().mainLoop()