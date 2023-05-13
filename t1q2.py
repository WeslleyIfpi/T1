def calculaCompra(valorInicial = 10000):
    valorInicialCarro = float(input())
    meses = 0
    while True:
        valorInicialCarro *= 1.004
        valorInicial *= 1.007
        meses += 1
        if valorInicial >= valorInicialCarro: break

    return meses

def main ():
    meses = calculaCompra()
    print(f'{meses}')

if __name__ == '__main__':
    main()