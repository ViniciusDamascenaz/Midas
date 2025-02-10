import flet as ft
from views import home
from views import welcome
from views import welcome2
from views import welcome3


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
        elif page.route == "/welcome1":
            page.views.append(welcome.welcome_page1(page))
        elif page.route == "/welcome2":
            page.views.append(welcome2.welcome_page2(page))
        elif page.route == "/welcome3":
            page.views.append(welcome3.welcome_page3(page))
        
        page.update()
        

    page.on_route_change = route_change
    page.go("/welcome3")
    page.update()
ft.app(target=main, assets_dir="./")