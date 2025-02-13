from flet import *
from system import dados

def welcome_page4(page: Page):

    def prox_page(e):
        page.go("/welcome1")

    return View(
        route="/welcome4",
        controls=[
            Stack([
                Container(
                    Column([
                        ProgressBar(0.75,bar_height=20, color="#a2a6fd", height=10),
                        Container(height=page.window.height/9),
                        Row([
                            Container(
                                    Column([
                                        Container(height=5),
                                        Row([Text("Saldos", color="black", size=25)], alignment=MainAxisAlignment.CENTER),
                                        
                                    ]),
                                    bgcolor="#a2a6fd",
                                    width=page.window.width/2 - 100,
                                    height=page.window.height - 300,
                                    border_radius=30,
                                    border=Border(top=BorderSide(2, "black"), left=BorderSide(2, "black"),bottom=BorderSide(2, "black"),right=BorderSide(2, "black"))
                                ),
                            Container(height=page.window.height/10),
                            Container(
                                    Column([
                                        Container(height=5),
                                        Row([Text("Cartões", color="black", size=25)], alignment=MainAxisAlignment.CENTER),
                                    ]),
                                    bgcolor="#a2a6fd",
                                    width=page.window.width/2 - 100,
                                    height=page.window.height - 300,
                                    border_radius=30,
                                    border=Border(top=BorderSide(2, "black"), left=BorderSide(2, "black"),bottom=BorderSide(2, "black"),right=BorderSide(2, "black"))
                                )
                        ], width=page.window.width, alignment=MainAxisAlignment.CENTER),
                        TextButton("Próximo", width=550, height=90, style=ButtonStyle(color="black", bgcolor="#a2a6fd", side=BorderSide(2,"black"), text_style=TextStyle(size=17, weight=FontWeight.BOLD), overlay_color="#f7d78a"), on_click=prox_page)
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

