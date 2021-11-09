import pygame, pymunk
import pymunk.pygame_util

#Create class Arrow:
    #Create special method __init__(self, x, y) and add the creation of arrow in it like following.
        #vs = [(-80, 0), (0, 2), (2, 0), (0, -2)]
        #self.body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)  #Add self to all values to indicate object.
        #self.shape = pymunk.Poly(arrow_body, vs)
        #self.shape.density = 0.1   
        #self.body.position = 100, 140 #change this to x,y we passed in method.
        #space.add(self.body, self.shape) #do not return, because __init__ does not return values instead add the body and shape to space.
        
    #Create another method power(self, start, end) and shift the arrow power related code here as mentioned below.
        #diff = start - end
        #power = min(diff, 1000) * 13.5
        #impulse = (power*1, 0)
        #self.body.body_type = pymunk.Body. DYNAMIC
        #self.body.apply_impulse_at_world_point(impulse, self.body.position)
    


#Remove this entire function (create_arrow function).
def create_arrow():
    vs = [(-80, 0), (0, 2), (2, 0), (0, -2)]
    arrow_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
    arrow_shape = pymunk.Poly(arrow_body, vs)
    arrow_shape.density = 0.1   
    arrow_body.position = 100, 140
    return arrow_body, arrow_shape

def powerbar(ticks):
    current_time = ticks
    diff = current_time - start_time
    power = min(diff, 1000)
    h = power / 2
    pygame.draw.line(screen, pygame.Color("red"), (650, 550), (650, 550 - h), 10)


pygame.init()

height = 600
width = 690
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

#pymunk space
gravity = 1000
wind = 200
space = pymunk.Space()
space.gravity = wind, gravity
draw_options = pymunk.pygame_util.DrawOptions(screen)

#background
bg = pygame.image.load("bg.png")
bg = pygame.transform.scale(bg, (width, height))

#archer
archer = pygame.image.load("bow.png")
archer = pygame.transform.scale(archer, (100,150))

vs_rect = [(1, -80), (1, 80), (-1, 80), (-1, -80)]
target_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
target_shape = pymunk.Poly(target_body, vs_rect)
target_body.position = 600,400
target_image = pygame.image.load("target.png")
target_image = pygame.transform.scale(target_image, (25,160))
rope_img = pygame.image.load("rope.png")
rope_img = pygame.transform.scale(rope_img, (25,400))
space.add(target_body, target_shape)     

#Create arrow by calling Arrow class like arrow = Arrow(130, 85)
arrow_body, arrow_shape = create_arrow()
space.add(arrow_body, arrow_shape)

flying_arrows = []

while True:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                start_time = pygame.time.get_ticks()
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                end_time = pygame.time.get_ticks()
            
                #call power method of arrow here like arrow.power(start_time, end_time)
                diff = end_time - start_time
                power = min(diff, 1000) * 13.5
                impulse = (power*1, 0)
                arrow_body.body_type = pymunk.Body.DYNAMIC
                arrow_body.apply_impulse_at_world_point(impulse, arrow_body.position)
                
                flying_arrows.append(arrow_body) #change arrow_body to arrow.body
                
                #create a new arrow here by initializing arrow class like arrow = Arrow(130, 85) and remove the next two lines.
                arrow_body, arrow_shape = create_arrow()
                space.add(arrow_body, arrow_shape)
    
    if pygame.mouse.get_pressed()[0]:
        powerbar(pygame.time.get_ticks())

    space.debug_draw(draw_options)
    
    #space reload
    space.step(1/60)
    pygame.display.update()
    clock.tick(60)
