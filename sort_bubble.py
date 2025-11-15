def init(vals):
    step.items = list(vals)
    step.n = len(step.items)
    step.i = 0
    step.j = 0

def step():
    items = step.items
    n = step.n
    i = step.i
    j = step.j

    # Fin del algoritmo
    if i >= n - 1:
        return {"done": True}

    a = j
    b = j + 1
    swap = False

    # Comparación + posible swap
    if items[a] > items[b]:
        items[a], items[b] = items[b], items[a]
        swap = True

    # Avanzar punteros
    j += 1
    if j >= n - 1 - i:
        i += 1
        j = 0

    step.i = i
    step.j = j

    return {"a": a, "b": b, "swap": swap, "done": False}
