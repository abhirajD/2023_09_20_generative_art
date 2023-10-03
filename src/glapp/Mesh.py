import pygame
import numpy as np
from OpenGL.GL import *

class Mesh():
    def __init__(self, program_id):
        self.vertices = [
            [-1, -1, 0],
            [-1,  1, 0],
            [ 1, -1, 0],
            [ 1, -1, 0],
            [-1,  1, 0],
            [ 1,  1, 0]
        ]

        self.vertex_uv = [
            [0,0],
            [0,1],
            [1,0],
            [1,0],
            [0,1],
            [1,1]
        ]

        self.program_id = program_id
        self.vao_ref = glGenVertexArrays(1)
        glBindVertexArray(self.vao_ref)

        position_ref = glGenBuffers(1)
        position_data = np.array(self.vertices, dtype=np.float32)
        position_id = glGetAttribLocation(self.program_id, "position")
        glBindBuffer(GL_ARRAY_BUFFER, position_ref)
        glVertexAttribPointer(position_id, 3, GL_FLOAT, False, 0, None)
        glEnableVertexAttribArray(position_id)
        glBindBuffer(GL_ARRAY_BUFFER, position_ref)
        glBufferData(GL_ARRAY_BUFFER, position_data.ravel(), GL_STATIC_DRAW)

        uv_ref = glGenBuffers(1)
        uv_data = np.array(self.vertex_uv, dtype=np.float32)
        uv_id = glGetAttribLocation(self.program_id, "vertex_uv")
        glBindBuffer(GL_ARRAY_BUFFER, uv_ref)
        glVertexAttribPointer(uv_id, 2, GL_FLOAT, False, 0, None)
        glEnableVertexAttribArray(uv_id)
        glBindBuffer(GL_ARRAY_BUFFER, uv_ref)
        glBufferData(GL_ARRAY_BUFFER, uv_data.ravel(), GL_STATIC_DRAW)

    def draw(self):
        timer_id = glGetUniformLocation(self.program_id, "iTime")
        glUniform1f(timer_id, pygame.time.get_ticks() / 1000.0)

        mouse_id = glGetUniformLocation(self.program_id, "iMouse")
        glUniform2f(mouse_id, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        
        glBindVertexArray(self.vao_ref)
        glDrawArrays(GL_TRIANGLES, 0, len(self.vertices))
        

