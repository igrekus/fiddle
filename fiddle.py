"""
#task Для транспортирования материалов из цеха А в цех В используется конвейер.
Материалы упаковываются в одинаковые контейнеры и размещаются на ленте один за одним в порядке изготовления в цехе А.
Каждый контейнер имеет степень срочности обработки в цехе В - флоат значение, где наименьшее означает наивысший приоритет.
То есть приоритет 1.0 должен выполняться раньше, чем 9.0.
Для упорядочивания контейнеров по степени срочности используют накопитель,
который находится в конце конвейера перед входом в цех В.

Накопитель работает пошагово, на каждом шаге возможны следующие действия:
 - накопитель перемещает первый контейнер из ленты в цех В;
 - накопитель перемещает первый контейнер из строки в склад
 (в складе каждый следующий контейнер помещается на предыдущий);
 - накопитель перемещает верхний контейнер из склада в цех В.

Напишите программу, которая по последовательности контейнеров определит, можно ли упорядочить их по степени срочности
пользуясь описанным накопителем. Предполагается, что всегда приходит на вход список с валидными значениями или пустой.
Сигнатуру функции не менять def work(tasks: list) -> bool: принимает на вход список флоат и возвращает булин
Ничего не импортируем, исключения не кидать, решения шлем мне в личку модулем питона.

Примеры:
work(2.9, 2.1) == True
work(5.6, 9.0, 2.0) ==False

Алексей admin
Сразу скажу, кроме разных способов есть 2 концептуальных подхода к решению -можно в лоб,
создав соответствующие структуры данных, а можно по-хитрому, раскурив алгоритм.
Новичкам, кому задача кажется сложной - можете написать в личку, дам задачку попроще.
"""


class Stack:
    def __init__(self):
        self.container = []

    def __bool__(self):
        return bool(self.container)


def _stack_sort(input_queue: list):
    stack = Stack()
    min_num = min(input_queue) if input_queue else 0
    output_queue = []

    while input_queue:
        current = input_queue.pop(0)
        if current == min_num:
            output_queue.append(current)
            min_num = _select_new_min(min_num, input_queue, stack)
            continue
        _unroll_stack_if(current, output_queue, stack)
        stack.container.append(current)
    output_queue.extend(reversed(stack.container))
    return output_queue


def _unroll_stack_if(current, output_queue, stack):
    while stack and current > stack.container[-1]:
        output_queue.append(stack.container.pop())


def _select_new_min(min_num, input_queue, stack):
    try:
        min_num = min(min(input_queue), min(stack.container))
    except ValueError:
        pass
    return min_num


def work(tasks):
    return sorted(tasks) == _stack_sort(tasks)
