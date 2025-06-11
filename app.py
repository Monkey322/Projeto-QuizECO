#Bibliotecas utilizadas 
import random
import os
import time

#classe de usuario
class Usuario:
  def __init__(self, nome, email, idade, cidade):
    self.nome = nome
    self.email = email
    self.idade = idade
    self.cidade = cidade

  #metodo para exibir dados do usuario
  def exibir_dados(self):
    print("NOME: " + self.nome)
    print("EMAIL: " + self.email)
    print("IDADE: " + str(self.idade))
    print("CIDADE: " + self.cidade)

#função para limpar console
def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

#função para cadastro
def cadastro():
  clear()
  nome = input("Digite seu nome: ")
  email = input("Digite seu e-mail: ")

#Laço infinito até o usuario inserir uma idade correta
  while True:
    try:
      idade = int(input("Digite sua idade: "))
      break
    #exceção para avisar a o usuario do valor invalido
    except ValueError:
      print("Por favor, digite um número válido para a idade.")

  cidade = input("Digite sua cidade: ")
  return Usuario(nome, email, idade, cidade)

#função para exibir o menu
def print_menu():
  clear()
  print("\n================== MENU ==================\n")
  print("1 - Cadastro de Usuário")
  print("2 - Exibir Usuário")
  print("3 - Jogar")
  print("0 - Sair")
  print("==========================================")

#função do jogo
def jogo_educativo(usuario):
  clear()
  print("\n=== QUIZECO - JOGO EDUCATIVO SOBRE SUSTENTABILIDADE ===\n")
  print(f"Bem-vindo(a), {usuario.nome}!")
  
  #lista de perguntas
  perguntas = [
    {
      "tipo": "vf",
      "pergunta": "Reciclar papel ajuda a salvar árvores.",
      "resposta": True,
      "curiosidade": "Você sabia que uma tonelada de papel reciclado pode salvar até 20 árvores?"
    },
    {
      "tipo": "vf",
      "pergunta": "Energia solar é uma fonte de energia poluente.",
      "resposta": False,
      "curiosidade": "Você sabia que a energia solar é limpa, renovável e abundante?"
    },
    {
      "tipo": "multipla",
      "pergunta": "Qual destas práticas ajuda a economizar água?",
      "opcoes": ["Deixar a torneira aberta", "Tomar banhos longos", "Usar vassoura para limpar a calçada", "Lavar o carro todos os dias"],
      "resposta": 2,
      "curiosidade": "Usar a vassoura em vez da mangueira pode economizar até 280 litros de água por vez."
    },
    {
      "tipo": "multipla",
      "pergunta": "Qual material pode ser reciclado infinitamente sem perder qualidade?",
      "opcoes": ["Plástico", "Papel", "Vidro", "Isopor"],
      "resposta": 2,
      "curiosidade": "O vidro pode ser reciclado infinitamente!"
    },
    {
      "tipo": "vf",
      "pergunta": "Os créditos de carbono podem beneficiar empresas sustentáveis.",
      "resposta": True,
      "curiosidade": "Empresas sustentáveis podem vender créditos de carbono."
    },
    {
      "tipo": "vf",
      "pergunta": "Jogar lixo na rua não prejudica o meio ambiente.",
      "resposta": False,
      "curiosidade": "Lixo na rua entope bueiros e causa enchentes."
    },
    {
      "tipo": "vf",
      "pergunta": "Desmatamento contribui para o aumento do efeito estufa.",
      "resposta": True,
      "curiosidade": "Florestas absorvem CO₂; seu corte libera esse gás."
    },
    {
      "tipo": "vf",
      "pergunta": "Água é um recurso natural inesgotável.",
      "resposta": False,
      "curiosidade": "Menos de 1% da água do planeta é potável."
    },
    {
      "tipo": "vf",
      "pergunta": "Plantar árvores ajuda a combater a mudança climática.",
      "resposta": True,
      "curiosidade": "Uma árvore pode absorver até 150 kg de CO₂ por ano."
    },
    {
      "tipo": "vf",
      "pergunta": "Reutilizar materiais é uma forma de reduzir a geração de resíduos.",
      "resposta": True,
      "curiosidade": "Reutilizar reduz a necessidade de novos recursos naturais."
    }
  ]

  #embaralhar ordem das perguntas
  random.shuffle(perguntas)
  
  #inicializa pontuação
  pontuacao = 0

  #laço que exibe enquanto existirem
  for i, item in enumerate(perguntas):
    
    #exibir pergunta no terminal
    print(f"\nPergunta {i + 1}:")

    #verifica se a pergunta é de verdadeiro ou falso
    if item["tipo"] == "vf":
      print(f"{item['pergunta']} (V/F)")
      resposta = input("Sua resposta: ").strip().upper()

      #verifica se a resposta é V ou F
      while resposta not in ["V", "F"]:
        resposta = input("Entrada inválida. Digite apenas 'V' para Verdadeiro ou 'F' para Falso: ").strip().upper()

      resposta_bool = resposta == "V"
      if resposta_bool == item["resposta"]:
        print("✅ Resposta correta!")
        pontuacao += 1
      else:
          print("❌ Resposta incorreta.")

    #caso a pergunta seja de multipla escolha
    elif item["tipo"] == "multipla":
        print(item["pergunta"])
        for idx, opcao in enumerate(item["opcoes"]):
          print(f"{idx + 1}) {opcao}")
        try:
          resposta = int(input("Digite o número da alternativa correta: ")) - 1
          if resposta == item["resposta"]:
             print("✅ Resposta correta!")
             pontuacao += 1
          else:
               print("❌ Resposta incorreta.")
        except ValueError:
           print("❌ Entrada inválida. Digite um número.")
           print(f"💡 Curiosidade: {item['curiosidade']}")

  print(f"\nJogo finalizado! \nSua pontuação: {pontuacao} de {len(perguntas)}")

  if pontuacao == len(perguntas):
    print("Parabéns! Você é um(a) verdadeiro(a) guardião(ã) do planeta! 🌱")
  elif pontuacao >= 6:
    print("Muito bem! Ainda dá pra melhorar! ♻️")
  else:
    print("Vamos estudar mais sobre sustentabilidade! Você consegue! 💪")
  time.sleep(2)

def escolha(opcao_escolhida, usuario):
  if opcao_escolhida == 1:
    return cadastro()
  elif opcao_escolhida == 2:
    if usuario:
      usuario.exibir_dados()
    else:
      print("Nenhum usuário cadastrado.")
    time.sleep(1)
  elif opcao_escolhida == 3:
    if usuario: # Verifica se o usuário foi cadastrado
      jogo_educativo(usuario) # Passa o objeto usuario para o jogo
    else:
      print("Por favor, cadastre-se primeiro.")
      time.sleep(1)
  elif opcao_escolhida == 0:
    print("ENCERRANDO APLICAÇÃO!")
    time.sleep(1)
    exit()
  else:
    print("OPÇÃO INVÁLIDA!!")
    time.sleep(1)
  return usuario

def main():
  usuario = None
  while True:
    print_menu()
    try:
      opcao = int(input("ESCOLHA UMA OPÇÃO: "))
      usuario = escolha(opcao, usuario)
    except ValueError:
      print("Entrada inválida! Digite um número.")
      time.sleep(1)

if __name__ == "__main__":
  main()