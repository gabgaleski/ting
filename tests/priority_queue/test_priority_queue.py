import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    pq = PriorityQueue()

    pq.enqueue({"nome_do_arquivo": "file1.txt", "qtd_linhas": 10})
    pq.enqueue({"nome_do_arquivo": "file2.txt", "qtd_linhas": 3})
    pq.enqueue({"nome_do_arquivo": "file3.txt", "qtd_linhas": 7})
    pq.enqueue({"nome_do_arquivo": "file4.txt", "qtd_linhas": 2})
    pq.enqueue({"nome_do_arquivo": "file5.txt", "qtd_linhas": 6})
    pq.enqueue({"nome_do_arquivo": "file6.txt", "qtd_linhas": 1})

    assert len(pq) == 6
    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        pq.search(44)

    assert pq.dequeue() == {"nome_do_arquivo": "file2.txt", "qtd_linhas": 3}
    assert pq.dequeue() == {"nome_do_arquivo": "file4.txt", "qtd_linhas": 2}
    assert pq.dequeue() == {"nome_do_arquivo": "file6.txt", "qtd_linhas": 1}
    assert pq.dequeue() == {"nome_do_arquivo": "file1.txt", "qtd_linhas": 10}
    assert pq.dequeue() == {"nome_do_arquivo": "file3.txt", "qtd_linhas": 7}
    assert pq.dequeue() == {"nome_do_arquivo": "file5.txt", "qtd_linhas": 6}

    assert len(pq) == 0

    pq.enqueue({"nome_do_arquivo": "file1.txt", "qtd_linhas": 10})
    pq.enqueue({"nome_do_arquivo": "file2.txt", "qtd_linhas": 3})
    pq.enqueue({"nome_do_arquivo": "file3.txt", "qtd_linhas": 7})
    pq.enqueue({"nome_do_arquivo": "file4.txt", "qtd_linhas": 2})

    assert pq.search(0) == {"nome_do_arquivo": "file2.txt", "qtd_linhas": 3}
    assert pq.search(1) == {"nome_do_arquivo": "file4.txt", "qtd_linhas": 2}
    assert pq.search(2) == {"nome_do_arquivo": "file1.txt", "qtd_linhas": 10}
    assert pq.search(3) == {"nome_do_arquivo": "file3.txt", "qtd_linhas": 7}
