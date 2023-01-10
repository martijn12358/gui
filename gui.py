import tkinter as tk
import tkinter.messagebox
import time
import threading
from PIL import ImageTk, Image
import json

buttonList = []
settings = {}
def load_settings():
    with open("settings.json", "r") as f:
        global settings
        settings = json.load(f)
def update_settings():
    with open("settings.json", "w") as f:
        json.dump(settings, f)
def test():
    print("test")
    time.sleep(1)
    print("test2")
    enableButtons()

def disableButtons():
    for i in buttonList:
        i.configure(state="disabled")

def enableButtons():
    for i in buttonList:
        i.configure(state="active")

def update_waveguide_value(value):
    label_val.config(text=f"waveguide value: {value}")
    settings["waveguide_value"] = value
    update_settings()


def take_picture(camera, filename):
    if camera:
        print(f"waveguide " + filename)
    else:
        print(f"tct " + filename)

def popup_camera():
    popup = tk.Toplevel()
    popup.title("Popup Window")
    popup.grab_set()
    popup.minsize(200, 100)

    # add a label to the popup window
    label = tk.Label(popup, text="enter filename")
    label.grid(column=0, row=0)
    file_name = tk.StringVar()
    file_entry = tk.Entry(popup, textvariable=file_name)
    file_entry.grid(column=0, row=1)

    label = tk.Label(popup, text=".png")
    label.grid(column=1, row=1, sticky="w")

    label = tk.Label(popup, text="select camera")
    label.grid(column=0, row=2)
    # create the checkboxes
    checkbox_var_1 = tk.IntVar()
    checkbox_var_1.set(1)
    checkbox_1 = tk.Checkbutton(popup, text="waveguide", variable=checkbox_var_1, onvalue=1, offvalue=0,
                                command=lambda: checkbox_var_2.set(0))
    checkbox_1.grid(column=0, row=3)

    checkbox_var_2 = tk.IntVar()
    checkbox_2 = tk.Checkbutton(popup, text="tct", variable=checkbox_var_2, onvalue=1, offvalue=0,
                                command=lambda: checkbox_var_1.set(0))
    checkbox_2.grid(column=1, row=3)

    button = tk.Button(popup, text="take picture", command=lambda: [take_picture(checkbox_var_1.get(), file_name.get()), popup.destroy()])
    button.grid(column=0, row=4)
    button = tk.Button(popup, text="Close", command=popup.destroy)
    button.grid(column=1, row=4)


def move_input(input):
   try:
       test_exception(input)
   except Exception as e:
       tkinter.messagebox.showerror(message=str(e))


def test_exception(input):
    if input.isdigit():
        print(input)
    else:
        raise Exception("invalid input")


def change_picture(img):
    im_label.configure(image=img)


step_size = 1
load_settings()
window = tk.Tk()

frame_left = tk.Frame(
    master=window,
    relief=tk.RAISED,
    borderwidth=1
)
frame_left.grid(column=0, row=0)
frame_control = tk.Frame(
    master=frame_left,
    relief=tk.RAISED,
    borderwidth=1
)
frame_control.grid(column=0, row=0)
frame_control.columnconfigure(0, minsize=100)
frame_control.columnconfigure(1, minsize=100)
frame_control.columnconfigure(2, minsize=100)
frame_control.columnconfigure(3, minsize=100)
frame_control.rowconfigure(0, minsize=100)
frame_control.rowconfigure(1, minsize=100)
frame_control.rowconfigure(2, minsize=100)
buttonw = tk.Button(master=frame_control, text="w", command=lambda: [disableButtons(), threading.Thread(target=test).start()])
buttonw.grid(row=0, column=1, sticky="nesw", pady=5, padx=5)
buttonList.append(buttonw)
buttona = tk.Button(master=frame_control, text="a", command=lambda: [disableButtons(), threading.Thread(target=test).start()])
buttona.grid(row=1, column=0, sticky="nesw", pady=5, padx=5)
buttonList.append(buttona)
button = tk.Button(master=frame_control, text="d", command=lambda: [disableButtons(), threading.Thread(target=test).start()])
button.grid(row=1, column=2, sticky="nesw", pady=5, padx=5)
button = tk.Button(master=frame_control, text="s", command=lambda: [disableButtons(), threading.Thread(target=test).start()])
button.grid(row=2, column=1, sticky="nesw", pady=5, padx=5)
button = tk.Button(master=frame_control, text="up", command=lambda: [disableButtons(), threading.Thread(target=test).start()])
button.grid(row=0, column=3, sticky="nesw", pady=5, padx=5)
button = tk.Button(master=frame_control, text="down", command=lambda: [disableButtons(), threading.Thread(target=test).start()])
button.grid(row=1, column=3, sticky="nesw", pady=5, padx=5)
button = tk.Button(master=frame_control, text="step size: " + str(step_size), command=lambda: [disableButtons(), threading.Thread(target=test).start()])
button.grid(row=2, column=3, sticky="nesw", pady=5, padx=5)

