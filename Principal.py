"""
Universidad del Valle de Guatemala
Graficas por computadora
Jorge Súchite
16/11/11


"""


from pygame.locals import *

from RenderOGL import Renderer
import shader

deltaTime = 0.0

pygame.init()
clock = pygame.time.Clock()
screenSize = (960, 540)
screen = pygame.display.set_mode(screenSize, DOUBLEBUF | OPENGL)

r = Renderer(screen)
r.setShaders(shader.vertex_shader, shader.fragment_shader)
r.createObjects()


cubeX = 0
cubeY = 0
cubeZ = 5
cubePitch = 0
cubeYaw = 0
cubeRoll = 0

isPlaying = True
while isPlaying:
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        cubePitch += 20 * deltaTime
    if keys[pygame.K_DOWN]:
        cubePitch -= 20 * deltaTime
    if keys[pygame.K_LEFT]:
        cubeYaw += 20 * deltaTime
    if keys[pygame.K_RIGHT]:
        cubeYaw -= 20 * deltaTime
    if keys[pygame.K_z]:
        cubeRoll += 20 * deltaTime
    if keys[pygame.K_x]:
        cubeRoll -= 20 * deltaTime

    if keys[pygame.K_q]:
        cubeY -= 2 * deltaTime
    if keys[pygame.K_e]:
        cubeY += 2 * deltaTime
    if keys[pygame.K_a]:
        cubeX -= 2 * deltaTime
    if keys[pygame.K_d]:
        cubeX += 2 * deltaTime
    if keys[pygame.K_w]:
        cubeZ -= 2 * deltaTime
    if keys[pygame.K_s]:
        cubeZ += 2 * deltaTime

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            isPlaying = False
        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_1:
                r.filledMode()
            elif ev.key == pygame.K_2:
                r.wireframeMode
            elif ev.key == pygame.K_ESCAPE:
                isPlaying = False


    r.rotarObjPitch(cubePitch)
    r.rotarObjYaw(cubeYaw)
    r.rotarObjRoll(cubeRoll)
    r.translateCube(cubeX, cubeY, cubeZ)

    r.render()

    pygame.display.flip()
    clock.tick(60)
    deltaTime = clock.get_time() / 1000

pygame.quit()
