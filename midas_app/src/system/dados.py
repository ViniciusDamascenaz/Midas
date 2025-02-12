import json

class Usuario:
    def __init__(self):
        self.arquivo = "usuario.json"
        self.dados = {
            "nome": "",
            "email": "",
            "objetivo": "",
            "renda": "",
            "saldo_atual": 0.0,
            "cartoes": {},
            "gastos": {},
            "receitas": {},
            "orçamento": {},
            "investimentos": {},
            "metas_financeiras": {},
            "ia": "False",
            "new_user": "True"
        }
        try:
            with open("usuario.json", "r", encoding="utf-8") as arquivo:
                self.usuario = json.load(arquivo)  
        except FileNotFoundError:
            with open("usuario.json", "w", encoding="utf-8") as arquivo:
                json.dump(self.dados, arquivo, indent=4, ensure_ascii=False)
                arquivo.close()
            with open("usuario.json", "r", encoding="utf-8") as arquivo:
                self.usuario = json.load(arquivo)

    def recarrega(self):
        try:
            with open("usuario.json", "r", encoding="utf-8") as arquivo:
                self.usuario = json.load(arquivo)  
        except FileNotFoundError:
            with open("usuario.json", "w", encoding="utf-8") as arquivo:
                json.dump(self.dados, arquivo, indent=4, ensure_ascii=False)
                arquivo.close()
            with open("usuario.json", "r", encoding="utf-8") as arquivo:
                self.usuario = json.load(arquivo)

    def adiciona_obj(self, chave, valor):
        self.recarrega()
        if chave in self.usuario:
            self.usuario[chave] = valor
            with open(self.arquivo, "w", encoding="utf-8") as f:
                json.dump(self.usuario, f, indent=4, ensure_ascii=False)
            return f"{chave} atualizado para {valor}"
        else:
            return f"Chave '{chave}' não encontrada."
        
    def new_user(self):
        self.recarrega()
        
        if self.usuario["new_user"] == "True":
            return True
        else: 
            return False
        


