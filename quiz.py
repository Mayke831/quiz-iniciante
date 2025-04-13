def boas_vindas():
    print("Bem-vindo ao Quiz da Sabedoria!")
    print("Responda as perguntas abaixo digitando a letra da alternativa correta.\n")

def fazer_pergunta(pergunta, opcoes, resposta_correta):
    print(pergunta)
    for opcao in opcoes:
        print(opcao)
    resposta = input("Sua resposta: ").strip().upper()

    if resposta == resposta_correta:
        print("✅ Resposta correta!\n")
        return True
    else:
        print(f"❌ Resposta errada! A resposta certa era: {resposta_correta}\n")
        return False

def jogar_quiz():
    pontuacao = 0
    total_perguntas = 4

    perguntas = [
        {
            "pergunta": "Quantas cores tem o arco-íris?",
            "opcoes": ["A) 5", "B) 3", "C) 8", "D) 7"],
            "resposta": "D"
        },
        {
            "pergunta": "Qual é o planeta mais próximo do Sol?",
            "opcoes": ["A) Marte", "B) Terra", "C) Mercúrio", "D) Vênus"],
            "resposta": "C"
        },
        {
            "pergunta": "Quem pintou a Mona Lisa?",
            "opcoes": ["A) Van Gogh", "B) Michelangelo", "C) Leonardo da Vinci", "D) Picasso"],
            "resposta": "C"
        },

        {
            "pergunta": "Qual é a floresta tropical mais extensa do mundo?",
            "opcoes": ["A) Floresta Amazônica", "B) Floresta Negra", "C) Floresta do Congo", "D) Florestra Brasileira"],
            "resposta": "A"
        }
    ]

    for pergunta in perguntas:
        if fazer_pergunta(pergunta["pergunta"], pergunta["opcoes"], pergunta["resposta"]):
            pontuacao += 1

    print(f"FIM DE JOGO ! Sua pontuação final foi: {pontuacao}/{total_perguntas}")

if __name__ == "__main__":
    boas_vindas()
    jogar_quiz()