frame_enter_location = tk.Frame(
    master=frame_left,
    relief=tk.RAISED,
    borderwidth=1
)
frame_enter_location.grid(column=0, row=1, sticky="nesw")
label= tk.Label(master=frame_enter_location, text="enter location")
location = tk.StringVar()
location_entry = tk.Entry(master=frame_enter_location, textvariable=location)
label.grid(row=0, column=0)
location_entry.grid(row=1, column=0)
button = tk.Button(master=frame_enter_location, text=f"move gantry to location", command=lambda: [threading.Thread(target=move_input(location.get())).start(), location_entry.delete(0, 100 )])
button.grid(row=2, column=0)

frame_functions = tk.Frame(
    master=frame_left,
    relief=tk.RAISED,
    borderwidth=1
)
frame_functions.grid(column=0, row=2)
frame_functions.columnconfigure(0,minsize=400)
button = tk.Button(master=frame_functions, text="home", command=lambda: threading.Thread(target=test).start())
button.grid(row=0, column=0, sticky="nesw", pady=5, padx=5)
button = tk.Button(master=frame_functions, text="pickup", command=lambda: threading.Thread(target=test).start())
button.grid(row=1, column=0, sticky="nsw", pady=5, padx=5)
button = tk.Button(master=frame_functions, text="return chip", command=lambda: threading.Thread(target=test).start())
button.grid(row=2, column=0, sticky="nesw", pady=5, padx=5)
button = tk.Button(master=frame_functions, text="angle measurement", command=lambda: threading.Thread(target=test).start())
button.grid(row=3, column=0, sticky="nesw", pady=5, padx=5)
button = tk.Button(master=frame_functions, text="entrance detection", command=lambda: threading.Thread(target=test).start())
button.grid(row=4, column=0, sticky="nesw", pady=5, padx=5)
button = tk.Button(master=frame_functions, text="take picture", command=lambda: popup_camera())
button.grid(row=5, column=0, sticky="nesw", pady=5, padx=5)
button = tk.Button(master=frame_functions, text="repeat camera", command=lambda: threading.Thread(target=test).start())
button.grid(row=6, column=0, sticky="nesw", pady=5, padx=5)
button = tk.Button(master=frame_functions, text="repeat gantry", command=lambda: threading.Thread(target=test).start())
button.grid(row=7, column=0, sticky="nesw", pady=5, padx=5)
button = tk.Button(master=frame_functions, text="place chip", command=lambda: threading.Thread(target=test).start())
button.grid(row=8, column=0, sticky="nesw", pady=5, padx=5)

frame_settings = tk.Frame(
    master=window,
    relief=tk.RAISED,
    borderwidth=1
)
frame_settings.grid(column=1,row=0)
frame_settings.columnconfigure(0, minsize=150)
start_val = settings["waveguide_value"]
label_val = tk.Label(master=frame_settings, text=f"waveguide value: {start_val}")
label_val.grid(column=0, row=1)
slider_value = tk.IntVar()
slider_value.set(settings["waveguide_value"])
slider = tk.Scale(master=frame_settings, from_=0, to=100, orient=tk.HORIZONTAL,
                  variable=slider_value, resolution=5, command=update_waveguide_value)
slider.grid(column=0, row=0)


frame_pictures = tk.Frame(
    master=window,
    relief=tk.RAISED,
    borderwidth=1
)
frame_pictures.grid(column=2,row=0)
img = ImageTk.PhotoImage(Image.open("C:/Users/Martijn/Documents/3s/imgstacker/fotos/test_stilstaand00.png").resize((750, 500)))
img2 = ImageTk.PhotoImage(Image.open("C:/Users/Martijn/Documents/3s/imgstacker/fotos/test.png").resize((750, 500)))
im_label = tk.Label(master=frame_pictures, image=img)
im_label.grid(column=0, row=0)
button = tk.Button(master=frame_pictures, text="foto2", command= lambda: change_picture(img2))
button.grid(row=1, column=0, sticky="nesw", pady=5, padx=5)

window.mainloop()
