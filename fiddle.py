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

    def is_empty(self):
        return len(self.container) == 0

    def push(self, item):
        self.container.append(item)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]


def _stack_sort(input_list: list):
    stack = Stack()
    ref_input = list(input_list)
    output_list = []
    while input_list:
        current = input_list.pop(0)
        if input_list:
            if current > input_list[0]:
                stack.push(current)
                continue
            else:
                if stack.is_empty():
                    output_list.append(current)
                else:
                    if stack.peek() >= current:
                        output_list.append(current)
                    else:
                        stack.push(current)
        else:
            output_list.append(current)
    while not stack.is_empty():
        current = stack.pop()
        output_list.append(current)
    print(ref_input, '->', output_list)
    return output_list


def work(tasks):
    return sorted(tasks) == _stack_sort(tasks)


print(work([2.9, 2.1]))
print(work([5.6, 9.0, 2.0]))
print(work([9.0, 5.6, 2.0]))
print(work([2.0, 5.6, 9.0]))
print(work([5.6]))
print(work([]))
print(work([4, 2, 1, 3, 1]))
print(work([2, 3, 5, 6, 4, 1, 2, 2, 4]))
print(work([6, 5, 4, 3, 2, 1, 1]))

