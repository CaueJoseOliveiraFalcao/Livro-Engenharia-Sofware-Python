

arquivo = open('text.txt', 'r')
numeroAlunos = 0
numeroReprova = 0
somaNotas = 0
media = 0
for linha in arquivo:
    numeroAlunos += 1
    nome = linha.split()[0]
    nota = float(linha.split()[1])
    if nota < 7.0:
        numeroReprova += 1
    somaNotas += nota
media = somaNotas / numeroAlunos

print(media, numeroAlunos, numeroReprova)
arquivo.close()
