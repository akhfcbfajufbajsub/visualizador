def init(vals):
    step.items = list(vals)
    step.n = len(vals)
    step.i = 1        # Insertion sort empieza desde el segundo elemento
    step.j = None     # Cursor aún no inicializado

def step():
    items = step.items
    n = step.n
    i = step.i
    j = step.j

    # 1) ¿Terminamos?
    if i >= n:
        return {"done": True}

    # 2) Si j es None, iniciar desplazamiento
    if j is None:
        j = i
        step.j = j
        return {"a": j-1, "b": j, "swap": False, "done": False}

    # 3) ¿Debemos intercambiar?
    if j > 0 and items[j-1] > items[j]:
        a = j-1
        b = j
        items[a], items[b] = items[b], items[a]
        j -= 1
        step.j = j
        return {"a": a, "b": b, "swap": True, "done": False}

    # 4) No hay más desplazamientos → avanzar i
    step.i = i + 1
    step.j = None
    return {"a": None, "b": None, "swap": False, "done": False}
