from flet import *
import json

def welcome_page1(page: Page):
    
    def prox_page(e):
        page.go("/welcome2")

    return View(
        route="/welcome1",
        controls=[
            Stack([
                Container(
                    Column([
                        ProgressBar(bar_height=20, color="#a2a6fd", height=10),
                        Container(height=page.window.height/7),
                        Text("Olá", size=75, color="black"),
                        Text("Bem vindo!", size=65, color="black"),
                        Container(height=page.window.height/7),
                        TextButton("Começar", width=250, height=90, style=ButtonStyle(color="black", bgcolor="#a2a6fd", side=BorderSide(2,"black"), text_style=TextStyle(size=17, weight=FontWeight.BOLD), overlay_color="#f7d78a"), on_click=prox_page)
                        
                    ],
                    horizontal_alignment=CrossAxisAlignment.CENTER
                    ),
                    bgcolor="#f8f7f2",
                    width=page.window.width,
                    height=page.window.height
                )
            ],
            width=page.window.width,
            height=page.window.height
            )
        ]
    )

