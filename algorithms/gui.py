import tkinter
class gui():
    def __init__(self):
        self.pro=tkinter.Tk()
        self.label1=tkinter.Label(self.pro,text='Hello cunts!')
        self.label2=tkinter.Label(self.pro,text='First GUI yet')
        self.label1.pack()
        self.label2.pack()
        tkinter.mainloop()
me=gui()
    