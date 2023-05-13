def main():
    metrosVantagem = int(input())
    distLebre = minutos = 0
    distTarta = metrosVantagem

    while True:
        if metrosVantagem == 0: break

        distLebre += 10
        distTarta += 1
        minutos += 1
        
        if distLebre >= distTarta: break

    print(minutos)

if __name__ == '__main__':
    main()

