import pygame
from pygame.locals import *

import os
import sys


class PyOGLApp():
    def __init__(self, screen_posX, screen_posY, screen_width, screen_height, screen_caption):
        self._running = True
        self._display_surf = None
    
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (screen_posX,screen_posY)
        self.screen_size = self.screen_width, self.screen_height = screen_width, screen_height
        self.screen_caption = screen_caption

        pygame.init()
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLEBUFFERS, 1)
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLESAMPLES, 4)
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)
        pygame.display.gl_set_attribute(pygame.GL_DEPTH_SIZE, 32)

        # self.screen = pygame.display.set_mode(self.screen_size, pygame.DOUBLEBUF | pygame.OPENGL | pygame.OPENGLBLIT | pygame.RESIZABLE)
        # self.screen = pygame.display.set_mode(self.screen_size, DOUBLEBUF | OPENGL | OPENGLBLIT | RESIZABLE)
        self.screen = pygame.display.set_mode(self.screen_size, DOUBLEBUF | OPENGL)
        pygame.display.set_caption(self.screen_caption)

        self.program_id = None
        self.clock = pygame.time.Clock()

    def mainLoop(self):
        done = False
        self.initialize()

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            self.display()
            pygame.display.flip()
            self.clock.tick(60)
        
        pygame.quit()
