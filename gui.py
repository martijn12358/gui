import tkinter as tk
import time
import threading
from PIL import ImageTk, Image


def test():
    print("test")
    time.sleep(1)
    print("test2")
    button.configure(background="black")


step_size = 1

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
buttonw = tk.Button(master=frame_control, text="w", command=lambda: threading.Thread(target=test).start())
buttonw.grid(row=0, column=1, sticky="nesw", pady=5, padx=5)
buttona = tk.Button(master=frame_control, text="a", command=lambda: threading.Thread(target=test).start())
buttona.grid(row=1, column=0, sticky="nesw", pady=5, padx=5)
button = tk.Button(master=frame_control, text="d", command=lambda: threading.Thread(target=test).start())
button.grid(row=1, column=2, sticky="nesw", pady=5, padx=5)
button = tk.Button(master=frame_control, text="s", command=lambda: threading.Thread(target=test).start())
button.grid(row=2, column=1, sticky="nesw", pady=5, padx=5)
button = tk.Button(master=frame_control, text="up", command=lambda: threading.Thread(target=test).start())
button.grid(row=0, column=3, sticky="nesw", pady=5, padx=5)
button = tk.Button(master=frame_control, text="down", command=lambda: threading.Thread(target=test).start())
button.grid(row=1, column=3, sticky="nesw", pady=5, padx=5)
button = tk.Button(master=frame_control, text="step size: " + str(step_size), command=lambda: threading.Thread(target=test).start())
button.grid(row=2, column=3, sticky="nesw", pady=5, padx=5)

frame_enter_location = tk.Frame(
    master=frame_left,
    relief=tk.RAISED,
    borderwidth=1
)
frame_enter_location.grid(column=0, row=1)
label= tk.Label(master=frame_enter_location, text="enter location")
inputbox = tk.Text(master=frame_enter_location, height=1, width=49)
label.grid(row=0, column=0)
inputbox.grid(row=1, column=0)

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
button = tk.Button(master=frame_functions, text="take picture", command=lambda: threading.Thread(target=test).start())
button.grid(row=5, column=0, sticky="nesw", pady=5, padx=5)
button = tk.Button(master=frame_functions, text="repeat camera", command=lambda: threading.Thread(target=test).start())
button.grid(row=6, column=0, sticky="nesw", pady=5, padx=5)
button = tk.Button(master=frame_functions, text="repeat gantry", command=lambda: threading.Thread(target=test).start())
button.grid(row=7, column=0, sticky="nesw", pady=5, padx=5)
button = tk.Button(master=frame_functions, text="place chip", command=lambda: threading.Thread(target=test).start())
button.grid(row=8, column=0, sticky="nesw", pady=5, padx=5)
#frame_functions.pack()

frame_right = tk.Frame(
    master=window,
    relief=tk.RAISED,
    borderwidth=1
)
frame_right.grid(column=2,row=0)
img = ImageTk.PhotoImage(Image.open("C:/Users/Martijn/Documents/3s/imgstacker/fotos/test_stilstaand00.png").resize((750, 500)))
label = tk.Label(master=frame_right, image=img)
label.grid(column=0, row=0)


window.mainloop()
