items = []
n = 0
i = 0          # cabeza de la parte no ordenada
j = 0          # cursor que recorre y busca el mínimo
min_idx = 0    # índice del mínimo de la pasada actual
fase = "buscar"  # "buscar" | "swap"

def init(vals):
    global items, n, i, j, min_idx, fase
    items = list(vals)
    n = len(items)
    i = 0
    j = i + 1
    min_idx = i
    fase = "buscar"

def step():
     global items, n,i,j, min_idx,fase                                         
    if i>=n:
       return {"done":True}  
    if fase=="buscar":
       if j<n: 
          if items[j]<= items[min_idx]:
             min_idx=j
          j_actual=j
          j=j+1
          return {"a": min_idx, "b": j_actual, "swap": False, "done": False}
       Else: #   Al terminar el barrido, pasar a fase "swap".
             fase=swap 
             return step()
    if fase== "swap":
       if min_idx !=i:
          items[i], items[min_idx]= items[min_idx], items[i] 
          swap_unico = {"a":i, "b":min_idx, "swap":True, "done":False 
          
       i=i+1
       j=i+1
       min_idx=i
       fase="buscar" 
       return swap_unico 
