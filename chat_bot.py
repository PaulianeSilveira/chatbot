import Levenshtein
import smtplib

# Variáveis de e-mail
servidor_smtp = "smtp.example.com"
email_remetente = "chatbot@example.com"
senha_email = "senha123"
assunto_email = "Resposta do Chatbot"
corpo_email = "Olá, \n\nSua pergunta foi: ${params.Pergunte}\n\nA resposta do chatbot é: [INCLUIR RESPOSTA DO CHATBOT]\n\nAtenciosamente,\nEquipe Chatbot"

def carregar_perguntas(arquivo):
  """
  Carrega perguntas e respostas de um arquivo de texto.

  Argumentos:
    arquivo (str): Caminho para o arquivo de perguntas e respostas.

  Retorna:
    dict: Dicionário com perguntas como chaves e respostas como valores.
  """
  perguntas_respostas = {}
  with open(arquivo, "r") as f:
    for linha in f:
      pergunta, resposta = linha.strip().split("|")
      perguntas_respostas[pergunta.lower()] = resposta
  return perguntas_respostas

def encontrar_resposta(pergunta, perguntas_respostas, limiar_distancia=5):
  """
  Encontra a resposta à pergunta do usuário com base em um dicionário de perguntas e respostas.

  Argumentos:
    pergunta (str): Pergunta do usuário.
    perguntas_respostas (dict): Dicionário com perguntas como chaves e respostas como valores.
    limiar_distancia (int, opcional): Limiar de distância de Levenshtein para considerar uma resposta válida (padrão: 5).

  Retorna:
    str: Resposta à pergunta do usuário ou "Pergunta não encontrada".
  """
  menor_distancia = float("inf")
  melhor_resposta = ""
  for p, r in perguntas_respostas.items():
    distancia = Levenshtein.distance(pergunta, p)
    if distancia < menor_distancia:
      menor_distancia = distancia
      melhor_resposta = r
  if menor_distancia <= limiar_distancia:
    return melhor_resposta
  else:
    return "Pergunta não encontrada."

def enviar_email(resposta):
  """
  Envia um e-mail de resposta ao usuário.

  Argumentos:
    resposta (str): Resposta à pergunta do usuário.
  """
  with smtplib.SMTP(servidor_smtp) as smtp:
    smtp.starttls()
    smtp.login(email_remetente, senha_email)
    mensagem = f"Subject: {assunto_email}\n\n{corpo_email.replace('[INCLUIR RESPOSTA DO CHATBOT]', resposta)}"
    smtp.sendmail(email_remetente, params.emailUsuario, mensagem)

if __name__ == "__main__":
  # Carregar perguntas e respostas
  perguntas_respostas = carregar_perguntas("perguntas.txt")

  # Obter a pergunta do usuário
  pergunta = params.Pergunte

  # Encontrar a resposta à pergunta
  resposta = encontrar_resposta(pergunta, perguntas_respostas)

  # Enviar e-mail de resposta
  if resposta != "Pergunta não encontrada.":
    enviar_email(resposta)

  # Imprimir a resposta na tela (opcional)

