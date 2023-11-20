import tkinter as tk
from tkinter import messagebox

class QuizGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulario dos golpes")

        self.quiz = Quiz()

        self.label_bem_vindo = tk.Label(
            root,
            text="Bem-vindo ao teste de confiabilidade de sua compra!\nVocê está respondendo antes ou depois da compra?",
            font=("Helvetica", 16)
        )
        self.label_bem_vindo.pack(pady=10)

        self.botao_antes = tk.Button(root, text="Antes", command=lambda: self.iniciar_quiz(self.quiz.perguntas_antes))
        self.botao_antes.pack(pady=5)

        self.botao_depois = tk.Button(root, text="Depois", command=lambda: self.iniciar_quiz(self.quiz.perguntas_depois))
        self.botao_depois.pack(pady=5)

        self.label_pontuacao = tk.Label(root, text="")
        self.label_pontuacao.pack(pady=10)

        self.explicacoes_corretas = []  

    def iniciar_quiz(self, perguntas):
        self.label_bem_vindo.pack_forget()  
        self.label_pontuacao.config(text="")  
        self.explicacoes_corretas = []  

        for pergunta, alternativa_correta, pontuacao, explicacao in perguntas:
            resposta = self.criar_janela_pergunta(pergunta)
            if resposta.lower() == alternativa_correta.lower():
                self.quiz.pontos += pontuacao
            else:
                self.explicacoes_corretas.append(explicacao)

        self.mostrar_pontuacao()

    def criar_janela_pergunta(self, pergunta):
        resposta_var = tk.StringVar()

        janela_pergunta = tk.Toplevel(self.root)
        janela_pergunta.title("Perguntas")

        label_pergunta = tk.Label(janela_pergunta, text=pergunta, font=("Helvetica", 12), pady=10)
        label_pergunta.pack()

        opcao_sim = tk.Radiobutton(janela_pergunta, text="Sim", variable=resposta_var, value="sim")
        opcao_sim.pack()
        opcao_nao = tk.Radiobutton(janela_pergunta, text="Não", variable=resposta_var, value="nao")
        opcao_nao.pack()

        botao_responder = tk.Button(janela_pergunta, text="Responder", command=lambda: janela_pergunta.destroy())
        botao_responder.pack()

        janela_pergunta.wait_window()

        return resposta_var.get()

    def mostrar_pontuacao(self):
        mensagem = "De 0 a 10 sua avaliação final é: {}".format(self.quiz.pontos)

        janela_resultado = tk.Toplevel(self.root)
        janela_resultado.title("Resultado Final")

        label_mensagem = tk.Label(janela_resultado, text=mensagem, font=("Helvetica", 14), pady=10)
        label_mensagem.pack()

        botao_fechar = tk.Button(janela_resultado, text="Fechar", command=janela_resultado.destroy)
        botao_fechar.pack()

        self.mostrar_explicacoes()

    def mostrar_explicacoes(self):
        if self.explicacoes_corretas:
            mensagem = "Abaixo alguns avisos/sugestões:\n{}".format("\n".join(self.explicacoes_corretas))
            messagebox.showinfo("Ultima Janela", mensagem)
        self.resetar_interface()

    def resetar_interface(self):
        self.label_bem_vindo.pack()
        self.label_pontuacao.config(text="")
        self.quiz.resetar_pontuacao()

