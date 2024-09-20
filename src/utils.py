import flet as ft

def on_change_obj(e:ft.ControlEvent):
    e.control.error_text = ""
    e.control.update()

def view_pop(e:ft.ViewPopEvent,*view):
    e.page.views.pop()
    top_view = e.page.views[-1]
    e.page.go(top_view.route)
    return top_view

class FrameCard(ft.Card):
    def __init__(self,obj):
        super().__init__(
            content=ft.Container(
                padding=10,
                content=obj
            )
        )

    