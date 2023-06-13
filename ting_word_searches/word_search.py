def exists_word(word, instance):
    search_result = list()
    for i in range(0, (instance.__len__())):
        file = instance.search(i)
        occurrence = list()
        for j in range(0, file["qtd_linhas"]):
            line = file["linhas_do_arquivo"][j]
            if word.lower() in line.lower():
                occurrence.append({"linha": (j + 1)})
        if len(occurrence) != 0:
            result = {
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": occurrence
            }
            search_result.append(result)
    return search_result


def search_by_word(word, instance):
    search_result = list()
    for i in range(0, (instance.__len__())):
        file = instance.search(i)
        occurrence = list()
        for j in range(0, file["qtd_linhas"]):
            line = file["linhas_do_arquivo"][j]
            if word.lower() in line.lower():
                occurrence.append({
                    "linha": (j + 1),
                    "conteudo": line
                })
        if len(occurrence) != 0:
            result = {
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": occurrence
            }
            search_result.append(result)
    return search_result
