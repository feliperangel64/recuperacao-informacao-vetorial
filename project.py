############## ENTRADA ###################
#Leitura do arquivo de texto 1
arq = open("./arquivos/texto1.txt", 'r')
texto1 = arq.read()
arq.close()

#Imprime conteúdo arquivo de texto 1
print('Texto 1')
print(texto1)
vet_texto1 = texto1.split()
print(vet_texto1)
print()

#Leitura do arquivo de texto 2
arq2 = open("./arquivos/texto2.txt", 'r')
texto2 = arq2.read()
arq2.close()

#Imprime conteúdo arquivo de texto 2
print('Texto 2')
print(texto2)
vet_texto2 = texto2.split()
print(vet_texto2)
print()

############## SAÍDA ###################

#Vocabulário de palavras únicas
print('Vocabulário único')
vet_vocabulario = texto1.split()

for palavra in vet_texto2:
    if texto1.find(palavra) == -1:
        if palavra not in vet_vocabulario:
            vet_vocabulario.append(palavra)

print(vet_vocabulario)
print()

#Verificar ocorrência no texto 1
print('Vetor palavras do texto 1')
vet_ocorr_txt1 = []
cont = 0

for palavra_vocabulario in vet_vocabulario:
    cont = vet_texto1.count(palavra_vocabulario)
    vet_ocorr_txt1.append(cont)

print(vet_ocorr_txt1)
print()

#Verificar ocorrência no texto 2
print('Vetor palavras do texto 2')
vet_ocorr_txt2 = []
cont_2 = 0

for palavra_vocabulario_2 in vet_vocabulario:
    cont_2 = vet_texto2.count(palavra_vocabulario_2)
    vet_ocorr_txt2.append(cont_2)

print(vet_ocorr_txt2)








