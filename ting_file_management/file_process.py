import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if instance.__len__() != 0:
        for i in range(0, (instance.__len__())):
            if instance.search(i)["nome_do_arquivo"] == path_file:
                return

    file_list = txt_importer(path_file)
    file_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_list),
        "linhas_do_arquivo": file_list
    }
    instance.enqueue(file_dict)
    return print(file_dict, file=sys.stdout)


def remove(instance):
    if instance.__len__() == 0:
        message = "Não há elementos"
        return print(message, file=sys.stdout)
    file = instance.search(0)
    path_file = file["nome_do_arquivo"]
    message = f"Arquivo {path_file} removido com sucesso"
    instance.dequeue()
    return print(message, file=sys.stdout)


def file_metadata(instance, position):
    try:
        file = instance.search(position)
        return print(file, file=sys.stdout)
    except IndexError:
        message = "Posição inválida"
        return print(message, file=sys.stderr)
