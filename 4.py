RED = "\u001b[41m"
BLUE = "\u001b[44m"
RESET = "\u001b[0m"
PIXEL = "  "
def fille():
    file = open('sequence.txt')
    odd = 0
    even = 0
    n = 1
    for x in file:
        if x.strip() != '':
            if n % 2 == 1:
                odd += abs(float(x))
            else:
                even += abs(float(x))
            n += 1
    file.close()
    total = odd + even
    odd_p = odd / total * 100
    even_p = even / total * 100
    print(f"Нечётные позиции: {round(odd, 2)}")
    print(f"{RED}{PIXEL * round(odd_p / 2)}{RESET} {round(odd_p, 2)}%")
    print(f"Чётные позиции: {round(even, 2)}")
    print(f"{BLUE}{PIXEL * round(even_p / 2)}{RESET} {round(even_p, 2)}%")
fille()
