import flet as ft
from views import home


def main(page: ft.Page):
    page.window.width = 1366
    page.window.height = 768
    page.window.maximized = True
    page.bgcolor = "#2c2c2c"
    page.adaptive = True
    page.title = "Midas"

    def route_change(route):
        page.views.clear()
        if page.route == "/home":
            page.views.append(home.home_page(page))
        
        page.update()
        

    page.on_route_change = route_change
    page.go("/home")
    page.update()
ft.app(target=main, assets_dir="./")