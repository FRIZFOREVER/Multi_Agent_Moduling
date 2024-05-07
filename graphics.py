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
        self.btn = tk.Button(text="start")
        self.btn.pack()

    def run(self):
        self.window.mainloop()

    def read_data(self):
        for item in self.proc.tanks.values():
            x, y = item.get_coords()
            self.canvas.create_rectangle(x, y, x+100, y+100, fill='White',
                                         outline='Black', width=2)
        for item in self.proc.flows:
            x0, y0 = item.get_start()
            x1, y1 = item.get_end()
            self.canvas.create_line(x0, y0, x1, y1, arrow=tk.LAST)
            self.canvas.pack(anchor='nw')
