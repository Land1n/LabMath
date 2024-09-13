import flet as ft

class HomeView(ft.View):
    def __init__(self,page:ft.Page):
        super().__init__()

        self.page = page

        self.route = "/home"