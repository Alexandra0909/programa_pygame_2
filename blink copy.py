import pygame as pg
import time

funcionando = True  
estado = False 

pg.init()
screen = pg.display.set_mode((500, 500), 0, 32)
tiempoInicial = time.process_time()*1000

while funcionando:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            funcionando = False
            break
    tiempoActual = time.process_time()*1000
    if (tiempoActual - tiempoInicial) > 200:
        '''
        if estado:
           color = [220, 220, 0]
           estado = False
       else: 
           color = [50, 50, 50]
           estado = True
        '''
    screen.fill([100, 100, 100])
    pg.draw.circle(screen, color, (200, 200), 70)
    pg.display.flip()

    time.sleep(1)

pg.quit()