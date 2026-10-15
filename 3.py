import time
RED = "\u001b[41m"
BLUE = "\u001b[44m"
WHITE = "\u001b[47m"
RESET = "\u001b[0m"
def animation():
    pixel = ' ' * 30
    height = 3   
    colors = [RED, WHITE, BLUE]   
    for frame in range(9):       
        for k in range(3):        
            for i in range(height):
                print(colors[(frame + k) % 3] + pixel + RESET)
        print('\x1b[9A', end='')  
        time.sleep(0.5)
    print('\x1b[9B')             
animation()