import flet as ft

from src.utils import FrameCard
from src.database import Database
from src.home.ui.sample_table import SampleTable
from src.home.ui.navigation_drawer import NavigationDrawer

class ExerciseReadDataRow(ft.DataRow):
    def __init__(self,id:int,title:str,annotation:str,rounds:list):

        self.title_row = ft.Ref[ft.DataCell]()
        self.annotation_row = ft.Ref[ft.DataCell]()
        self.rounds_row = ft.Ref[ft.DataCell]()


        self.cells = [
            ft.DataCell(ref=self.title_row,content=ft.Text(value=title)),
            ft.DataCell(ref=self.annotation_row,content=ft.Text("Да" if annotation else "Нет")),
            ft.DataCell(ref=self.rounds_row,content=ft.Text(f"{len(rounds)}")),
        ]
        super().__init__(
            cells=self.cells,
            on_long_press=lambda _: print(
                self.title_row.current.content.value,
                self.annotation_row.current.content.value,
                self.rounds_row.current.content.value,              
            )
        )

class ExerciseReadDataTable(ft.DataTable):
    def __init__(self,rows:list[ExerciseReadDataRow] = [],visible:bool=True):
        self.rows = rows
        super().__init__(
            visible=visible,
            rows=self.rows,
            columns=[
                ft.DataColumn(ft.Text("Название")),
                ft.DataColumn(ft.Text("Аннотация")),
                ft.DataColumn(ft.Text("Походы"), numeric=True),
            ],
        )
class HomeView(ft.View):
    def __init__(self,page:ft.Page):
        super().__init__(
            horizontal_alignment=ft.MainAxisAlignment.CENTER,         
            vertical_alignment=ft.MainAxisAlignment.CENTER,
        )

        self.page = page

        self.route = "/home"

        self.appbar=ft.AppBar(
            title=ft.Text("LabMath"),
            actions=[
                ft.PopupMenuButton(
                    items=[
                        ft.PopupMenuItem(text="Добавить выборку",icon="add",on_click=lambda _: self.page.go("/sample/create")),
                        ft.PopupMenuItem(text="Изменть выборку",icon="edit_note",on_click=lambda _: self.page.go("/sample/update")),
                        ft.PopupMenuItem(text="Удалить выборку",icon="delete",on_click=self.delete_sample),
                    ]
                )   
            ]
        )

        self.drawer = NavigationDrawer()

        self.lv = ft.ListView(
            expand=1,
        )
        self.controls = [self.lv]
        self.view_sample()

    def delete_sample(self,e:ft.ControlEvent=None):
        Database(self.page).sample = []
        self.view_sample(e)
        self.page.update()

    def view_sample(self,need_update:bool = False):
        self.lv.controls.clear()
        print(f"{Database(self.page).sample=}")
        if not Database(page=self.page).sample:
            self.lv.controls += [
                ft.Text("Чтобы начать добавьте выборку."),
                ft.FilledButton(
                    text="Добавить выборку",
                    icon="add",
                    on_click=lambda _: self.page.go("/sample/create")
                )
            ]
        else:
            self.lv.controls += [
                FrameCard(
                    ft.ExpansionTile(
                        title=ft.Text("Выборка данных"),
                        subtitle=ft.Text("Информация представлена в таблице",color="grey"),
                        leading=ft.Icon("assignment"),
                        affinity=ft.TileAffinity.PLATFORM,
                        controls=[
                            ft.Column(
                                controls=[
                                    SampleTable(Database(self.page).sample)
                                ]
                            )   
                        ]
                    )
                ),
                FrameCard(
                    ft.ExpansionTile(
                        title=ft.Text("Измерения"),
                        subtitle=ft.Text("В этом разделе представленно прямые и косвенные измерения",color="grey"),
                        leading=ft.Icon("analytics"),
                        affinity=ft.TileAffinity.PLATFORM,
                        controls=[
                            ft.Column(
                                controls=[
                                    ft.ListTile(
                                        title=ft.Text("Прямые измерения"),
                                        subtitle=ft.Text("В этом разделе прямые измерения показаны по каждой выборке ( по каждому столбцу )"),
                                        on_click=lambda _: self.page.go("/direct_measurements")
                                    ),
                                    ft.Divider(),
                                    ft.ListTile(
                                        title=ft.Text("Косвенные измерения"),
                                        subtitle=ft.Text("В этом разделе косвенные измерения показаны все вместе ( по каждому столбцу )"),
                                        on_click=lambda _: self.page.go("/indirect_measurements")
                                    )
                                ]
                            )
                        ]
                    )
                )
            ]
        if need_update:
            self.lv.update()