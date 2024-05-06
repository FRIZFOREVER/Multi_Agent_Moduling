import tkinter as tk


class Graphics:

    """docstring for graphics."""

    def __init__(self, proc):
        self.proc = proc
        self.window = tk.Tk()
        self.window.title("Khromov_Kirill_Model")
        self.window.geometry('1000x1000')
        self.canvas = tk.Canvas(width=1000, height=1000)
        self.read_data()

    def run(self):
        self.window.mainloop()

    def read_data(self):
        for name in self.proc.tanks:
            x, y = self.proc.tanks[name].get_coords()
            self.canvas.create_rectangle(x, y, x+100, y+100, fill='White',
                                         outline='Black', width=2)
            self.canvas.pack(anchor='nw')
