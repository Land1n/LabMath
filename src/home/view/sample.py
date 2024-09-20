import flet as ft
from flet_core import colors

from repath import match

from src.utils import on_change_obj,view_pop
from src.home.ui.mini_column_card import MiniColumnCard
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
    def __init__(self,page:ft.Page,sample_data={}):
        super().__init__()

        self.page = page
        self.type = match("/sample/:type",self.page.route).groupdict()["type"]

        self.route = f"/sample/{self.type}"

        self.type_settings = {
            "create":{
                "info":True,
                "title":"Добавить выборку",
                "icon":"add",
                "func_main_btn":self.create_sample
            },
            "update":{
                "info":False,
                "title":"Изменть выборку",
                "icon":"edit_note",
                "func_main_btn":self.update_sample
            }
        }

        self.appbar = ft.AppBar(
            title=ft.Text(self.type_settings.get(self.type,None)["title"]),
        )

        self.column_with_tf = ft.ListView(expand=1)

        self.column_dd = self.MyDropdown(
            f"Количество\nстолбцов",self.on_change_dd
        )  
        self.row_dd = self.MyDropdown(
            "Количесто\nстрок",self.on_change_dd
        )      

        self.controls=[
            ft.ResponsiveRow(
                col=2,
                controls=[
                    self.column_dd,
                    self.row_dd,
                    ft.Container(
                        col={"md": 4,"xs": 4},  
                        border_radius=3,    
                        height=55,          
                        on_click=self.type_settings.get(self.type,None)["func_main_btn"],        
                        bgcolor=colors.PRIMARY,
                        content=ft.Icon(self.type_settings.get(self.type,None)["icon"],color="white")
                    )
                ]
            ),
            ft.Divider(),
            ft.Card(
                visible=self.type_settings.get(self.type,None)["info"],
                content=ft.ListTile(
                    leading=ft.Icon("info"),
                    title=ft.Text("Важная информация"),
                    subtitle=ft.Text('Столбцы - название выборки (Пример: m, кг.),\nСтроки - элементы выборки (№: 1, 2, ..., n)'),
                )
            ),
            ft.Text(
                value="Список столбцов:",
                size=20,
                weight=ft.FontWeight.BOLD
            ),
            self.column_with_tf
        ]

    def on_change_dd(self,e:ft.ControlEvent=None):
        on_change_obj(e)
        self.column_with_tf.controls.clear()
        
        for i in range(1,int(self.column_dd.value)+1):
            self.column_with_tf.controls += [MiniColumnCard(int(self.row_dd.value),i)]
        self.column_with_tf.update()
    def check_field(self,e:ft.ControlEvent=None):
        text = "Это поле обязательно"
        for tf in self.column_with_tf.controls:
            if not tf.value:
                tf.symbol.error_text = text
                tf.name.error_text = text
                tf.device_error.error_text = text
                tf.update()
        if not self.column_dd.value:
            self.column_dd.error_text = text
            self.column_dd.update()
        if not self.row_dd.value:
            self.row_dd.error_text = text
            self.row_dd.update()
        if all([tf.value for tf in self.column_with_tf.controls]) and self.row_dd.value and self.column_dd.value:
            return True
        else:
            return False
    def create_sample(self,e:ft.ControlEvent=None):
        if not self.check_field():
            return False  
        database = Database(page=self.page)    
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
        last_view = view_pop(e)    
        print("update_sample")