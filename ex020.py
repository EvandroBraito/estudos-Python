from random import shuffle
n1 = str(input('Primereio aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
nomes = [n1, n2, n3, n4]
shuffle(nomes)
print('a ortem de apresentacão será \n{}'.format(nomes))
