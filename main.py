import flet as ft

from src.router import Router

from flet_core import theme

from src.utils import view_pop


def main(page:ft.Page):
    page.title = 'LabMath'
    router = Router(page)
    page.on_route_change = router.route_change
    page.views.clear()

    page.theme_mode = "light"
    page.theme = theme.Theme(color_scheme_seed="green")
    page.on_view_pop = view_pop
    page.go("/auth") 


if __name__ == '__main__':
    ft.app(main)