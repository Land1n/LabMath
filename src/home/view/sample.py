import flet as ft
from flet_core import colors

from repath import match

from src.utils import on_change_obj,view_pop, ImportantInformationCard
from src.home.ui.sample_card import SampleCard
from src.database import Database


class SampleView(ft.View):
    class MyDropdown(ft.Dropdown):
        def __init__(self,text:str,on_change_dd):
            super().__init__(
                label=text,
                hint_style=ft.TextStyle(size=11),
                col={"md": 4,"xs": 4},
                height=80,
                label_style=ft.TextStyle(size=13),
                on_change=on_change_dd,
                options=[ft.dropdown.Option(str(i)) for i in range(1,11)]
            )
    def __init__(self,page:ft.Page):
        super().__init__()

        self.page = page
        self.type = match("/sample/:type",self.page.route).groupdict()["type"]
        
        self.route = f"/sample/{self.type}"

        self.type_settings = {
            "create":{
                "info":True,
                "title":"Выборка",
                "icon":"add",
                "func_main_btn":self.create_sample
            },
            "update":{
                "info":False,
                "title":"Выборка",
                "icon":"edit_note",
                "func_main_btn":self.update_sample
            }
        }


        self.appbar = ft.AppBar(
            title=ft.Text(self.type_settings.get(self.type,None)["title"]),
            title_text_style=ft.TextStyle(size=16,color="black"),
            actions=[
                ft.Container(
                    padding=5,
                    content=ft.Row(
                        spacing=5,
                        controls=[
                            ft.IconButton(
                                icon='addchart',
                                on_click=self.add_sample,
                                tooltip="Add data selection element",
                            ),
                            ft.FilledButton(
                                text="Добавить выборку",
                                icon="add",
                                on_click=self.type_settings.get(self.type,None)["func_main_btn"],
                                style=ft.ButtonStyle(
                                    color="white",
                                    bgcolor=colors.PRIMARY,
                                ),
                                tooltip="Add data sampling",
                            )
                        ]
                    )
                )
            ]
        )

        self.column_with_tf = ft.ListView(
            expand=1,
        )

        self.controls=[
            ImportantInformationCard('Важно заполнять поля правильно эти данные будут использоваться в косвенных измерениях',visible=self.type_settings.get(self.type,None)["info"]),
            ft.Divider(),
            self.column_with_tf,
    
        ]

        if self.type == "update":
            for i,data in enumerate(Database(self.page).sample):
                self.column_with_tf.controls += [SampleCard(i+1,data)]

    def add_sample(self,e:ft.ControlEvent=None,data:dict={}):
        self.column_with_tf.controls.clear()
        self.column_with_tf.controls += [SampleCard(len(self.column_with_tf.controls)+1,data)]
        self.column_with_tf.update()
    def check_field(self,e:ft.ControlEvent=None):
        text = "Это поле обязательно"
        for tf in self.column_with_tf.controls:
            if not tf.value:
                tf.symbol.error_text = text
                tf.name.error_text = text
                tf.device_error.error_text = text
                tf.update()
        if all([tf.value for tf in self.column_with_tf.controls]):
            return True
        else:
            return False

    def create_sample(self,e:ft.ControlEvent=None):
        if not self.check_field():
            return False  
        last_sample = Database(page=self.page).sample
        temp_list = []
        for tf in self.column_with_tf.controls:
            temp_list += [
                tf.value
            ]
        sample = last_sample + temp_list
        Database(page=self.page).sample = sample
        view_pop(e).view_sample(need_update=True)

    def update_sample(self,e:ft.ControlEvent=None):
        if not self.check_field():
            return False
        temp_list = []
        for tf in self.column_with_tf.controls:
            temp_list += [
                tf.value
            ]
        Database(page=self.page).sample = temp_list
        view_pop(e).view_sample(need_update=True)
