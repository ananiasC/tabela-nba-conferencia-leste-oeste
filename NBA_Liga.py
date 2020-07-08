from selenium.webdriver import Firefox
from time import sleep
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import csv

def nome_equipes_nba(equipes):
    nome_equipes = []

    for equipe in equipes:
        if equipe.get_attribute('title') != '' and len(equipe.get_attribute('title')) < 38:
            nome = equipe.get_attribute('title')
            nome_equipes.append(nome)

    return nome_equipes
# SALVANDO EM ARQUIVO csv

def escrever_csv(tabela_conf_leste, tabela_conf_oeste):
    with open('nba_tabela_leste.csv', 'w') as arquivo_csv:
        colunas = ['EQUIPES', 'V', 'D', '% VIT.', 'JA', 'CASA', 'VISITANTE', 'DIV', 'CONF', 'PTS', 'PTS CONTRA', 'DIF', 'STRK', 'U10']
        escrever = csv.DictWriter(arquivo_csv, fieldnames = colunas, delimiter=';', lineterminator='\n')
        escrever.writeheader()
        for dados_leste in tabela_conf_leste:
            dados = dados_leste[1]
            escrever.writerow({'EQUIPES': dados_leste[0], 'V': dados[0], 'D': dados[1], '% VIT.': dados[2], 'JA': dados[3], 'CASA': dados[4], 'VISITANTE': dados[5], 'DIV': dados[6], 'CONF': dados[7], 'PTS': dados[8], 'PTS CONTRA': dados[9], 'DIF': dados[10], 'STRK': dados[11], 'U10': dados[12]})

    with open('nba_tabela_oeste.csv', 'w') as arquivo_csv:
        colunas = ['EQUIPES', 'V', 'D', '% VIT.', 'JA', 'CASA', 'VISITANTE', 'DIV', 'CONF', 'PTS', 'PTS CONTRA', 'DIF', 'STRK', 'U10']
        escrever = csv.DictWriter(arquivo_csv, fieldnames = colunas, delimiter=';', lineterminator='\n')
        escrever.writeheader()
        for dados_oeste in tabela_conf_oeste:
            dados = dados_oeste[1]
            escrever.writerow({'EQUIPES': dados_oeste[0], 'V': dados[0], 'D': dados[1], '% VIT.': dados[2], 'JA': dados[3], 'CASA': dados[4], 'VISITANTE': dados[5], 'DIV': dados[6], 'CONF': dados[7], 'PTS': dados[8], 'PTS CONTRA': dados[9], 'DIF': dados[10], 'STRK': dados[11], 'U10': dados[12]})

def ler_print_csv():
    with open('nba_tabela_leste.csv', 'r') as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv, delimiter=';')
        for coluna in leitor:
            print(coluna['EQUIPES'], coluna['V'], coluna['D'], coluna['% VIT.'], coluna['JA'], coluna['CASA'], coluna['VISITANTE'], coluna['DIV'], coluna['CONF'], coluna['PTS'], coluna['PTS CONTRA'], coluna['DIF'], coluna['STRK'], coluna['U10'])

    with open('nba_tabela_oeste.csv', 'r') as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv, delimiter=';')
        for coluna in leitor:
            print(coluna['EQUIPES'], coluna['V'], coluna['D'], coluna['% VIT.'], coluna['JA'], coluna['CASA'], coluna['VISITANTE'], coluna['DIV'], coluna['CONF'], coluna['PTS'], coluna['PTS CONTRA'], coluna['DIF'], coluna['STRK'], coluna['U10'])

# DIVISAO DOS NOMES POR CONFERENCIA

def divisao_equipes_conferencia(nome_equipes, conf_leste, conf_oeste):
    contador = 1
    for nome in nome_equipes:
        if contador < 16:
            conf_leste.append(nome)
            contador += 1
        else:
            conf_oeste.append(nome)

# DIVISAO DOS DADOS POR CONFERENCIA NOS INTERVALOS DESEJADOS

def divisao_dados_conferencia(dados_equipes, lista_intervalo_1, lista_intervalo_2):
    posicao = 1

    for dados in dados_equipes:
        if posicao >= 16 and posicao <= 210:
            lista_intervalo_1.append(dados.text)
        elif posicao >= 226 and posicao <= 420:
            lista_intervalo_2.append(dados.text)

        posicao += 1

# PRINT PARA OS NOMES DAS EQUIPES POR CONFERENCIA

