from tkinter import *

root = Tk()
root.title('Бесполезные кнопки-2')
root.geometry('200x185')

class Application(Frame):
    '''GUI приложение с тремя кнопками'''
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # 1 кнопка
        self.bttn1 = Button(self, text= 'Я ничего делаю!')
        self.bttn1.grid()
        # 2 кнопка
        self.bttn2 = Button(self, text = 'И я тоже !')
        self.bttn2.grid()
        # 3 кнопка
        self.bttn3 = Button(self, text = 'И я!')
        self.bttn3.grid()

app = Application(root)








root.mainloop()