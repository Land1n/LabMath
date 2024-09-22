import flet as ft

from src.utils import FrameCard,ImportantInformationCard
from src.shemes import DataSample
from src.database import Database

class DirectMeasurementsView(ft.View):
    def __init__(self,page:ft.Page):
        super().__init__()
        self.page = page
        self.route = "/direct_measurements"

        self.appbar=ft.AppBar(
            title=ft.Text("Прямые измерения"),
        )

        self.controls=[
            ft.Text('Список выборок:',size=15),
            ImportantInformationCard("Устраните из выборки очевидные промахи (описки)"),
            ft.Divider()
        ]
        for sample in Database(self.page).sample:
            self.view_sample(sample)
    def view_sample(self,sample:DataSample):
        sample = DataSample(**sample)
        self.controls += [
            FrameCard(
                leading=ft.Icon('insert_chart_outlined'),
                title=ft.Text(f"Выборка: {len(self.controls)-2}", size=15, weight=ft.FontWeight.BOLD),
                control=ft.ExpansionTile(
                    title=ft.Text(f"Выборка: {len(self.controls)-2}"),
                    controls=[
                        ft.Text(
                            "xi+1–xi < UP,N R"
                        )
                    ]
                )
            )
        ]
    