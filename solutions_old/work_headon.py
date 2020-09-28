def work(tasks):
    return len(tasks) < 3 or sorted(tasks) == _stack_sorted(tasks)


def _stack_sorted(input_queue):
    stack = list()
    output_queue = list()
    min_ = min(input_queue)

    while input_queue:
        current = input_queue.pop(0)
        if current == min_:
            output_queue += [current]
            min_ = _new_min_from(min_, input_queue, stack)
            continue

        output_queue += _unwind(stack, until=current)
        stack += [current]

    output_queue += reversed(stack)
    return output_queue


def _new_min_from(min_, input_queue, stack):
    return min(min(input_queue, default=min_), min(stack, default=min_))


def _unwind(stack, until=None):
    unwound = list()
    while stack and until > stack[-1]:
        unwound += [stack.pop()]
    return unwound
