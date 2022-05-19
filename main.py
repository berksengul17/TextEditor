from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfile, asksaveasfile

#Styling
#s = ttk.Style()
#s.configure("TFrame", background="red")

def openFile():
    file = askopenfile(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file:
        txt_edit.delete("1.0", END)
        txt_edit.insert("1.0", file.read())
        root.title("*" + file.name + " - " + TITLE)

def saveAsFile():
    with open(f"{asksaveasfile().name}", "a") as textFile:
        textFile.write(txt_edit.get("1.0", END))

def saveFile():
    title = root.title()
    if title != TITLE:
        filepath = title[1 : title.find("-")]
        with open(filepath, "w") as file:
            file.write(txt_edit.get("1.0", END))

        root.title(file.name + " - " + TITLE)



#Initializing tkinter
root = Tk()
TITLE = "Text Editor"
root.title(TITLE)
root.rowconfigure(0, minsize=500, weight=1)
root.columnconfigure(1, minsize=500, weight=1)

#Initializing widgets
txt_edit = Text(root)
btn_frame = ttk.Frame(root)

btn_open = ttk.Button(btn_frame, text="Open", command=openFile)
btn_save = ttk.Button(btn_frame, text="Save", command=saveFile)
btn_saveAs = ttk.Button(btn_frame, text="Save As...", command=saveAsFile)

#Placing widgets
btn_frame.grid(row=0, column=0, sticky="ns")
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_saveAs.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
txt_edit.grid(row=0, column=1, sticky="nsew")


#Event loop
root.mainloop()