class Quiz:
    def __init__(self):
        self.pontos = 0

        self.perguntas_antes = [
            (
                "Você reconhece o vendedor ou site de onde está fazendo a compra?",
                "Sim",
                0.66,
                "\n -Se reconhecer, é um sinal positivo de confiabilidade."
            ),
            (
                "A oferta parece boa demais para ser verdade?",
                "Nao",
                0.66,
                "\n -Ofertas muito boas podem ser suspeitas."
            ),
            (
                "O site possui um certificado de segurança (SSL) para proteger seus dados?",
                "Sim",
                0.66,
                "\n -Certificado SSL é essencial para segurança."
            ),
            (
                "O vendedor solicita informações pessoais excessivas ou sensíveis?",
                "Nao",
                0.66,
                "\n -Evite compartilhar informações excessivas."
            ),
            (
                "Você verificou as avaliações e comentários de outros compradores sobre o vendedor ou site?",
                "Sim",
                0.66,
                "\n -Verifique para validar a confiabilidade."
            ),
            (
                "A política de devolução e reembolso é clara e justa?",
                "Sim",
                0.66,
                "\n -Política clara é um bom sinal."
            ),
            (
                "Você recebeu um email suspeito ou mensagem de texto sobre a compra?",
                "Nao",
                0.66,
                "\n -Emails suspeitos são sinais de fraude."
            ),
            (
                "O site pede que você pague usando métodos de pagamento não convencionais?",
                "Nao",
                0.66,
                "\n -Evite métodos incomuns de pagamento."
            ),
            (
              "Você confirmou os detalhes do produto, tipo preço, tamanho, cor, etc.?",
                "Sim",
                0.66,
                "\n -Confirme para evitar erros."
            ),
            (
                "Você recebeu um código de autenticação de dois fatores para a compra?",
                "Sim",
                0.66,
                "\n -Autenticação de dois fatores é seguro."
            ),
            (
                "O site oferece suporte ao cliente e informações de contato claras?",
                "Sim",
                0.66,
                "\n -Suporte claro é importante."
            ),
            (
                "Você está usando uma conexão de internet segura ao fazer a compra?",
                "Sim",
                0.66,
                "\n -Use conexão segura."
            ),
            (
                "O site fornece informações sobre a política de privacidade?",
                "Sim",
                0.66,
                "\n -Privacidade é importante."
            ),
            (
                "A transação inclui custos inesperados ou taxas ocultas?",
                "Nao",
                0.66,
                "\n -Custos ocultos são um problema."
            ),
            (
                "Você já fez pesquisas adicionais sobre a loja ou vendedor para garantir sua legitimidade?",
                "Sim",
                0.66,
                "\n -Pesquisa adiciona segurança."
            ),
        ]

        self.perguntas_depois = [
            (
                "Você recebeu uma confirmação da compra por email ou mensagem de texto?",
                "Sim",
                0.66,
                "\n -Confirmação é importante."
            ),
            (
                "O produto ou serviço foi entregue conforme prometido?",
                "Sim",
                0.66,
                "\n -Receber o que foi prometido é positivo."
            ),
            (
                "O produto é autêntico e de qualidade?",
                "Sim",
                0.66,
                "\n -Receber produto genuíno é positivo."
            ),
            (
                "Verificou novamente a política de devolução e reembolso em caso de problemas?",
                "Sim",
                0.66,
                "\n -Saiba sobre política em caso de problemas."
            ),
            (
                "Entrou em contato com o vendedor ou loja imediatamente se houver algum problema?",
                "Sim",
                0.66,
                "\n -Comunique problemas proativamente."
            ),
            (
                "Mantém registros detalhados da transação, incluindo emails de confirmação e recibos?",
                "Sim",
                0.66,
                "\n -Registros são importantes."
            ),
            (
                "Relatou a transação à sua instituição financeira se suspeitar de fraude?",
                "Sim",
                0.66,
                "\n -Relatar suspeita de fraude é importante."
            ),
            (
                "Verificou se o site ou vendedor está associado a uma organização de proteção ao consumidor?",
                "Sim",
                0.66,
                "\n -Verificar associações é uma boa prática."
            ),
            (
                "Avaliou sua experiência com o vendedor e deixou feedback se aplicável?",
                "Sim",
                0.66,
                "\n -Feedback ajuda outros compradores."
            ),
            (
                "Fez uma revisão final das informações da compra antes de finalizar a transação?",
                "Sim",
                0.66,
                "\n -Revisar é importante para evitar erros."
            ),
            (
                "Mantém um olho atento a e-mails de phishing ou tentativas de golpes após a compra?",
                "Nao",
                0.66,
                "\n -Esteja atento a golpes pós-compra."
            ),
            (
                "Verificou sua fatura de cartão de crédito ou extrato bancário para garantir que a cobrança seja legítima?",
                "Sim",
                0.66,
                "\n -Verificar a fatura é uma prática segura."
            ),
            (
                "Observou atividades suspeitas em sua conta ou cartão de crédito após a compra?",
                "Nao",
                0.66,
                "\n -Atividades suspeitas requerem atenção."
            ),
            (
                "Compartilhou informações pessoais adicionais com o vendedor após a compra?",
                "Nao",
                0.66,
                "\n -Evite compartilhar informações adicionais."
            ),
            (
                "Recebeu solicitações de pagamento adicionais após a compra?",
                "Nao",
                0.66,
                "\n -Cuidado com solicitações de pagamento adicionais."
            ),
        ]

    def resetar_pontuacao(self):
        self.pontos = 0

if __name__ == "__main__":
    root = tk.Tk(className="Quiz")
    app = QuizGUI(root)
    root.mainloop()