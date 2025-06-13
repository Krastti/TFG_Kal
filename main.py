import tkinter as tk
from tkinter.ttk import Combobox
import Functions.Selected as s
import Functions.Calculation as c

class App:
    def __init__(self, root):
        self.first_label = None
        self.box = None
        self.second_label = None
        self.third_label = None
        self.third_label_ent = None
        self.root = root
        self.root.title('Calculator alloys')
        self.root.geometry('300x300')
        self.create_widgets()

    def create_widgets(self):
        self.first_label = tk.Label(
            self.root,
            text = 'Выберите, что вы хотите сделать:'
        )
        self.first_label.grid(column=0, row=0, padx=5)

        with open('Functions/Alloys') as alloys: alloys = [line.strip() for line in alloys]
        self.box = Combobox(
            self.root,
            values=alloys,
            width=15,
            state='readonly',
        )
        self.box.grid(column=0, row=1, pady = 5)
        self.box.current(0)
        self.box.bind('<<ComboboxSelected>>', lambda e: s.selected(e, self))

        self.second_label = tk.Label(
            self.root,
            text = f'Что вы хотите сделать?'
        )
        self.second_label.grid(column=0, row=2, padx=0)
        self.third_label = tk.Label(
            self.root,
            text = 'Сколько вы хотите сделать слитков?'
        )
        self.third_label.grid(column=0, row=3, padx=0)
        self.third_label_ent = tk.Entry(
            self.root,
            width = 10,
            state='disabled'
        )
        self.third_label_ent.grid(column=1, row=3, padx=0)

        calc_btn = tk.Button(
            self.root,
            text = 'Рассчитать',
            command = lambda: c.show_result(self)
        )
        calc_btn.grid(column=0, row=4)

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()