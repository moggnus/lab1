RESET = "\033[0m"
RED   = "\u001b[41m"
WHITE = "\u001b[47m"
BLUE  = "\u001b[44m"
PIXEL='   '
height=15
lenght=height
for i in range(height//3):
    print(RED+PIXEL*(lenght)+RESET)
for i in range(height//3):
    print(WHITE+PIXEL*(lenght)+RESET)
for i in range(height//3):
    print(BLUE+PIXEL*(lenght)+RESET)

    