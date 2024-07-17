from pygame import *
import sys

def pintarceldas():
    for row in range(rows):
        for col in range(cols):
            if celdas[row][col] == 1:
                draw.rect(screen, (255, 255, 255), (col * tamaño_celda, row * tamaño_celda, tamaño_celda, tamaño_celda))
            else:
                draw.rect(screen, (0, 0, 0), (col * tamaño_celda, row * tamaño_celda, tamaño_celda, tamaño_celda))

def validar_lados(celdas, pos_x, pos_y):
    contador = 0
    # Asegurarse de que las coordenadas no se salgan de los límites
    if pos_y - 1 >= 0 and celdas[pos_x][pos_y - 1] == 1:
        contador += 1
    if pos_y + 1 < cols and celdas[pos_x][pos_y + 1] == 1:
        contador += 1
    if pos_x - 1 >= 0 and celdas[pos_x - 1][pos_y] == 1:
        contador += 1
    if pos_x + 1 < rows and celdas[pos_x + 1][pos_y] == 1:
        contador += 1
    if pos_x - 1 >= 0 and pos_y - 1 >= 0 and celdas[pos_x - 1][pos_y - 1] == 1:
        contador += 1
    if pos_x + 1 < rows and pos_y + 1 < cols and celdas[pos_x + 1][pos_y + 1] == 1:
        contador += 1
    if pos_x - 1 >= 0 and pos_y + 1 < cols and celdas[pos_x - 1][pos_y + 1] == 1:
        contador += 1
    if pos_x + 1 < rows and pos_y - 1 >= 0 and celdas[pos_x + 1][pos_y - 1] == 1:
        contador += 1

    return contador
    
    

def validarceldas():
    nueva_celdas = [[celdas[row][col] for col in range(cols)] for row in range(rows)]
    for row in range(rows):
        for col in range(cols):
            vali = validar_lados(celdas, row, col)
            if celdas[row][col] == 1:
                if vali < 2 or vali > 3:
                    nueva_celdas[row][col] = 0
            else:
                if vali == 3:
                    nueva_celdas[row][col] = 1
    return nueva_celdas
    


# ------------ CONFIGURACION DE LA VENTANA ------------
init();
screen_width = 1000
screen_height = 800
tamaño_celda = 10


screen = display.set_mode((screen_width, screen_height))
display.set_caption("Juego de la vida")

run = True

# ------------- CELDAS ------------------
cols = screen_width // tamaño_celda
rows = screen_height // tamaño_celda

celdas = [[0 for x in range(cols)] for y in range(rows)]

validacion = False
TIMER_EVENT = USEREVENT + 1
time.set_timer(TIMER_EVENT, 50)



# ------------ BUCLE PRINCIPAL ------------

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == MOUSEBUTTONDOWN: # ESTADO DE CADA CELDA
            x, y = mouse.get_pos()
            col = x // tamaño_celda
            row = y // tamaño_celda
            celdas[row][col] = 1 if celdas[row][col] == 0 else 0
        elif e.type == KEYDOWN:
            if e.key == K_q:
                run = False
            elif e.key == K_p:
                if validacion == False:
                    validacion = True
                else:
                    validacion = False
        elif e.type == TIMER_EVENT:
            if validacion:
                celdas = validarceldas()
    
    screen.fill((0, 0, 0)) # COLOR NEGRO
    
    
    
    for row in range(rows):
        draw.line(screen, (255,255,255), (0, row * tamaño_celda), (screen_width, row * tamaño_celda))

    # Dibuja las líneas verticales
    for col in range(cols):
        draw.line(screen, (255,255,255), (col * tamaño_celda, 0), (col * tamaño_celda, screen_height))

    
    pintarceldas()
    
    
    display.flip()



# ------------ SALIDA ------------
quit()
sys.exit()