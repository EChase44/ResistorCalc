from tkinter import*
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import messagebox

calculation_history = []
max_size = 5

def first():
    element1 = str(ring1.get())
    if element1 == '---':
        messagebox.showinfo('Неудачная попытка', 'Выберите цвет')
    elif element1 == 'Коричневый':
        return 100
    elif element1 == 'Красный':
        return 200
    elif element1 == 'Оранжевый':
        return 300
    elif element1 == 'Желтый':
        return 400
    elif element1 == 'Зеленый':
        return 500
    elif element1 == 'Синий':
        return 600
    elif element1 == 'Фиолетовый':
        return 700
    elif element1 == 'Серый':
        return 800
    elif element1 == 'Белый':
        return 900
def second():
    element2 = str(ring2.get())
    if element2 == '---':
        messagebox.showinfo('Неудачная попытка', 'Выберите цвет')
    elif element2 == 'Черный':
        return 0
    elif element2 == 'Коричневый':
        return 10
    elif element2 == 'Красный':
        return 20
    elif element2 == 'Оранжевый':
        return 30
    elif element2 == 'Желтый':
        return 40
    elif element2 == 'Зеленый':
        return 50
    elif element2 == 'Синий':
        return 60
    elif element2 == 'Фиолетовый':
        return 70
    elif element2 == 'Серый':
        return 80
    elif element2 == 'Белый':
        return 90
def six():
    element6 = str(ring3.get())
    if element6 == '4-х полосный резистор':
        return True
    elif element6 == 'Коричневый':
        return 1
    elif element6 == 'Красный':
        return 2
    elif element6 == 'Оранжевый':
        return 3
    elif element6 == 'Желтый':
        return 4
    elif element6 == 'Зеленый':
        return 5
    elif element6 == 'Синий':
        return 6
    elif element6 == 'Фиолетовый':
        return 7
    elif element6 == 'Серый':
        return 8
    elif element6 == 'Белый':
        return 9 
def third():
    element3 = str(multiplier.get())
    if element3 == '---':
        messagebox.showinfo('Неудачная попытка', 'Выберите цвет')
    elif element3 == 'Черный':
        return 1
    elif element3 == 'Коричневый':
        return 10
    elif element3 == 'Красный':
        return 100
    elif element3 == 'Оранжевый':
        return 1000
    elif element3 == 'Желтый':
        return 10000
    elif element3 == 'Зеленый':
        return 100000
    elif element3 == 'Синий':
        return 1000000
    elif element3 == 'Фиолетовый':
        return 10000000
    elif element3 == 'Золотой':
        return 0.1
    elif element3 == 'Серебряный':
        return 0.01
def fourth():
    element4 = str(accuracy.get())
    if element4 == '---':
        messagebox.showinfo('Неудачная попытка', 'Выберите цвет')
    elif element4 == 'Коричневый':
        return '±1%'
    elif element4 == 'Красный':
        return '±2%'
    elif element4 == 'Зеленый':
        return '±0.5%'
    elif element4 == 'Синий':
        return '±0.25%'
    elif element4 == 'Фиолетовый':
        return '±0.1%'
    elif element4 == 'Серый':
        return '±0.05%'
    elif element4 == 'Золотой':
        return '±5%'
    elif element4 == 'Серебряный':
        return '±10%'
        
def Resist():
    if six() == True:
        R1= (first() + second())/10 *third()
    else:
        R1 = (first() + second()+ six()) * third()
    if R1 > 1000000000:
        R1 = round(R1, 2)
        R1 = str(R1/1000000000)
        R = R1 + ' ' + fourth() + ' ' + 'ГОм'
    elif R1 > 999 and R1 < 1000000:
        R1 = round(R1, 2)
        R1 = str(R1/1000)
        R = R1 + ' ' + fourth() + ' ' + 'кОм'
    elif R1 > 999999 and R1 < 1000000000:
        R1 = round(R1, 2)
        R1 = str(R1/1000000)
        R = R1 + ' ' + fourth() + ' ' + 'МОм'
    elif R1 > 0 and R1 < 1000:
        R1 = round(R1, 2)
        R1 = str(R1)
        R = R1 + ' ' + fourth() + ' ' + 'Ом'
    if R is not None:
        lb1 = Label(window, text=R, font=("Arial Bold", 14))
        lb1.grid(column=4, row=8)

    current_calculation = f"Сопротивление: {R}\nКольца: {ring1.get()}, {ring2.get()}, {ring3.get()}\nМножитель: {multiplier.get()}\nТочность: {accuracy.get()}\n"
    calculation_history.append(current_calculation)
    if len(calculation_history) > max_size:
        calculation_history.pop(0)
    update_history_display()

