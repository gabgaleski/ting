from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for i in range(len(instance)):
        if instance[i]["nome_do_arquivo"] == path_file:
            return None

    files = txt_importer(path_file)
    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(files),
        "linhas_do_arquivo": (files),
    }

    instance.enqueue(data)
    print(data)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
