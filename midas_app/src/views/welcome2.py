from flet import *
import json
from system import dados

def welcome_page2(page: Page):

    economia = Checkbox(label="Quero Economizar", value=False, label_style=TextStyle(size=30, color="black"), overlay_color="#f7d78a", active_color="#f7d78a", shape=RoundedRectangleBorder(radius=5), height=100)
    investir = Checkbox(label="Quero Invertir", value=False, label_style=TextStyle(size=30, color="black"), overlay_color="#f7d78a", active_color="#f7d78a", shape=RoundedRectangleBorder(radius=5), height=100)
    gastos = Checkbox(label="Quero controlar meus gastos", value=False, label_style=TextStyle(size=30, color="black"), overlay_color="#f7d78a", active_color="#f7d78a", shape=RoundedRectangleBorder(radius=5), height=100)  
    dividas = Checkbox(label="Quero quitar dívidas", value=False, label_style=TextStyle(size=30, color="black"), overlay_color="#f7d78a", active_color="#f7d78a", shape=RoundedRectangleBorder(radius=5), height=100)

    def prox_page(e):
        objetivo = []
        if economia.value == True:
            objetivo.append("Economizar")
        if investir.value == True:
            objetivo.append("Investir")
        if gastos.value == True:
            objetivo.append("Gastos")
        if dividas.value == True:
            objetivo.append("Dividas")
        user = dados.Usuario()
        user.adiciona_obj("objetivo", objetivo)
        page.go("/welcome3")

    return View(
        route="/welcome2",
        controls=[
            Stack([
                Container(
                    Column([
                        ProgressBar(0.2,bar_height=20, color="#a2a6fd", height=10),
                        Container(height=page.window.height/7),
                        Row([
                            Column([
                                Text("Qual o seu objetivo financeiro?", size=65, color="black", text_align=TextAlign.CENTER, weight=FontWeight.BOLD),
                                Container(height=page.window.height/40),
                                Text("Para personalizar sua experiência, queremos entender suas metas.", size=30, color="black", text_align=TextAlign.CENTER),
                                Container(height=page.window.height/7),
                                TextButton("Próximo", width=250, height=90, style=ButtonStyle(color="black", bgcolor="#a2a6fd", side=BorderSide(2,"black"), text_style=TextStyle(size=17, weight=FontWeight.BOLD), overlay_color="#f7d78a"), on_click=prox_page)
                                
                                
                            ], horizontal_alignment=CrossAxisAlignment.CENTER, width=page.window.width/2, height=page.window.height),

                            Column([
                                Row([
                                    Container(width=page.window.width/10),
                                    economia
                                ]),
                                Row([
                                    Container(width=page.window.width/10),
                                    investir
                                ]),
                                Row([
                                    Container(width=page.window.width/10),
                                    gastos
                                ]),
                                Row([
                                    Container(width=page.window.width/10),
                                    dividas
                                ]),

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