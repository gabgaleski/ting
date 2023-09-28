def exists_word(word, instance):
    result = []
    for i in range(len(instance)):
        file = instance.search(i)
        data = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": [],
        }

        for line, line_num in enumerate(file["linhas_do_arquivo"], 1):
            if word.lower() in line_num.lower():
                data["ocorrencias"].append(
                    {
                        "linha": line,
                    }
                )

        if len(data["ocorrencias"]) > 0:
            result.append(data)

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
