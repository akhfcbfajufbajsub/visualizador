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

    # Si terminó
    if i >= n:
        return {"done": True}

    # Iniciar desplazamiento del elemento en posición i
    if j is None:
        j = i
        step.j = j
        return {"a": j-1, "b": j, "swap": False, "done": False}

    # Hacer un swap si corresponde
    if j > 0 and items[j-1] > items[j]:
        a = j-1
        b = j
        items[a], items[b] = items[b], items[a]
        j -= 1
        step.j = j
        return {"a": a, "b": b, "swap": True, "done": False}

    # No hay más desplazamientos → avanzar i
    step.i = i + 1
    step.j = None
    return {"a": None, "b": None, "swap": False, "done": False}
