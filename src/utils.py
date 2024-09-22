import flet as ft

from src.shemes import TypeClassicalButton

class ConsolePanel(ft.AlertDialog):
    def __init__(self,page:ft.Page):
        self.page = page
        super().__init__(
            title=ft.Text("Консоль"),
            content=ft.TextField(),
            actions=[
                ft.FilledButton(
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.Text('Sibmit')
                        ] 
                    )
                )
            ]
        )

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

class ClassicalButton:
    obj = []
    def change_btn_style(self,type:TypeClassicalButton=TypeClassicalButton.NORMAL,e:ft.ControlEvent=None):
        for control in self.obj:
            if type == TypeClassicalButton.NORMAL:
                control.color = ""
            elif type == TypeClassicalButton.ERROR:
                control.color = "red200"
            control.update()

class ClassicalTextButton(ft.TextButton,ClassicalButton):
    def __init__(self,obj:list[ft.Control] = None,text:str="",icon:str="",visible=True,on_click=None,ref:ft.Ref=None) -> None:
        self.obj = []

        if icon:
            self.obj += [ft.Icon(icon)]
        
        if text:
            self.obj += [ft.Text(text)]

        if isinstance(obj,list):
            self.obj = obj
        super().__init__(
            ref=ref,
            visible=visible,
            on_click=on_click,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=self.obj 
            )
        )
