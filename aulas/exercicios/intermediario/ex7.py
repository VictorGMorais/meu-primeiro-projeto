#crie uma funçao zipper que junte duas listas

cidades = ['Salvador','Ubatuba','Belo Horizonte']
tag = ['BA','SP','MG','GO']

def zipper(cid,tg):
    menor = min(len(cid),len(tg))
    return [(cid[i],tg[i]) for i in range(menor)]
    
print(zipper(cidades,tag))
print(list(zip(cidades,tag)))
# print(list(zip_longest(cidades,tag, fillvalue='Sem Cidade')))