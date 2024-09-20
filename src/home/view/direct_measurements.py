import flet as ft


class DirectMeasurementsView(ft.View):
    def __init__(self,page:ft.Page):
        super().__init__()
        self.page = page
        self.route = "/direct_measurements"

        self.appbar=ft.AppBar(
            title=ft.Text("Прямые измерения"),
        )