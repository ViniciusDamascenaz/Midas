from flet import *

def home_page(page: Page):

    return View(
        route="/home",
        controls=[
            Stack([
                Container(
                    Row([
                        Container(
                            Column([
                                Container(height=15),
                                Image("assets/logo_midasl.png",scale=0.8),
                                TextButton("Finanças"),
                                

                            ],
                            horizontal_alignment=CrossAxisAlignment.CENTER
                            ),
                            bgcolor="#2c2c2c",
                            height=page.window.height,
                            width=page.window.width/5
                        )
                    ]),
                    bgcolor="#f8f7f2",
                    width=page.window.width,
                    height=page.window.height,
                )
            ], 
            width=page.window.width,
            height=page.window.height,
            )
        ]
    )