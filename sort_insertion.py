def init(vals):
    step.items = list(vals)
    step.n = len(step.items)
    step.i = 1
    step.j = None

def step():
    items = step.items
    n = step.n
    i = step.i
    j = step.j

    # Terminado
    if i >= n:
        return {"done": True}

    # Empezar desplazamiento:
    if j is None:
        j = i
        step.j = j
        return {"a": j-1, "b": j, "swap": False, "done": False}

    # Desplazar 1 posición hacia la izquierda
    if j > 0 and items[j-1] > items[j]:
        a = j-1
        b = j
        items[a], items[b] = items[b], items[a]
        j -= 1
        step.j = j
        return {"a": a, "b": b, "swap": True, "done": False}

    # No queda más desplazamiento → pasar al siguiente i
    step.i = i + 1
    step.j = None
    return {"a": None, "b": None, "swap": False, "done": False}

