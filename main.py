import flet as ft

from src.router import Router


def main(page:ft.Page):
    page.title = 'ZAL'
    router = Router(page)
    page.on_route_change = router.route_change
    page.views.clear()
    page.go("/auth") 


if __name__ == '__main__':
    ft.app(main)