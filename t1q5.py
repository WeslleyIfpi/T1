def main():
    populacaoInicial = int(input())
    populacaoAtual = populacaoInicial
    anos = 1600

    while True:
        mortos = populacaoAtual * 0.06
        nascidos = populacaoAtual * 0.01
        populacaoAtual = populacaoAtual - mortos + nascidos
        
        print(f'{anos},{nascidos:.0f},{mortos:.0f},{populacaoAtual:.0f}')

        anos +=1

        

        if populacaoAtual <= (0.1 * populacaoInicial): break
        
    

if __name__ == '__main__':
    main()