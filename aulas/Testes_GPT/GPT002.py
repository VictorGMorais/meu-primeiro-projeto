def contador_inteligente(ini,fim,pas):
    if pas == 0:
        pas = 1 if ini < fim or ini > fim else -1
    elif (ini < fim and pas < 0) or (ini > fim and pas > 0):
        pas = -pas  
    for i in range(ini,fim +1 if ini < fim else -1,pas):
        yield i
    
                  
for i in contador_inteligente(1, 10, -1):
    print(i,end=' ')