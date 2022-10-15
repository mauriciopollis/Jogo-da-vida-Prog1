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
            return int(num_iteracoes)
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


def regras_evolucao(celula, vizinhanca):
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


def retorna_vizinhos(indice_linha, indice_coluna, matriz):
    vizinhos = []
    # achar vizinhos da linha de cima
    for j in range(indice_coluna - 1, indice_coluna + 2):
        try:
            if (indice_linha - 1) >= 0:
                if j >= 0:
                    vizinhos.append(matriz[indice_linha - 1][j])
        except IndexError:
            pass

    # achar vizinhos da mesma linha
    for j in range(indice_coluna - 1, indice_coluna + 2, 2):
        try:
            if j >= 0:
                vizinhos.append(matriz[indice_linha][j])
        except IndexError:
            pass

    # achar vizinhos da linha de baixo
    for j in range(indice_coluna - 1, indice_coluna + 2):
        try:
            if j >= 0:
                vizinhos.append(matriz[indice_linha + 1][j])
        except IndexError:
            pass

    return vizinhos


def jogo_da_vida(populacao_inicial, num_iteracoes):
    inicio = copia_matriz(populacao_inicial)
    populacao_apos_iteracao = copia_matriz(populacao_inicial)
    num_linhas = len(inicio)
    num_colunas = len(inicio[0])
    for _ in range(num_iteracoes):
        for i in range(num_linhas):
            for j in range(num_colunas):
                vizinhos = retorna_vizinhos(i, j, inicio)
                populacao_apos_iteracao[i][j] = regras_evolucao(inicio[i][j], vizinhos)
        inicio = copia_matriz(populacao_apos_iteracao)
    return populacao_apos_iteracao


def escreve_populacao_em_arquivo(populacao_final):
    with open('resultado.txt', 'w') as f:
        for linha in populacao_final:
            f.write(" ".join(linha) + '\n')


def copia_matriz(matriz):
    matriz_copia = []
    for linha in matriz:
        copia = linha.copy()
        matriz_copia.append(copia)
    return matriz_copia


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
