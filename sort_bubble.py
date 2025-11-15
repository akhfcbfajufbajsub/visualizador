def init(vals):
    return {
        "items": list(vals),
        "n": len(vals),
        "i": 0,
        "j": 0
    }

def step(state):
    items = state["items"]
    n = state["n"]
    i = state["i"]
    j = state["j"]
    
    # Si ya terminó
    if i >= n - 1:
        return {"done": True, "state": state}

    # Par a comparar
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

    # Guardar punteros actualizados en el estado
    state["i"] = i
    state["j"] = j

    return {
        "a": a,
        "b": b,
        "swap": swap,
        "done": False,
        "state": state
    }

