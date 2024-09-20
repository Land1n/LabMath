import flet as ft


class IndirectMeasurementsView(ft.View):
    def __init__(self,page:ft.Page):
        super().__init__()
        self.page = page
        self.route = "/indirect_measurements"

        self.appbar=ft.AppBar(
            title=ft.Text("Косвенный измерения"),
        )