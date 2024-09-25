#ALUNOS: Arthur Baldissera Claumann Marcos  RM:550219
#       Sarah Ribeiro                       RM:97747 

import time #O import do time é para saber o tempo de execução das funções

# Armazenando pontuações como listas [nome, pontuação, dificuldade] dos médicos residentes.
pontuacoes_lista = []

def adicionar_pontuacao(nome, pontuacao, dificuldade):
    inicio = time.time()
    pontuacoes_lista.append([nome, pontuacao, dificuldade])
    fim = time.time()
    print(f"Tempo para adicionar na lista: {fim - inicio:.10f} segundos")

def mostrar_pontuacoes():
    print("Pontuações (Lista):")
    for p in pontuacoes_lista:
        print(f"Nome: {p[0]}, Pontuação: {p[1]}, Dificuldade: {p[2]}")

# Exemplos:
adicionar_pontuacao('Médico Residente 1', 100, 'Fácil')
adicionar_pontuacao('Médico Residente 2', 88, 'Médio')
mostrar_pontuacoes()

# Armazenando os médicos como dicionários com informações de pontuação e dificuldade
medicos = {}

def adicionar_medico(nome, pontuacao, dificuldade):
    medicos[nome] = {
        'pontuacao': pontuacao,
        'dificuldade': dificuldade
    }

def mostrar_medicos():
    print("Dados dos Médicos:")
    for nome, dados in medicos.items():
        print(f"Nome: {nome}, Pontuação: {dados['pontuacao']}, Dificuldade: {dados['dificuldade']}")

def buscar_medico(nome):
    if nome in medicos:
        dados = medicos[nome]
        print(f"Nome: {nome}, Pontuação: {dados['pontuacao']}, Dificuldade: {dados['dificuldade']}")
    else:
        print("Médico não encontrado.")

# Exemplos:
adicionar_medico('Médico Residente 1', 100, 'Fácil')
adicionar_medico('Médico Residente 2', 88, 'Médio')

mostrar_medicos()

buscar_medico('Médico Residente 1')  # Busca por médico existente
buscar_medico('Médico Residente 3')  # Tentar buscar um médico que não existe


#Sistema básico de Autenticação e Tela de Login
usuarios = {
    "medicoResidente1": "FIAP1",
    "medicoResidente2": "FIAP2"
}

def login(username, password):
    if username in usuarios and usuarios[username] == password:
        print(f"Bem-vindo, {username}!")
        return True
    else:
        print("Login falhou! Usuário ou senha incorretos.")
        return False

# Exemplos:
login("medicoResidente1", "FIAP1")  # Login correto
login("medicoResidente2", "FIAP0")  # Login incorreto
