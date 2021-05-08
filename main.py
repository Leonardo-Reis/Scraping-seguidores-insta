from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import random
from myJson.maniJson import lerArquivo, escreverArquivo

usuario = str(input('Nome de usuário: '))
senha = str(input('Senha: '))
analisando = str(input('Usuario a ser analisado: '))

url = 'https://www.instagram.com/'

driver = webdriver.Firefox()

driver.get(url)
sleep(2)

# LOGIN
input_nome = driver.find_element_by_xpath('//input[@name="username"]')
input_senha = driver.find_element_by_xpath('//input[@name="password"]')
botao_entrar = driver.find_element_by_xpath('//button[@type="submit"]')

for letra in usuario:
    input_nome.send_keys(letra)
    sleep(random() / 30)

for letra in senha:
    input_senha.send_keys(letra)
    sleep(random() / 30)

sleep(1)

botao_entrar.send_keys(Keys.ENTER)

sleep(4)

# LER SEGUIDORES
driver.get(url + analisando)
sleep(3)
numero_seguidores = int(driver.find_element_by_xpath(f'//a[@href="/{analisando}/followers/"]//span[@class="g47SY "]').text)
botao_seguidores = driver.find_element_by_xpath(f'//a[@href="/{analisando}/followers/"]')
botao_seguidores.send_keys(Keys.ENTER)

sleep(2)

tabela_seguidores_scroll = driver.find_element_by_xpath('//div[@class="isgrP"]')

while True:
    seguidores = driver.find_elements_by_xpath('//a[@class="FPmhX notranslate  _0imsa "]')
    print(f'Seguidores analisados: {len(seguidores)}/{numero_seguidores}')

    if len(seguidores) != numero_seguidores:
        tabela_seguidores_scroll.send_keys(Keys.END)
        sleep(random())
    else:
        break

# ORGANIZAR DADOS E MANIPULAR ARQUIVO
lista_seguidores = list()  # Lista que será usada no arquivo .json mais para frente.
for seguidor in seguidores:
    lista_seguidores.append(seguidor.text)

driver.close()

if lerArquivo(analisando):
    user_json = lerArquivo(analisando)
    user_json['seguidores-antes'] = user_json['seguidores-depois']
    user_json['seguidores-depois'] = lista_seguidores
    escreverArquivo(analisando, user_json)
else:
    json_usuario = {
        "user": analisando,
        "seguidores-antes": [],
        "seguidores-depois": lista_seguidores
    }
    escreverArquivo(analisando, json_usuario)
