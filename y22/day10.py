import re
import numpy as np

register = []
cycle = 0
value = 1
with open("day10.dat") as file:
    lines = file.read().splitlines()
    for line in lines:
        found = re.match("(noop|addx)(?: ?(-?[0-9]+))?", line)
        if (found):
            if (found.group(1) == "noop"):
                cycle += 1
                register.append(value)
            elif (found.group(1) == "addx"):
                cycle += 1
                register.append(value)
                cycle += 1
                value += int(found.group(2))
                register.append(value)

sprite_position: int = 0


def render(display):
    import PIL
    from PIL import Image

    img = Image.fromarray(display, 'L')
    img = img.resize((4000, 600), resample=PIL.Image.NEAREST)
    img.show()


display = np.zeros(shape=(6, 40), dtype=np.int8)


def render_pixel(cycle: int, reg: int):
    global sprite_position
    if (cycle % 40 == 0):
        print("Cycle", f'{i:3d}', "-> ", end="")
    if ((cycle % 40) + 1 >= sprite_position and (cycle % 40) + 1 < sprite_position + 3):
        print("#", end="")
        display[int(cycle / 40)][cycle % 40] = 255
    else:
        print(".", end="")
        display[int(cycle / 40)][cycle % 40] = 0
    if (((cycle % 40) + 1) % 40 == 0):
        print()
    sprite_position = reg


strength1: int = 0
for i in range(20, len(register), 40):
    strength1 += (i * register[i - 2])
    print(i, register[i - 2], i * register[i - 2])

for i in range(0, len(register)):
    render_pixel(i, register[i])
print()

print("Find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles. What is the sum of these six signal strengths?")
print(" Answer:", strength1)

print("Render the image given by your program. What eight capital letters appear on your CRT?")
print(" See the generated image...")

render(display)
