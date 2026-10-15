BLUE = "\u001b[44m"
RESET = "\u001b[0m"
PIXEL = "  "
def p():
    hig = 5
    wid = 25
    for i in range(hig):
        line = ''
        for k in range(wid):
            c = k % 8                
            if c <= 4:
                a = c                
            else:
                a = 8 - c            
            b = 4 - a                
            if i == a or i == b:
                line += BLUE + PIXEL + RESET
            else:
                line += PIXEL
        print(line)
p()