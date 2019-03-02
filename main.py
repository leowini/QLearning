import tkinter as tk
from PIL import Image

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.mapDims = (1920, 1080)

    def createMap(self):
        

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")
        self.canvas = tk.Canvas(root)
        self.canvas.pack
        self.img = tk.PhotoImage(Image.open("intersectionImage.png"))
        self.canvas.create_image(0,0, self.img)

root = tk.Tk()

app = Application(master=root)
app.mainloop()