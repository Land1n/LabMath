import flet as ft

from src.utils import on_change_obj

class AuthView(ft.View):
    def __init__(self,page:ft.Page):
        super().__init__(
            padding=ft.Padding(0,100,0,0),
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,         
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
                        width=.3*self.page.width,
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
    def log_in(self,e:ft.ControlEvent):
        if not self.user_name_tf.current.value: 
            self.user_name_tf.current.error_text = "Это поле обязательно"
            self.user_name_tf.current.update()
        if not self.user_password_tf.current.value: 
            self.user_password_tf.current.error_text = "Это поле обязательно"
            self.user_password_tf.current.update()
            
        if self.user_password_tf.current.value and self.user_name_tf.current.value:
            ...