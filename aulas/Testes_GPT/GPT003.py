# from collections import defaultdict

# def contando_caracteres(caracteres=''):
#     frase = list(caracteres.replace(' ', ''))
#     cont = defaultdict(int)
#     for letra in frase:
#         cont[letra] += 1
#     return dict(cont)
    
# frase_contada = contando_caracteres('   venha rodar a baiana de salto alto  ')


# for k,v in frase_contada.items():
#     print(f'letra [{k}] aparece {v} vez(s)')


frase = 'victor gomes morais'
cont = {}
frase.lower().replace(' ', '')
for carac in frase:
    if carac in cont:
        cont["carac"] += 1
    else:
        cont["carac"] = 1
        
print(cont)


