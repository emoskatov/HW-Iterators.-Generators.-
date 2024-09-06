class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.iterators_queue = []  # определяем вложенный список для добавления элементов очереди итераторов
        self.current_iterator = iter(self.list_of_list)  # определяем итератор для списка
        return self


    def __next__(self):
        while True:
            try:
                self.current_element = next(self.current_iterator)  # получаем следующий элемент списка
            except StopIteration:  # или получаем исключение, ели следующего элемента нет
                if not self.iterators_queue:  # если не осталось элементов в очереди, возвращаем исключение
                    raise StopIteration
                else:
                    self.current_iterator = self.iterators_queue.pop()  # или получаем следующий элемент очереди
                    continue
            if isinstance(self.current_element, list):  # проверяем тип следующего элемента (список или нет)
                self.iterators_queue.append(self.current_iterator)  # если список, то добавляем в очередь
                self.current_iterator = iter(self.current_element)  # и смещаем указатель текущего итератора
            else:  # если элемент не список, то возвращаем этот элемент
                return self.current_element


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()