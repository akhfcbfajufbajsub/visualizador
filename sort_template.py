# Template genérico — SKELETON
# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i=0
j=0
fase="buscar"

def init(vals):
    global items, n
    items = list(vals)
    n = len(items)
    i=1
    j=i
    fase="buscar"

def step():
    # TODO: implementar UN micro-paso de tu algoritmo y devolver el dict.
    # Recordá:
    # - a, b dentro de [0, n-1]
    # - si swap=True, primero hacé el intercambio en 'items'
    # - cuando termines, devolvé {"done": True}
    return {"done": True}
