import json


def lerArquivo(nome_user):
    try:
        with open(f'seguidores/{nome_user}.json', 'r') as json_file:
            dado = json.load(json_file)
            return dado
    except:
        return False


def criarArquivo(nome_user, objeto):
    with open(f'seguidores/{nome_user}.json', 'w') as json_file:
        json.dump(objeto, json_file)
