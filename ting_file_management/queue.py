from ting_file_management.abstract_queue import AbstractQueue

from collections import deque


class Queue(AbstractQueue):
    def __init__(self):
        self._data = deque()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        self._data.popleft()

    def search(self, index):
        element = self._data[index]
        if element is None:
            raise ("Índice Inválido ou Inexistente")
        try:
            return element
        except IndexError as e:
            print(str(e))
