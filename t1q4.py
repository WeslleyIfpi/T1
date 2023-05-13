def calcNumSorte():
    dataNasci = input()
    numSorte = 0

    for i in range(len(dataNasci)):
        numSorte += int(dataNasci[i])

    return numSorte

def main():

    numeroDaSorte = calcNumSorte()

    print(f'{numeroDaSorte}')

if __name__ == '__main__':
    main()