def print_nome_equipes(conf_leste, conf_oeste):
    print('\n-------------------------- Equipes --------------------------')
    print('--------- Coferência Leste ---------')
    for eq_leste in conf_leste:
        print(eq_leste)

    print('--------- Coferência Oeste ---------')
    for eq_oeste in conf_oeste:
        print(eq_oeste)

# DIVISAO DOS DADOS PARA SUAS RESPECTIVAS EQUIPES

def definicao_tabelas_leste_oeste(tabela_conf_leste, tabela_conf_oeste, conf_leste, conf_oeste, lista_intervalo_1, lista_intervalo_2):
    contador_nome = 0
    lista_dados = []
    contador_troca = 1

    for intervalo_um in lista_intervalo_1:
        lista_dados.append(intervalo_um)
        if contador_troca == 13:
            tabela_conf_leste.append([conf_leste[contador_nome], lista_dados])
            contador_nome += 1
            lista_dados = []
            contador_troca = 1
        else:
            contador_troca += 1

    contador_nome = 0
    lista_dados = []
    contador_troca = 1

    for intervalo_dois in lista_intervalo_2:
        lista_dados.append(intervalo_dois)
        if contador_troca == 13:
            tabela_conf_oeste.append([conf_oeste[contador_nome], lista_dados])
            contador_nome += 1
            lista_dados = []
            contador_troca = 1
        else:
            contador_troca += 1

# PRINT PARA OS DADOS POR CONFERENCIA

def print_tabelas(tabela_conf_leste, tabela_conf_oeste):
    print('\n------------------------------- CONFERÊNCIA LESTE -------------------------------\n')
    for dados_leste in tabela_conf_leste:
        print(dados_leste[0], '\n\t\t\t', dados_leste[1])
    print('\n------------------------------- CONFERÊNCIA OESTE -------------------------------\n')
    for dados_oeste in tabela_conf_oeste:
        print(dados_oeste[0], '\n\t\t\t', dados_oeste[1])

def print_dados_equipes(lista_intervalo_1, lista_intervalo_2):
    contador_enter = 1
    print('\n------- Intervalo 01 -------')
    for intervalo_um in lista_intervalo_1:
        print(intervalo_um, end=' | ')
        if contador_enter == 13:
            print('')
            contador_enter = 1
        else:
            contador_enter += 1

    contador_enter = 1
    print('\n------- Intervalo 02 -------')
    for intervalo_dois in lista_intervalo_2:
        print(intervalo_dois, end=' | ')
        if contador_enter == 13:
            print('')
            contador_enter = 1
        else:
            contador_enter += 1

# ----------------------------------------------------------------------------------------------
# ------------------------------------ EXECUÇÃO PRINCIPAL --------------------------------------
# ----------------------------------------------------------------------------------------------

# Declarações para contato web com site de destino
option = Options()
option.headless = True
url = 'https://www.espn.com.br/nba/classificacao'
browser = Firefox(options=option)
browser.get(url)

sleep(1)
# Declaração da Listas

conf_leste = []
conf_oeste = []
lista_intervalo_1 = []
lista_intervalo_2 = []

tabela_conf_leste = []
tabela_conf_oeste = []

# COLETA DOS NOMES DAS EQUIPES DE CADA CONFERENCIA

equipes = browser.find_elements_by_tag_name('img')
nome_equipes = nome_equipes_nba(equipes)


# COLETA DOS DADOS DE TODAS AS EQUIPES
dados_equipes = browser.find_elements_by_tag_name('td')

# FILTRO DOS DADOS

divisao_equipes_conferencia(nome_equipes, conf_leste, conf_oeste)
divisao_dados_conferencia(dados_equipes, lista_intervalo_1, lista_intervalo_2)
definicao_tabelas_leste_oeste(tabela_conf_leste, tabela_conf_oeste, conf_leste, conf_oeste, lista_intervalo_1, lista_intervalo_2)

# PRINT DE DADOS

# print_dados_equipes(lista_intervalo_1, lista_intervalo_2)
# print_nome_equipes(conf_leste, conf_oeste)
#print_tabelas(tabela_conf_leste, tabela_conf_oeste)

# SALVAR DADOS EM CSV

escrever_csv(tabela_conf_leste, tabela_conf_oeste)

# PRINTANDO PELO ARQUIVO CSV

ler_print_csv()

browser.quit()
