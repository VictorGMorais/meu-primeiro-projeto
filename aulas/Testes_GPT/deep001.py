#1.Crie uma lambda que recebe um número como entrada e retorna o quadrado desse número

#2. Crie uma função lambda que recebe um número como entrada e 
#retorna True se o número for par e False caso contrário.

#3. Crie uma função lambda que recebe duas strings e um separador (também uma string)
#como entrada e retorna as duas strings concatenadas com o separador entre elas.

#4. Crie uma função lambda que calcula o fatorial de um número. 
# Dica: você pode usar recursividade ou uma função auxiliar.

#5. Crie uma lambda que recebe três números e retorna a média deles.

#1
quadrado = lambda x: x**2
print(quadrado(5))

#2
eh_par = lambda x: True if x % 2 == 0 else False
print(eh_par(56))

#3
concatenar = lambda s1,s2,sep: f'{s1}{sep}{s2}'
print(concatenar('bom dia','Como vai voce?','! '))

#4
fatorial = lambda x: 1 if x == 0 else x * fatorial(x-1)
print(fatorial(5))

#5
media = lambda n1,n2,n3: (n1+n2+n3) / 3 if n1 and n2 and n3 > 0 else 'numeros negativos invalidam a media'
print(media(55,67,76))