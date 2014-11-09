from __future__ import print_function, unicode_literals, absolute_import
import sys, os, subprocess, platform

try:
    import toga
except ImportError:
    if platform.system() == "Windows":
        current_dir = os.getcwd()
        os.chdir(os.path.dirname(os.path.realpath(__file__)) + "\\Toga\\toga\\")
        subprocess.call(["python", os.path.dirname(os.path.realpath(__file__)) + "\\setup.py", "install"], shell=False)
        os.chdir(current_dir)
        import toga
    elif platform.system() == "Linux":
        print("Linux!")
        sys.exit(0)
        pass

def button_handler(widget):
        print("Hello FLE!")


def build(app):
        container = toga.Container()

        button = toga.Button('Hello world', on_press=button_handler)

        container.add(button)

        return container


if __name__ == '__main__':
        app = toga.App('KA Lite', 'KA Lite', startup=build)
        app.main_loop()