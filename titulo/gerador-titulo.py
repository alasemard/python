# gerador Titulo de Eleitor em Python

import random

# codigos das UFs de acordo com a RESOLUCAO Nº 19.875, DE 12 DE JUNHO DE 1997
codUf = ["SP","MG","RJ","RS","BA","PR","CE","PE","SC", "GO",
		 "MA","PB","PA","ES","PI","RN","AL","MT", "MS",
		 "DF","SE","AM","RO","AC","AP","RR","TO","ZZ"]

# entrada e validacao da UF
print("Digite para qual UF deseja gerar o titulo")
print("ZZ significa internacional e se não unformar nada significa aleatório")
validacaoUf = True
while validacaoUf == True:
	ufInformada = input("Digite a UF: ").upper()
	if ufInformada in codUf:
		validacaoUf = False
	elif (ufInformada not in codUf) and (ufInformada == ""):
		validacaoUf = False

# entrada e validacao da quantidade de titulos a serem gerados
validacaoQuantidade = True
while validacaoQuantidade == True:
	try:
		quantidadeDeTitulosASeremGerados = int(input("Digite a quantidade de titulos eleitorais que deseja gerar: "))
		quantidadeDeTitulosASeremGerados = abs(quantidadeDeTitulosASeremGerados)
		validacaoQuantidade = False
	except:
		print("Numero invalido! Tente novamente")

# funcao que retorna o codigo da UF de acordo com a string de UF passada
seqUf = []
ufAleatoria = False
def retornaListaCodigoUf(uf):
	if uf == "":
		global ufAleatoria
		ufAleatoria = True
		return 0
	indice = codUf.index(uf) + 1
	if indice < 10:
		seqUf.append(0)
		seqUf.append(indice)
		return seqUf
	else:
		seqUf.append(int(indice/10))
		seqUf.append(indice % 10)
		return seqUf


retornaListaCodigoUf(ufInformada)

# uma linha de espaco para melhor leitura do resultado
print("")

for i in range(quantidadeDeTitulosASeremGerados):

	# gera um sequencial aleatorio
	sequencialTitulo = [random.randint(0, 9) for x in range(8)]

	# calculo do primeiro DV
	seq1 = sequencialTitulo.copy()
	for i in range(len(seq1)):
		seq1[i] = seq1[i]*(i+2)

	soma1 = sum(seq1) % 11
	dv1 = 0 if soma1 == 10 else soma1


	#calculo do segundo DV
	seq2 = []
	if ufAleatoria == True:
		seqUf = []
		a = random.randint(0, 2)
		seqUf.append(a)
		if a == 2:
			seqUf.append(random.randint(0, 8))
		else:
			seqUf.append(random.randint(0, 9))
		seq2 = seqUf.copy()
	else:
		seq2 = seqUf.copy()

	seq2.append(dv1)
	for i in range(len(seq2)):
		seq2[i] = seq2[i]*(i+7)

	soma2 = sum(seq2) % 11
	dv2 = 0 if soma2 == 10 else soma2


	# concatenando os DV's
	titulo = sequencialTitulo + seqUf
	titulo.append(dv1)
	titulo.append(dv2)
	tituloFinal = ""
	for i in range(len(titulo)):
		tituloFinal += str(titulo[i])

	print(tituloFinal)




