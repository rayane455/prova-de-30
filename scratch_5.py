class Cliente:
    def __init__(self,nome,cpf,rendamensal,scoreCredito):
        self.nome = nome
        self.cpf = cpf
        self.rendamensal = rendamensal
        self.scoreCredito = scoreCredito

    def verificar_credito(self):
        print(f"olá, minha renda mensal é {self.rendamensal} e meu score-crédito é {self.scoreCredito}.")
        if self.rendamensal >= 2000 and self.scoreCredito >= 600:
            print(f"Cliente {self.nome}: Crédito aprovado para a concessão de compras.")
        else:
            print(f"Cliente {self.nome}: Crédito negado.")


cliente1 = Cliente("Julia", 50011908744, 4000, 700)
cliente2 = Cliente("Richard", 70088906722, 4000, 500)
cliente3 = Cliente("Marina", 80099804211, 1500, 800)

cliente1.verificar_credito()
cliente2.verificar_credito()
cliente3.verificar_credito()