def update_history_display():
    history_text.config(state=NORMAL)
    history_text.delete("1.0", END)
    for calculation in reversed(calculation_history):
      history_text.insert(END, calculation + "\n")
    history_text.config(state=DISABLED)

def Sbros():
    lb1 = Label(window, text='                                ', font=("Arial Bold", 14))
    lb1.grid(column=4, row=8)
    history_text.config(state=NORMAL)
    history_text.delete("1.0", END)
    history_text.config(state=DISABLED)
    calculation_history.clear()

window = Tk()
window.title("Расчет резистора")
window.geometry('1050x560')
window.configure(bg='lightblue')

lbl = Label(window, text="Расчет номинала резистора", bg = "lightblue", fg = "black",
font=("Arial Bold", 14))
lbl.grid(column=4, row=0)

lbl1 = Label(window, text="1 Кольцо",  bg = "lightblue", fg = "black",
font=("Arial Bold", 14))
lbl1.grid(column=1, row=4)

lbl2 = Label(window, text="2 Кольцо",  bg = "lightblue", fg = "black",
font=("Arial Bold", 14))
lbl2.grid(column=2, row=4)

lbl5 = Label(window, text="3 Кольцо",  bg = "lightblue", fg = "black",
font=("Arial Bold", 14))
lbl5.grid(column=3, row=4)

lbl3 = Label(window, text="Множитель",  bg = "lightblue", fg = "black",
font=("Arial Bold", 14))
lbl3.grid(column=5, row=4)

lbl4 = Label(window, text="Точность",   bg = "lightblue", fg = "black",
font=("Arial Bold", 14))
lbl4.grid(column=6, row=4)

ring1 = Combobox(window, state='readonly')
ring1['values'] = ('---', 'Коричневый', 'Красный', 'Оранжевый', 'Желтый', 'Зеленый', 'Синий', 'Фиолетовый', 'Серый', 'Белый')
ring1.current(0)
ring1.grid(column=1, row=5)

ring2 = Combobox(window, state='readonly')
ring2['values'] = ('---', 'Черный', 'Коричневый', 'Красный', 'Оранжевый', 'Желтый', 'Зеленый', 'Синий', 'Фиолетовый', 'Серый', 'Белый')
ring2.current(0)
ring2.grid(column=2, row=5)

ring3 = Combobox(window, state='readonly')
ring3['values'] = ('4-х полосный резистор', 'Коричневый', 'Красный', 'Оранжевый', 'Желтый', 'Зеленый', 'Синий', 'Фиолетовый', 'Серый', 'Белый')
ring3.current(0)
ring3.grid(column=3, row=5)

multiplier = Combobox(window, state='readonly')
multiplier['values'] = ('---', 'Черный', 'Коричневый', 'Красный', 'Оранжевый', 'Желтый', 'Зеленый', 'Синий', 'Фиолетовый', 'Золотой', 'Серебряный')
multiplier.current(0)
multiplier.grid(column=5, row=5)

accuracy = Combobox(window, state='readonly')
accuracy['values'] = ('---', 'Коричневый', 'Красный', 'Зеленый', 'Синий', 'Фиолетовый', 'Серый', 'Золотой', 'Серебряный')
accuracy.current(0)
accuracy.grid(column=6, row=5)

btn = Button(window, text="Посчитать:", bg="#63F25A", fg="black", font=("Arial", 11), command=Resist)
btn.grid(column=4, row=7)

btn = Button(window, text="Сбросить", bg="#F25A5A", fg="black", font=("Arial", 11), command=Sbros)
btn.grid(column=1, row=10)

history_text = Text(window, height=16, width=100, bg='white', wrap=WORD)
history_text.grid(column=1, row=12, columnspan=6, padx=10, pady=10)

history_text.config(state=NORMAL)
history_text.delete("1.0", END)
history_text.config(state=DISABLED)

scrollbar = Scrollbar(window, command=history_text.yview)
scrollbar.grid(column=7, row=12, sticky='ns')
history_text.config(yscrollcommand=scrollbar.set)

'''
image = PhotoImage(file="Res1.png")
image_label = Label(window, image=image, bg='lightblue')
image_label.grid(column=3, row=17)
'''

window.mainloop()
