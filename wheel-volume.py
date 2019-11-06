from subprocess import check_output

from pynput import mouse, keyboard
from pynput.keyboard import Controller, KeyCode

XF86AudioRaiseVolume = KeyCode(269025043)
XF86AudioLowerVolume = KeyCode(269025041)

keyboard = Controller()


VOL = False


def on_scroll(x, y, dx, dy):
    global VOL

    if VOL:
        # print('Scrolled {0} at {1}'.format(
        #     'down' if dy < 0 else 'up',
        #     (x, y)))

        ##
        if dy < 0:
            # check_output(["amixer", "-D", "pulse", "sset", "Master", "3%-"])
            keyboard.press(XF86AudioLowerVolume)
            keyboard.release(XF86AudioLowerVolume)

        else:
            # check_output(["amixer", "-D", "pulse", "sset", "Master", "3%+"])
            keyboard.press(XF86AudioRaiseVolume)
            keyboard.release(XF86AudioRaiseVolume)


def on_click(x, y, button, pressed):
    global VOL

    # print('{0} at {1}'.format(
    #     'Pressed' if pressed else 'Released',
    #     (x, y)))

    if pressed and button == mouse.Button.right:
        VOL = True
    else:
        VOL = False


# Collect events until released
with mouse.Listener(
        on_click=on_click,
        on_scroll=on_scroll
        ) as listener:
    listener.join()
