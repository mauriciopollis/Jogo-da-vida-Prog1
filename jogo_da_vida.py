from curses.ascii import isdigit
import os


def imprime_arquivos_existentes():
    arquivos = os.listdir("Arquivos_Exemplo")
    print("Os arquivos exemplo existentes são:")
    for arquivo in arquivos:
        print(arquivo)


def retorna_arquivo_exemplo():
    arquivo_exemplo = input("Escolha um dos arquivos existentes: ")
    if arquivo_exemplo not in os.listdir("Arquivos_Exemplo"):
        print("Arquivo inválido.")
        retorna_arquivo_exemplo()
    else:
        print(f'O arquivo {arquivo_exemplo} foi selecionado.')
        return arquivo_exemplo


def retorna_num_iteracoes():
    num_iteracoes = input("Insira o número de iterações: ")
    if num_iteracoes.isdigit():
        if int(num_iteracoes) >= 0:
            print(f'Serão feitas {num_iteracoes} iterações.')
            return num_iteracoes
        else:
            print("O número de iterações deve ser um inteiro não negativo.")
            retorna_num_iteracoes()
    else:
        print("O número de iterações deve ser um inteiro não negativo.")
        retorna_num_iteracoes()


def retorna_populacao_inicial(arquivo):
    matriz = []
    with open('Arquivos_Exemplo' + '\\' + arquivo, 'r') as f:
        linhas = f.readlines()
        for linha in linhas:
            linha = linha.strip('\n')
            linha = linha.split()
            matriz.append(linha)
    return matriz


def regras_evolucao(vizinhanca, celula):
    if celula == 'M':
        if vizinhanca.count('V') == 3:
            celula = 'V'
    elif celula == 'V':
        if vizinhanca.count('Z') >= 1:
            celula = 'Z'
        else:
            if vizinhanca.count('V') < 2 or vizinhanca.count('V') > 3:
                celula = 'M'
    elif celula == 'Z':
        if vizinhanca.count('V') == 0:
            celula = 'M'
    return celula


def retorna_vizinhos(celula): # irá retornar uma lista com os vizinhos de uma dada célula
    pass


def jogo_da_vida(populacao_inicial, num_iteracoes):
    pass # irá retornar uma matriz com a população ao final do jogo


def escreve_populacao_em_arquivo(populacao_final):
    with open('resultado.txt', 'w') as f:
        for linha in populacao_final:
            f.write(" ".join(linha) + '\n')


def main():
    while True:
        imprime_arquivos_existentes()
        arquivo_exemplo = retorna_arquivo_exemplo()
        num_iteracoes = retorna_num_iteracoes()
        populacao_inicial = retorna_populacao_inicial(arquivo_exemplo)
        populacao_final = jogo_da_vida(populacao_inicial, num_iteracoes)
        escreve_populacao_em_arquivo(populacao_final)
        print("O resultado do jogo foi escrito no arquivo resultado.txt")
        continua = input("Deseja recomeçar o jogo? [SIM - qualquer tecla; Não - N]").upper()
        if continua == 'N':
            break


main()

