import flet as ft

from src.database import Database
from src.utils import view_pop

class NavigationDrawer(ft.NavigationDrawer):
    def __init__(self):
        super().__init__(
            on_change=self.on_change_navigation,
            controls=[
                ft.Container(height=12),
                ft.NavigationDrawerDestination(
                    label="Пользователь",
                    icon="account_circle" 
                ),
                ft.Divider(thickness=2),
                ft.NavigationDrawerDestination(
                    label="Настройки",
                    icon="settings"
                ),
                ft.NavigationDrawerDestination(
                    label="Выйти из аккаунта",
                    icon="close",
                ),
                ft.NavigationDrawerDestination(
                    label="Открыть консоль",
                    icon="code",
                ),
            ],
        )
    def exit_account(self,e:ft.ControlEvent = None):
        Database(e.page).set_username_password_in_client_storage("","")
        self.open = False
        self.update()
        view_pop(e)
        print('exit_account')
    def on_change_navigation(self, e:ft.ControlEvent = None):
        if e.data == "2":
            self.exit_account(e)