import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    queue = PriorityQueue()
    assert len(queue) == 0
    file1 = {"qtd_linhas": 3, "nome_do_arquivo": "file1.txt"}
    file2 = {"qtd_linhas": 7, "nome_do_arquivo": "file2.txt"}
    file3 = {"qtd_linhas": 5, "nome_do_arquivo": "file3.txt"}
    queue.enqueue(file1)
    queue.enqueue(file2)

    assert len(queue) == 2

    assert queue.search(0) == file1
    assert queue.search(1) == file2

    assert queue.dequeue() == file1
    assert len(queue) == 1

    assert queue.is_priority(file1) is True
    assert queue.is_priority(file3) is False
    assert queue.is_priority(file2) is False

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        queue.search(55)
