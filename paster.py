import typer
import keyboard
import pyperclip
import time

app = typer.Typer()

def type_clipboard_content():
    content = pyperclip.paste()
    for char in content:
        keyboard.write(char)
        time.sleep(0.1)  # 100ms delay

@app.command()
def listen():
    typer.echo("Listening for Ctrl+V...")
    keyboard.add_hotkey('ctrl+v', type_clipboard_content)
    keyboard.wait('esc')  # Script will run until 'esc' is pressed
    typer.echo("Stopping...")

if __name__ == "__main__":
    app()
