import flet as ft

def on_change_obj(e:ft.ControlEvent):
    e.control.error_text = ""
    e.control.update()
