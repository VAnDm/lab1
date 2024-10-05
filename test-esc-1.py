import time


SET_COLOR = "\x1b[48;5;"
END = "\x1b[0m"
CLEAR = "\033[H"


def draw_line(offset = 0, length = 1, color = 222):
    line = " " * length
    print(f"{' ' * offset}{SET_COLOR}{color}m{line}{END}")


for i in range(20):
    draw_line(length = 20, color = 47, offset = i)
    print(f"{CLEAR}")
    time.sleep(0.5)