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
            "metas_financeiras": {}
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

    def adiciona_obj(self, chave, valor):
        if chave in self.dados:
            self.dados[chave] = valor
            with open(self.arquivo, "w", encoding="utf-8") as f:
                json.dump(self.dados, f, indent=4, ensure_ascii=False)
            return f"{chave} atualizado para {valor}"
        else:
            return f"Chave '{chave}' não encontrada."

