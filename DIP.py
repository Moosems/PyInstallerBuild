from tkinter import Tk, Label

class ExampleApp(Tk):
    def __init__(self):
        super().__init__()
        self.title("Example")
        self.label = Label(self, text="Hello World", font=("Courier New bold", 15))
        self.label.pack()

def create_application():
    app = ExampleApp()
    app.mainloop()

if __name__ == '__main__':
    create_application()