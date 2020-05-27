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

    def push(self, item):
        self.container.append(item)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    @property
    def min(self):
        return min(self.container)


def _stack_sort(inp: list):
    stack = Stack()
    input_queue = list(inp)
    min_num = min(input_queue) if input_queue else 0
    output_queue = []

    while input_queue:
        current = input_queue.pop(0)
        if current == min_num:
            output_queue.append(current)
            if input_queue and min_num not in input_queue:
                min_num = min(input_queue)
            if stack and min_num > stack.min:
                min_num = stack.min
        else:
            while stack and current > stack.peek():
                output_queue.append(stack.pop())
            stack.push(current)
    while stack:
        output_queue.append(stack.pop())
    return output_queue


def work(tasks):
    return sorted(tasks) == _stack_sort(tasks)


print(work([2.9, 2.1]), 'true')
print(work([5.6, 9.0, 2.0]), 'false')
print(work([9.0, 5.6, 2.0]), 'true')
print(work([2.0, 5.6, 9.0]), 'true')
print(work([5.6]), 'true')
print(work([]), 'true')
print(work([4, 2, 1, 3, 1]), 'false')
print(work([2, 3, 5, 6, 4, 1, 2, 2, 4]), 'false')
print(work([6, 5, 4, 3, 2, 1, 1]), 'true')

print(work([3, 2, 1, 1, 2, 2, 4]), 'true')
print(work([3, 2, 1, 1, 2, 1, 4]), 'true')
print(work([2, 2, 1, 5, 4, 3]), 'true')
