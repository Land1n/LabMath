import flet as ft

from src.utils import on_change_obj
from src.database import Database


class AuthView(ft.View):
    def __init__(self,page:ft.Page):
        super().__init__(
            horizontal_alignment=ft.MainAxisAlignment.CENTER,         
            vertical_alignment=ft.MainAxisAlignment.CENTER,
        )

        self.page = page

        self.route = "/auth"

        self.user_name_tf = ft.Ref[ft.TextField]()
        self.user_password_tf = ft.Ref[ft.TextField]()

        title = "Авторизация"

        self.controls = [
            ft.Card(
                content=ft.Container(
                    padding=15,
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text(title,size=20),
                            ft.TextField(
                                ref=self.user_name_tf,
                                label="Логин",
                                icon="account_circle",
                                on_change=on_change_obj,
                            ),
                            ft.TextField(
                                ref=self.user_password_tf,
                                label="Пароль",
                                icon="lock",
                                password=True,
                                can_reveal_password=True,
                                on_change=on_change_obj,
                            ),
                            ft.CupertinoButton(
                                content=ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[ft.Text(title)]
                                ),
                                bgcolor=ft.colors.PRIMARY,
                                opacity_on_click=0.3,
                                on_click=self.log_in,
                            ),
                        ]
                    )
                )    
            )
            
        ]
        database = Database(self.page) 
        if database.log_in(*database.get_username_password_in_client_storage()):
            self.page.go("/home")
    def log_in(self,e:ft.ControlEvent):
        if not self.user_name_tf.current.value: 
            self.user_name_tf.current.error_text = "Это поле обязательно"
            self.user_name_tf.current.update()
        if not self.user_password_tf.current.value: 
            self.user_password_tf.current.error_text = "Это поле обязательно"
            self.user_password_tf.current.update()
            
        if self.user_password_tf.current.value and self.user_name_tf.current.value:
            database = Database(self.page) 
            if database.log_in(self.user_name_tf.current.value,self.user_password_tf.current.value):
                database.set_username_password_in_client_storage(self.user_name_tf.current.value,self.user_password_tf.current.value)
                self.page.go("/home")
            else:
                self.user_name_tf.current.error_text = "Неверный логин или пароль"
                self.user_password_tf.current.update()