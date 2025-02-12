from flet import *
import json
from system import dados

def welcome_page3(page: Page):
    

    nome = TextField(width=page.window.width/2 - 150, border_radius=60, text_style=TextStyle(color="black", size=20))
    email = TextField(width=page.window.width/2 - 150, border_radius=60, text_style=TextStyle(color="black", size=20))
    renda = TextField(width=page.window.width/2 - 150, border_radius=60, text_style=TextStyle(color="black", size=20),prefix_text="R$")
    ia = Checkbox(label="Sim, quero insights personalizados!", value=False, label_style=TextStyle(size=18, color="black"), overlay_color="#f7d78a", active_color="#f7d78a", shape=RoundedRectangleBorder(radius=5), height=35)


    def prox_page(e):
        print("foda")
        user = dados.Usuario()

        if nome.value == "":
            page.snack_bar = SnackBar(content=Text("Preencha todos os campos."),bgcolor="red",action="Ok!",duration=3000)
            page.snack_bar.open = True
            page.update()

        elif email.value == "":
            page.snack_bar = SnackBar(content=Text("Preencha todos os campos."),bgcolor="red",action="Ok!",duration=3000)
            page.snack_bar.open = True
            page.update()

        elif renda.value == "":
            page.snack_bar = SnackBar(content=Text("Preencha todos os campos."),bgcolor="red",action="Ok!",duration=3000)
            page.snack_bar.open = True
            page.update()
        else:
            user.adiciona_obj("renda", renda.value)
            user.adiciona_obj("nome", nome.value)
            user.adiciona_obj("email", email.value)
            if ia.value == True:
                user.adiciona_obj("ia", "True")
            else:
                user.adiciona_obj("ia", "False")
            page.go("/welcome1")


        

    return View(
        route="/welcome1",
        controls=[
            Stack([
                Container(
                    Column([
                        ProgressBar(0.4,bar_height=20, color="#a2a6fd", height=10),
                        Container(height=page.window.height/9),
                        Row([
                            Column([
                                #Container(height=page.window.height/20),
                                Row([
                                    Container(width=40),
                                    Column([
                                        Text("Como devemos chama-lo?", size=20, color="black", weight=FontWeight.BOLD),
                                        nome
                                    ])
                                ]),
                                Container(height=page.window.height/25),
                                Row([
                                    Container(width=40),
                                    Column([
                                        Text("Qual seu endereço de email?", size=20, color="black", weight=FontWeight.BOLD),
                                        email
                                    ])
                                ]),
                                Container(height=page.window.height/25),
                                Row([
                                    Container(width=40),
                                    Column([
                                        Text("Qual sua renda mensal?", size=20, color="black", weight=FontWeight.BOLD),
                                        renda
                                    ])
                                ]),
                                Container(height=page.window.height/25),
                                Row([
                                    Container(width=40),
                                    Column([
                                        Text("Quer usar inteligência artificial para melhorar sua experiência?", size=20, color="black", weight=FontWeight.BOLD),
                                        ia
                            
                                        
                                        
                                    ])
                                ]),
                                
                                
                                
                            ], horizontal_alignment=CrossAxisAlignment.START, width=page.window.width/2, height=page.window.height),

                            Column([
                                Text("Personalize sua experiência!", size=65, color="black", text_align=TextAlign.START, weight=FontWeight.BOLD),
                                Container(height=page.window.height/40),
                                Text("Para te oferecer insights personalizados, precisamos de algumas informações.", size=30, color="black", text_align=TextAlign.START),
                                Container(height=page.window.height/7),
                                
                                TextButton("Próximo", width=550, height=90, style=ButtonStyle(color="black", bgcolor="#a2a6fd", side=BorderSide(2,"black"), text_style=TextStyle(size=17, weight=FontWeight.BOLD), overlay_color="#f7d78a"), on_click=prox_page)
                                

                            ], horizontal_alignment=CrossAxisAlignment.START, width=page.window.width/2, height=page.window.height),
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
        ], scroll=ScrollMode.ADAPTIVE
    )