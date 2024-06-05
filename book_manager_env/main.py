import csv
import flet as ft

# Função para ler dados do CSV
def ler_dados_csv(nome_arquivo):
    alunos = []
    with open(nome_arquivo, mode='r') as arquivo:
        leitor_csv = csv.DictReader(arquivo)
        for linha in leitor_csv:
            alunos.append(linha)
    return alunos

# Função para calcular a média das notas
def calcular_media(alunos):
    total_notas = 0
    for aluno in alunos:
        total_notas += int(aluno['nota'])
    media = total_notas / len(alunos)
    return media

# Função para encontrar maior e menor nota
def encontrar_maior_menor_nota(alunos):
    maior_nota = max(alunos, key=lambda aluno: int(aluno['nota']))
    menor_nota = min(alunos, key=lambda aluno: int(aluno['nota']))
    return maior_nota, menor_nota

# Função para criar a interface gráfica
def main(page: ft.Page):
    alunos = ler_dados_csv('students.csv')
    media_notas = calcular_media(alunos)
    maior_nota, menor_nota = encontrar_maior_menor_nota(alunos)
    
    # Título
    page.add(ft.Text("Lista de Alunos e Notas", style="headlineMedium"))
    
    # Exibindo os dados dos alunos
    for aluno in alunos:
        page.add(ft.Text(f"{aluno['nome']}, Idade: {aluno['idade']}, Nota: {aluno['nota']}"))
    
    # Exibindo a média das notas
    page.add(ft.Text(f"\nA média das notas é: {media_notas:.2f}", style="headlineSmall"))

    # Exibindo a maior e menor nota
    page.add(ft.Text(f"\nMaior Nota: {maior_nota['nome']} com {maior_nota['nota']}", style="headlineSmall"))
    page.add(ft.Text(f"Menor Nota: {menor_nota['nome']} com {menor_nota['nota']}", style="headlineSmall"))

# Inicializando a aplicação Flet
if __name__ == "__main__":
    ft.app(target=main)
