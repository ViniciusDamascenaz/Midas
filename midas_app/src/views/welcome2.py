from flet import *

def welcome_page2(page: Page):
    

    return View(
        route="/welcome2",
        controls=[
            Stack([
                Container(
                    Column([
                        ProgressBar(1,bar_height=20, color="#a2a6fd", height=10),
                        Container(height=page.window.height/7),
                        
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