"""
# Cria a matriz que representa a situação da população ao início de cada rodada.
inicio_da_rodada = []

# Pergunta ao usuário qual dos exemplos disponíveis deve ser rodado
arquivo_exemplo = input("Insira o nome do arquivo exemplo: ")

# Abre o arquivo que contém a situação inicial da população.
f1 = open(arquivo_exemplo, "r")

# Pede para que seja inserido o número de iterações a serem feitas na população:
numero_de_iteracoes = int(input("Insira o número de iterações: "))

# Loop que preenche a matriz que representa a população no início de uma rodada com as linhas da matriz presente no
# arquivo.
linha = f1.readline()
while linha != "":
    linha = linha.split()
    inicio_da_rodada.append(linha)
    linha = f1.readline()

# Fecha o arquivo de leitura.
f1.close()

# Cria a matriz que guarda a situação da população ao final de cada iteração.
final_da_rodada = []

# Variável que armazena o número de linhas da matriz inicial.
M = len(inicio_da_rodada)

# Variável que armazena o número de colunas da matriz inicial.
N = len(inicio_da_rodada[0])

# Loop que copia a matriz inicial para a matriz final.
for linha in inicio_da_rodada:
    copia = linha.copy()
    final_da_rodada.append(copia)

# Loop que efetua o número de iterações necessárias.
for k in range(numero_de_iteracoes):
    # Loops nos índices i e j, que percorrem cada célula da matriz inicial, para que os vizinhos de cada célula possam
    # ser identificados.
    for i in range(M):
        for j in range(N):
            # Dividi os tipos de matrizes nos seguintes grupos:
            # (1) Matrizes com mais de uma linha e mais de uma coluna.
            # (2) Matrizes com apenas uma linha e mais de uma coluna.
            # (3) Matrizes com apenas uma linha e mais de uma coluna.
            # (4) Matrizes com apenas uma linha e apenas uma coluna.
            # Foi necessário dividir as matrizes nesses grupos pois para cada tipo de matriz a maneira de achar os
            # vizinhos de cada célula é diferente.

            # Matrizes do grupo (1):
            if M > 1 and N > 1:
                # Para esse tipo de matriz, dividi as células em 9 tipos:
                # (i) Células no 'interior' da matriz, ou seja, células que não estão na primeira linha, na última
                # linha, na primeira coluna ou na última coluna.
                # (ii) Células que estão na primeira linha, exceto as células mais à esqueda e à direita.
                # (iii) Células que estão na última linha, exceto as células mais à esquerda e á direita.
                # (iv) Células da primeira coluna, exceto a primeira e a última.
                # (v) Células que estão na última coluna, exceto a primeira e a última.
                # (vi) Célula do canto superior esquerdo.
                # (vii) Célula do canto superior direito.
                # (viii) Célula do canto inferior esquerdo.
                # (iv) Célula do canto inferior direito.
                # Fiz essa divisão pois para cada tipo de célula desse grupo a forma de achar os vizinhos é diferente.

                # Achando os vizinhos das células do tipo (i):
                if 0 < i < M - 1 and 0 < j < N - 1:
                    vizinhos = [inicio_da_rodada[i - 1][j - 1], inicio_da_rodada[i - 1][j],
                                inicio_da_rodada[i - 1][j + 1], inicio_da_rodada[i][j - 1], inicio_da_rodada[i][j + 1],
                                inicio_da_rodada[i + 1][j - 1], inicio_da_rodada[i + 1][j],
                                inicio_da_rodada[i + 1][j + 1]]

                # Achando os vizinhos das células do tipo (ii):
                elif i == 0 and 0 < j < N - 1:
                    vizinhos = [inicio_da_rodada[0][j - 1], inicio_da_rodada[1][j - 1], inicio_da_rodada[1][j],
                                inicio_da_rodada[1][j + 1], inicio_da_rodada[0][j + 1]]

                # Achando os vizinhos das células do tipo (iii):
                elif i == M - 1 and 0 < j < N - 1:
                    vizinhos = [inicio_da_rodada[M - 1][j - 1], inicio_da_rodada[M - 2][j - 1],
                                inicio_da_rodada[M - 2][j], inicio_da_rodada[M - 2][j + 1],
                                inicio_da_rodada[M - 1][j + 1]]

                # Achando os vizinhos das células do tipo (iv):
                elif 0 < i < M - 1 and j == 0:
                    vizinhos = [inicio_da_rodada[i - 1][0], inicio_da_rodada[i - 1][1], inicio_da_rodada[i][1],
                                inicio_da_rodada[i + 1][1], inicio_da_rodada[i + 1][0]]

                # Achando os vizinhos das células do tipo (v):
                elif 0 < i < M - 1 and j == N - 1:
                    vizinhos = [inicio_da_rodada[i - 1][N - 1], inicio_da_rodada[i - 1][N - 2],
                                inicio_da_rodada[i][N - 2], inicio_da_rodada[i + 1][N - 2],
                                inicio_da_rodada[i + 1][N - 1]]

                # Achando os vizinhos das células do tipo (vi):
                elif i == 0 and j == 0:
                    vizinhos = [inicio_da_rodada[0][1], inicio_da_rodada[1][1], inicio_da_rodada[1][0]]

                # Achando os vizinhos das células do tipo (vii):
                elif i == 0 and j == N - 1:
                    vizinhos = [inicio_da_rodada[0][N - 2], inicio_da_rodada[1][N - 2], inicio_da_rodada[1][N - 1]]

                # Achando os vizinhos das células do tipo (viii):
                elif i == M - 1 and j == 0:
                    vizinhos = [inicio_da_rodada[M - 2][0], inicio_da_rodada[M - 2][1], inicio_da_rodada[M - 1][1]]

                # Achando os vizinhos das células do tipo (iv):
                elif i == M - 1 and j == N - 1:
                    vizinhos = [inicio_da_rodada[M - 1][N - 2], inicio_da_rodada[M - 2][N - 2],
                                inicio_da_rodada[M - 2][N - 1]]

            # Matrizes do grupo (2):
            elif M == 1 and N > 1:
                # Para esse tipo de matriz, dividi as células em 3 tipos:
                # (i) Célula mais à esquerda.
                # (ii) Células entre a primeira célula e a última célula.
                # (iii) Célula mais à direita

                # Achando os vizinhos das células do tipo (i):
                if j == 0:
                    vizinhos = [inicio_da_rodada[i][j + 1]]

                # Achando os vizinhos das células do tipo (ii):
                elif 0 < j < N - 1:
                    vizinhos = [inicio_da_rodada[i][j - 1], inicio_da_rodada[i][j + 1]]

                # Achando os vizinhos das células do tipo (iii):
                else:
                    vizinhos = [inicio_da_rodada[i][j - 1]]

            # Matrizes do grupo (3):
            elif M > 1 and N == 1:
                # Para esse tipo de matriz, dividi as células em 3 tipos:
                # (i) Célula superior.
                # (ii) Células entre a célula superior e a célula inferior.
                # (iii) Célula inferior.

                # Achando os vizinhos das células do tipo (i):
                if i == 0:
                    vizinhos = [inicio_da_rodada[i + 1][j]]

                # Achando os vizinhos das células do tipo (ii):
                elif 0 < i < M - 1:
                    vizinhos = [inicio_da_rodada[i - 1][j], inicio_da_rodada[i + 1][j]]

                # Achando os vizinhos das células do tipo (iii):
                else:
                    vizinhos = [inicio_da_rodada[i - 1][j]]

            # Matrizes do grupo (4):
            elif M == 1 and N == 1:
                # Esse tipo de matriz só tem uma célula, então não existem vizinhos.
                vizinhos = []

            # Atribui o resultado da evolução da célula á celula correspondente da matriz que armazena a situação da
            # população ao final da rodada
            final_da_rodada[i][j] = evolucao(vizinhos, inicio_da_rodada[i][j])

    # Cria uma matriz vazia para representar a situação da população no início da próxima iteração.
    inicio_da_rodada = []

    # Loop que armazena a situação da população ao final da iteração na matriz que representa a população no início de
    # uma iteração, para que a próxima iteração possa ser feita.
    for linha in final_da_rodada:
        copia = linha.copy()
        inicio_da_rodada.append(copia)

# Cria um arquivo com nome "final.txt". Nesse arquivo será impressa a
# situação final do da população presente no arquivo de exemplo selecionado
f2 = open("final.txt", "w")

# Escreve cada linha da matriz final da população em uma linha do arquivo final.txt
f2.write("Após %d iterações, a população do arquivo %s estará na seguinte situação:\n" % (numero_de_iteracoes, arquivo_exemplo))
for linha in final_da_rodada:
    aux = ''
    for i in range(len(linha) - 1):
        aux += str(linha[i]) + ' '
    aux += str(linha[len(linha) - 1])
    f2.write(aux + '\n')

# Fecha o arquivo final.txt
f2.close()
"""