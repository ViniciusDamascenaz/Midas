from flet import *
import json

def welcome_page3(page: Page):
    
    def prox_page(e):
        page.go("/welcome2")

    return View(
        route="/welcome1",
        controls=[
            Stack([
                Container(
                    Column([
                        ProgressBar(0.2,bar_height=20, color="#a2a6fd", height=10),
                        Container(height=page.window.height/7),
                        Row([
                            Column([
                                
                                
                                
                            ], horizontal_alignment=CrossAxisAlignment.CENTER, width=page.window.width/2, height=page.window.height),

                            Column([
                                Text("Personalize sua experiência!", size=65, color="black", text_align=TextAlign.CENTER, weight=FontWeight.BOLD),
                                Container(height=page.window.height/40),
                                Text("Para te oferecer insights personalizados, precisamos de algumas informações.", size=30, color="black", text_align=TextAlign.CENTER),
                                Container(height=page.window.height/7),
                                TextButton("Próximo", width=250, height=90, style=ButtonStyle(color="black", bgcolor="#a2a6fd", side=BorderSide(2,"black"), text_style=TextStyle(size=17, weight=FontWeight.BOLD), overlay_color="#f7d78a"), on_click=prox_page)

                            ], horizontal_alignment=CrossAxisAlignment.CENTER, width=page.window.width/2, height=page.window.height),
                        ], width=page.window.width)
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