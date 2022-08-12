from tkinter import Tk, Label

class ExampleApp(Tk):
    def __init__(self):
        super().__init__()
        self.label = Label(self, text="Hello World")
        self.label.pack()

def create_application():
    app = ExampleApp()
    app.mainloop()

if __name__ == '__main__':
    create_application()