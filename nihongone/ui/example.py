import urwid

# Define the functions to be called when buttons are pressed
def hello_world(button):
    output.set_text("Hello world!")

def test_message(button):
    output.set_text("This is a test!")

def exit_program(button):
    raise urwid.ExitMainLoop()

# Create the buttons
button_hello = urwid.Button("Press 1: Print 'Hello world!'")
urwid.connect_signal(button_hello, 'click', hello_world)

button_test = urwid.Button("Press 2: Print 'This is a test!'")
urwid.connect_signal(button_test, 'click', test_message)

button_exit = urwid.Button("Press 3: Exit the program")
urwid.connect_signal(button_exit, 'click', exit_program)

# Create a Text widget for output
output = urwid.Text("Output will be displayed here.")

# Arrange buttons and output in a vertical pile
pile = urwid.Pile([button_hello, button_test, button_exit, urwid.Divider(), output])
filler = urwid.Filler(pile, valign='top')

# Main event loop
def handle_input(key):
    if key == '1':
        hello_world(None)
    elif key == '2':
        test_message(None)
    elif key == '3':
        exit_program(None)

loop = urwid.MainLoop(filler, unhandled_input=handle_input)
loop.run()

