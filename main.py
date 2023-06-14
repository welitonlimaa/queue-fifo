from ting_file_management.priority_queue import PriorityQueue
from ting_file_management.file_process import process

from ting_word_searches.word_search import search_by_word

queue = PriorityQueue()

process('statics/novo_paradigma_globalizado.txt', queue)
process('statics/nome_pedro.txt', queue)
process('statics/arquivo_teste.txt', queue)

print(queue.__len__())

print(search_by_word('orçamento', queue))
