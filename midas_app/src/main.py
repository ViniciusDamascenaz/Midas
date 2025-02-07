import flet as ft


def main(page: ft.Page):
    page.window.width = 414
    page.window.height = 896
    page.adaptive = True
    page.title = "Gamefy"

    def route_change(route):
        page.views.clear()
        if page.route == "/home":
            pass
        
        page.update()
        

    page.on_route_change = route_change
    page.go("/home")
    page.update()
ft.app(target=main, assets_dir="./")