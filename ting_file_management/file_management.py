import os
import sys


def txt_importer(path_file):
    if not os.path.exists(path_file):
        mensagem = f"Arquivo {path_file} não encontrado"
        return print(mensagem, file=sys.stderr)
    file_name, extension = os.path.splitext(path_file)
    if extension != '.txt':
        mensagem = "Formato inválido"
        return print(mensagem, file=sys.stderr)
    with open(path_file, 'r') as file:
        text = file.read()
    list_lines = text.split("\n")
    return list_lines
