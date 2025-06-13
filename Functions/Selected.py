import main

def selected(event, app_instance):
    selection = app_instance.box.get()
    app_instance.second_label.config(text=f'Вы хотите сделать: {selection}')
    app_instance.third_label_ent.config(state='normal')
    app_instance.third_label_ent.focus()
    app_instance.third_label_ent.delete(0, 'end')
    return selection
