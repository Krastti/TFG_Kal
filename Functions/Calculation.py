import main
import Functions.Selected as s
import tkinter as tk
from tkinter import messagebox

ALLOYS = {
    'Bismuth Bronze': {'Copper': 0.5, 'Zinc': 0.3, 'Bismuth': 0.2},
    'Black Bronze': {'Copper': 0.6, 'Silver': 0.2, 'Gold': 0.2},
    'Bronze': {'Copper': 0.9, 'Tin': 0.1},
    'Brass': {'Copper': 0.9, 'Zinc': 0.1},
    'Pink Gold': {'Copper': 0.3, 'Gold': 0.7},
    'Sterling Silver': {'Copper': 0.4, 'Silver': 0.6},
    'Black Steel': {'Steel': 0.6, 'Nickel': 0.2, 'Black Bronze': 0.2},
    'Blue Steel': {'Black Steel': 0.55, 'Bismuth Bronze': 0.1, 'Sterling Silver': 0.1, 'Steel': 0.25},
    'Red Steel': {'Black Steel': 0.55, 'Pink Gold': 0.1, 'Brass': 0.1, 'Steel': 0.25}
}

def get_amount(app_instance):
    try:
        if app_instance.third_label_ent['state'] == 'disabled':
            messagebox.showerror('Ошибка', 'Поле ввода отключено')
            return None

        input_value = app_instance.third_label_ent.get()

        if not input_value.strip():
            messagebox.showerror('Ошибка', 'Поле ввода не может быть пустым')
            return None
        if float(input_value) < 0:
            messagebox.showerror('Ошибка', 'Число должно быть положительным')
            return None
        if float(input_value) == 0:
            messagebox.showerror('Ошибка', 'Число не должно равняться нулю')
            return None

        return float(input_value)

    except (ValueError, TypeError):
        messagebox.showerror('Ошибка', 'Введите числовое значение')
        return None

def calculate_result(app_instance, amount):
    selectedAlloy = str(app_instance.box.get())

    components = ALLOYS[selectedAlloy]
    result_lines = [f'Состав {selectedAlloy} для {amount} слитков:']

    for material, ratio in components.items():
        required = amount * ratio
        result_lines.append(f'- {material}: {required:.2f} слитков')
    return '\n'.join(result_lines)

def show_result(app_instance):
    amount = get_amount(app_instance)

    result_text = calculate_result(app_instance, amount)

    if amount is not None:
        messagebox.showinfo('Результат', f'{result_text}')