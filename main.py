from tkinter import *
from tkinter.colorchooser import askcolor
import json
import time


#GETTING SETTINGS FROM JSON FILE
file = open("settings.json", "r")
data = json.load(file)

TITLE = data["title"]
BACKGROUND = data["bg"]
TEXT_COLOR = data["fg"]
FONT = (data["font"]["style"], data["font"]["size"])

file.close()


#MAIN WINDOW
window = Tk()
window.resizable(width=False, height=False)
window.title(TITLE)
menubar = Menu(window)
window.config(menu=menubar)    


#SETTINGS WINDOW
def settings():
    settings_window = Toplevel(window)
    settings_window.resizable(width=False, height=False)

    #TITLE
    Label(settings_window, text="Title").grid(column=0, row=0)
    title_text = Text(settings_window, height=1, width=10)
    title_text.grid(column=1, row=0)

    #BACKGROUND
    Label(settings_window, text="Background").grid(column=0, row=1)
    bg_text = Text(settings_window, height=1, width=10)
    bg_text.grid(column=1, row=1)
    Button(settings_window, text="Color Chooser", command=lambda:bg_text.insert(INSERT,f"{askcolor()[1]}")).grid(column=2, row=1)
    

    #TEXT COLOR
    Label(settings_window, text="Text Color").grid(column=0, row=2)
    color_text = Text(settings_window, height=1, width=10)
    color_text.grid(column=1, row=2)
    Button(settings_window, text="Color Chooser", command=lambda:color_text.insert(INSERT,f"{askcolor()[1]}")).grid(column=2, row=2)


    #FONT STYLE
    Label(settings_window, text="Font Style").grid(column=0, row=3)
    style_text = Text(settings_window, height=1, width=10)
    style_text.grid(column=1, row=3)

    #FONT SIZE
    Label(settings_window, text="Font Size").grid(column=0, row=4)
    size_text = Text(settings_window, height=1, width=10)
    size_text.grid(column=1, row=4)


    #SAVE
    def save():
        new_title = title_text.get("1.0", END).split("\n")[0]
        new_bg = bg_text.get("1.0", END).split("\n")[0]
        new_color = color_text.get("1.0", END).split("\n")[0]
        new_style = style_text.get("1.0", END).split("\n")[0]
        new_size = size_text.get("1.0", END).split("\n")[0]


        data["title"] = new_title
        data["bg"] = new_bg
        data["fg"] = new_color
        data["font"]["style"] = new_style
        data["font"]["size"] = new_size
        
        with open("settings.json", "w") as file:
            json.dump(data, file)
            print("Settings saved.")

    Button(settings_window, text="Save", command=save, width=12).grid(column=0, row=5, columnspan=3)


#MENUBAR
fileMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Menu", menu=fileMenu)
fileMenu.add_command(label="Style", command=settings)


#CLOCK
def update_time():
    time_string = time.strftime("%H:%M:%S %p")
    time_label.config(text = time_string)
    time_label.after(1000, update_time)


time_label = Label(window, font=FONT, fg=TEXT_COLOR, background=BACKGROUND)
time_label.pack()

update_time()





window.mainloop()